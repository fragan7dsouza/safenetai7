# Graph Report - C:\Work\safenetai7  (2026-04-25)

## Corpus Check
- 85 files · ~41,548 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 399 nodes · 539 edges · 69 communities detected
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 90 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]

## God Nodes (most connected - your core abstractions)
1. `EmailContext` - 45 edges
2. `PipelineResult` - 24 edges
3. `run_pipeline()` - 10 edges
4. `_process_message()` - 9 edges
5. `parse_email()` - 8 edges
6. `check_authentication()` - 8 edges
7. `check_threat_intel()` - 8 edges
8. `predict_doc()` - 8 edges
9. `_normalize_domain()` - 8 edges
10. `_cached_call()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `pipeline/l1_authentication.py — SPF / DKIM / DMARC verification + display name s` --uses--> `EmailContext`  [INFERRED]
  C:\Work\safenetai7\email\pipeline\l1_authentication.py → C:\Work\safenetai7\email\pipeline\email_parser.py
- `Extract spf=, dkim=, dmarc= results from the Authentication-Results header.` --uses--> `EmailContext`  [INFERRED]
  C:\Work\safenetai7\email\pipeline\l1_authentication.py → C:\Work\safenetai7\email\pipeline\email_parser.py
- `Fallback SPF check: look up the TXT record for sender_domain and check     whet` --uses--> `EmailContext`  [INFERRED]
  C:\Work\safenetai7\email\pipeline\l1_authentication.py → C:\Work\safenetai7\email\pipeline\email_parser.py
- `Score SPF result. Prefer parsed Authentication-Results; fall back to DNS.` --uses--> `EmailContext`  [INFERRED]
  C:\Work\safenetai7\email\pipeline\l1_authentication.py → C:\Work\safenetai7\email\pipeline\email_parser.py
- `Score DKIM result from Authentication-Results.` --uses--> `EmailContext`  [INFERRED]
  C:\Work\safenetai7\email\pipeline\l1_authentication.py → C:\Work\safenetai7\email\pipeline\email_parser.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (41): get_gmail_service(), gmail_client.py — OAuth 2.0 authentication and Gmail API resource factory.  Fl, Authenticate with Gmail via OAuth 2.0 and return a Gmail API service object., get_supabase_client(), _apply_labels(), apply_phishguard_label(), apply_verdict_labels(), ensure_all_labels_exist() (+33 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (37): EmailContext, All data extracted from a single email, passed between pipeline stages.      t, aggregate_l3_score(), _cached_call(), check_threat_intel(), CollegeDBScanResult, _days_since(), DomainScanResult (+29 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (23): _get_domain(), pipeline/l2_heuristics.py — Deterministic rule engine (mirrors EOP Transport Rul, Urgency or scarcity language designed to bypass critical thinking., Phrases associated with credential collection / account-takeover phishing., Very short/empty body + attachment = delivery vehicle phishing.     All the mal, Sender address starts with common spoofed prefix patterns (no-reply-, security-), Sender uses a free email provider (gmail, yahoo, etc.) but the display name, More than 5 URLs suggests link-spam or a phishing kit with decoy links. (+15 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (19): check_heuristics(), Run all heuristic rules against the email context.      Args:         ctx: Pa, check_nlp(), classify_email(), pipeline/l2_nlp.py — TF-IDF + Logistic Regression phishing classifier.  Mirror, Full NLP stage: classify + score.      Args:         body_text:   Plain text, Classify an email body as phishing or ham.      Args:         body_text: Plai, Convert a (label, confidence) pair into an SCL score contribution.      Scorin (+11 more)

### Community 4 - "Community 4"
Cohesion: 0.15
Nodes (19): BaseModel, clean_text_for_offer(), count_matches(), EmailPrediction, EmailRequest, extract_features(), get_red_flags(), has_fee_demand() (+11 more)

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (15): compose_guard_scan(), _domain_is_ip(), _email_model_score(), _email_rule_signals(), _extract_recipient_domains(), _link_model_score(), _normalize_domain(), _preprocess_url() (+7 more)

### Community 6 - "Community 6"
Cohesion: 0.17
Nodes (15): check_authentication(), _check_display_name_spoofing(), _check_dkim(), _check_dmarc(), _check_spf(), _parse_auth_results(), pipeline/l1_authentication.py — SPF / DKIM / DMARC verification + display name s, Score DKIM result from Authentication-Results. (+7 more)

### Community 7 - "Community 7"
Cohesion: 0.17
Nodes (13): extract_text_from_docx(), extract_text_from_pdf(), calculate_risk_score(), extract_phishing_features(), find_suspicious_indicators(), get_risk_level(), predict_doc(), Calculate an overall risk score based on indicators (+5 more)

### Community 8 - "Community 8"
Cohesion: 0.2
Nodes (13): _decode_header_value(), _extract_domain(), _extract_urls(), parse_email(), pipeline/email_parser.py — Parses raw MIME bytes into a structured EmailContext., Convert HTML to readable plain text using BeautifulSoup., Recursively walk the MIME tree to collect:       - body_text (from text/plain p, Parse a raw MIME string into a structured EmailContext.      Args:         ra (+5 more)

### Community 9 - "Community 9"
Cohesion: 0.26
Nodes (12): call_mcp_tool(), _next_id(), pipeline/mcp_client.py — MCP stdio JSON-RPC client for the VirusTotal MCP server, Call a VirusTotal MCP tool and return the parsed result dict.      Args:, Write a JSON-RPC message to the TCP socket (newline-delimited)., Read one newline-delimited JSON-RPC message from the TCP socket., Read responses until we get the one matching expected_id.     Notifications (no, Connect to the VT MCP server running over TCP and perform the MCP handshake. (+4 more)

### Community 10 - "Community 10"
Cohesion: 0.4
Nodes (9): _clean_text(), _count(), detect_offer_scam(), _extract_features(), _get_red_flags(), _has_fee_demand(), _is_offer_related(), Return True if the message is about a job/internship offer. (+1 more)

### Community 11 - "Community 11"
Cohesion: 0.44
Nodes (8): clean_text(), count_matches(), extract_features(), get_red_flags(), has_fee_demand(), main(), Train a custom ML model for detecting fake internship/job offers. Uses hand-eng, Check if text demands payment of a FEE (not just mentioning stipend).

### Community 12 - "Community 12"
Cohesion: 0.32
Nodes (7): _convert(), _download(), download_dataset(), data/download_dataset.py -- Downloads a phishing email dataset to data/emails.cs, Try each source in order; stop after the first successful download + conversion., Download url to dest. Returns True on success., Read raw_path, normalize columns to (text, label) using source mapping,     and

### Community 13 - "Community 13"
Cohesion: 0.32
Nodes (6): deleteDomain(), deleteUrl(), fetchData(), Synchronous Supabase query for scam URLs., _sync_check_scam_urls(), Select()

### Community 14 - "Community 14"
Cohesion: 0.36
Nodes (5): buildCorsHeaders(), findFirstUrl(), OPTIONS(), POST(), processMessageInBackground()

### Community 15 - "Community 15"
Cohesion: 0.33
Nodes (4): assertAdmin(), getAdminEmails(), isAdminUser(), DashboardPage()

### Community 16 - "Community 16"
Cohesion: 0.33
Nodes (2): isJsonValue(), toJsonValue()

### Community 17 - "Community 17"
Cohesion: 0.33
Nodes (0): 

### Community 18 - "Community 18"
Cohesion: 0.33
Nodes (2): mapStatusLabel(), StatusBadge()

### Community 19 - "Community 19"
Cohesion: 0.4
Nodes (3): createQueryClient(), getQueryClient(), TRPCReactProvider()

### Community 20 - "Community 20"
Cohesion: 0.4
Nodes (4): watch_manager.py — Registers a Gmail Pub/Sub watch on the user's inbox.  Impor, Register (or re-register) a Gmail Pub/Sub watch on the inbox.      Each call o, # NOTE: In Phase 2, persist historyId to a database / Redis so the, register_watch()

### Community 21 - "Community 21"
Cohesion: 0.4
Nodes (4): clean_text(), extract_phishing_features(), Basic text cleaning while preserving some structure, Extract additional phishing-related features from text

### Community 22 - "Community 22"
Cohesion: 0.4
Nodes (0): 

### Community 23 - "Community 23"
Cohesion: 0.4
Nodes (2): createContext(), createTRPCContext()

### Community 24 - "Community 24"
Cohesion: 0.5
Nodes (2): health_check(), Render uses this to verify the container is healthy.

### Community 25 - "Community 25"
Cohesion: 0.5
Nodes (0): 

### Community 26 - "Community 26"
Cohesion: 0.67
Nodes (2): load(), normalizeBaseUrl()

### Community 27 - "Community 27"
Cohesion: 0.5
Nodes (0): 

### Community 28 - "Community 28"
Cohesion: 0.67
Nodes (0): 

### Community 29 - "Community 29"
Cohesion: 0.67
Nodes (0): 

### Community 30 - "Community 30"
Cohesion: 0.67
Nodes (0): 

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (1): config.py — Central configuration loader for PhishGuard. All runtime settings a

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (0): 

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (0): 

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (0): 

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (0): 

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (0): 

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (0): 

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (0): 

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (0): 

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (0): 

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (0): 

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (0): 

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (0): 

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (0): 

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (0): 

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (0): 

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (0): 

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (0): 

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (0): 

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (0): 

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (0): 

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (0): 

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (0): 

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (0): 

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (0): 

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (0): 

### Community 59 - "Community 59"
Cohesion: 1.0
Nodes (0): 

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (0): 

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (0): 

### Community 62 - "Community 62"
Cohesion: 1.0
Nodes (0): 

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (0): 

### Community 64 - "Community 64"
Cohesion: 1.0
Nodes (0): 

### Community 65 - "Community 65"
Cohesion: 1.0
Nodes (0): 

### Community 66 - "Community 66"
Cohesion: 1.0
Nodes (0): 

### Community 67 - "Community 67"
Cohesion: 1.0
Nodes (0): 

### Community 68 - "Community 68"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **46 isolated node(s):** `config.py — Central configuration loader for PhishGuard. All runtime settings a`, `gmail_client.py — OAuth 2.0 authentication and Gmail API resource factory.  Fl`, `Authenticate with Gmail via OAuth 2.0 and return a Gmail API service object.`, `watch_manager.py — Registers a Gmail Pub/Sub watch on the user's inbox.  Impor`, `Register (or re-register) a Gmail Pub/Sub watch on the inbox.      Each call o` (+41 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 31`** (2 nodes): `config.py`, `config.py — Central configuration loader for PhishGuard. All runtime settings a`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `PendingApprovals.tsx`, `PendingApprovals()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `extractor.py`, `extract_text_from_file()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `generate_dataset.py`, `generate_message()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `train_link_model.py`, `preprocess_url()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (2 nodes): `seed-one-report.mjs`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (2 nodes): `seed.mjs`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (2 nodes): `middleware.ts`, `middleware()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (2 nodes): `page.tsx`, `SignupPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `page.tsx`, `ExtensionDownloadPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (2 nodes): `cn()`, `badge.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (2 nodes): `cn()`, `button.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `textarea.tsx`, `cn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `utils.ts`, `cn()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `db.ts`, `createPrismaClient()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (1 nodes): `START_DASHBOARD.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `eslint.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `postcss.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `tailwind.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `vite.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `eslint.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `next-env.d.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `next.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `postcss.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `prettier.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `auth.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `env.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (1 nodes): `layout.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `page.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `route.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `input.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `root.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (1 nodes): `auth.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (1 nodes): `report.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (1 nodes): `server.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (1 nodes): `next-auth.d.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (1 nodes): `backend.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `EmailContext` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 6`, `Community 8`, `Community 13`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Why does `PipelineResult` connect `Community 0` to `Community 3`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `run_pipeline()` connect `Community 3` to `Community 0`, `Community 8`, `Community 6`, `Community 1`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `EmailContext` (e.g. with `pipeline/l1_authentication.py — SPF / DKIM / DMARC verification + display name s` and `Extract spf=, dkim=, dmarc= results from the Authentication-Results header.`) actually correct?**
  _`EmailContext` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Are the 20 inferred relationships involving `PipelineResult` (e.g. with `label_manager.py — Creates and applies PhishGuard Gmail labels.  Phase 2 adds` and `Resolve a label to its Gmail ID. Creates it if it does not yet exist.     Cache`) actually correct?**
  _`PipelineResult` has 20 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `run_pipeline()` (e.g. with `_process_message()` and `parse_email()`) actually correct?**
  _`run_pipeline()` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `_process_message()` (e.g. with `run_pipeline()` and `apply_verdict_labels()`) actually correct?**
  _`_process_message()` has 3 INFERRED edges - model-reasoned connections that need verification._