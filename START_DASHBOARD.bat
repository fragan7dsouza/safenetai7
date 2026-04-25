@echo off
REM ============================================================================
REM PhishGuard Dashboard - Quick Start Script
REM ============================================================================
REM This script will start the dashboard dev server
REM ============================================================================

echo.
echo ============================================================================
echo PhishGuard Dashboard - Starting...
echo ============================================================================
echo.

REM Change to dashboard directory
cd /d c:\Work\safenetai7\safenetai

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
)

REM Start dev server
echo.
echo Starting Next.js development server...
echo.
call npm run dev

REM After server stops, show instructions
echo.
echo ============================================================================
echo Dashboard stopped. To restart, run this script again.
echo ============================================================================
