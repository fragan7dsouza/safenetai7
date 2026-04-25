#!/usr/bin/env pwsh
# ============================================================================
# PhishGuard Dashboard - Quick Start Script (PowerShell)
# ============================================================================
# Run this script to start the dashboard: .\START_DASHBOARD.ps1
# ============================================================================

Write-Host ""
Write-Host "============================================================================"
Write-Host "PhishGuard Dashboard - Starting..."
Write-Host "============================================================================"
Write-Host ""

# Change to dashboard directory
Set-Location c:\Work\safenetai7\safenetai

# Check if node_modules exists
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing dependencies..."
    npm install
}

# Start dev server
Write-Host ""
Write-Host "Starting Next.js development server..."
Write-Host ""
Write-Host "The dashboard will be available at: http://localhost:3000"
Write-Host ""

npm run dev

# After server stops
Write-Host ""
Write-Host "============================================================================"
Write-Host "Dashboard stopped. To restart, run this script again."
Write-Host "============================================================================"
