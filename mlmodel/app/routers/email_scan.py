# app/routers/email_scan.py
from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import os
import pandas as pd
from app.utils.preprocess import preprocess_text
from typing import List

router = APIRouter()

# Load the trained model and vectorizer
model = joblib.load("app/models/email_model.pkl")
vectorizer = joblib.load("app/models/email_vectorizer.pkl")

class EmailRequest(BaseModel):
    text_content: str
    sender_domain: str = ""

class EmailPrediction(BaseModel):
    prediction: str
    confidence: float
    red_flag_words: List[str] = []

@router.post("/", response_model=EmailPrediction)
def predict_email(data: EmailRequest):
    cleaned = {
        "cleaned_text": preprocess_text(data.text_content),
        "cleaned_domain": data.sender_domain.lower().replace("www.", "")
    }
    
    # Transform input
    X = vectorizer.transform(pd.DataFrame([cleaned]))
    
    # Predict probabilities and class
    prob = model.predict_proba(X)[0]
    pred = model.predict(X)[0] # 1 for Legit, 0 for Fake
    
    # Extract red flag words if it's Fake (or even if it's not, we can show what pulled it towards Fake)
    red_flags = []
    
    if hasattr(model, "coef_") and hasattr(vectorizer, "get_feature_names_out"):
        feature_names = vectorizer.get_feature_names_out()
        coef = model.coef_[0] # Positive pushes to 1 (Legit), Negative pushes to 0 (Fake)
        
        # Get non-zero features for this specific text
        nonzero_indices = X.nonzero()[1]
        
        # Sort features by coefficient (most negative first = strongest indicator of Fake)
        sorted_indices = sorted(nonzero_indices, key=lambda i: coef[i])
        
        # Collect top 3-5 negative features
        for i in sorted_indices:
            if coef[i] < -0.1: # Only include if it has a meaningful negative weight
                word = feature_names[i]
                # feature names might have prefixes from ColumnTransformer, e.g., 'text_vec__urgent'
                if "__" in word:
                    word = word.split("__")[1]
                if word not in red_flags:
                    red_flags.append(word)
            
            if len(red_flags) >= 5:
                break

    return {
        "prediction": "Legit" if pred == 1 else "Fake",
        "confidence": round(prob[0] * 100, 2) if pred == 0 else round(prob[1] * 100, 2), # Return % confidence of the predicted class
        "red_flag_words": red_flags if pred == 0 else [] # Only return red flags if predicted as Fake
    }
