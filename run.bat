@echo off
cd /d "%~dp0"
if not exist venv\Scripts\python.exe (
    echo Creating Python virtual environment...
    py -m venv venv
    if errorlevel 1 goto error
)
echo Installing required package...
venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto error
echo.
echo Starting SkyRoute. Open http://127.0.0.1:5000 in your browser.
venv\Scripts\python.exe app.py
goto end
:error
echo.
echo Setup failed. Please install Python 3.10+ and ensure the 'py' command works.
:end
pause
