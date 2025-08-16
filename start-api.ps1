# Start HelmBot API Server (PowerShell)

Write-Host "🚀 Starting HelmBot API Server..." -ForegroundColor Green

# Check if virtual environment exists
if (!(Test-Path ".venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
& ".venv\Scripts\Activate.ps1"

# Install requirements
Write-Host "📋 Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt

# Start the server
Write-Host "🌐 Starting FastAPI server on http://localhost:8000" -ForegroundColor Green
Write-Host "📚 API Documentation available at http://localhost:8000/docs" -ForegroundColor Cyan
python -m api.server
