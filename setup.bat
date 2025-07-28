@echo off
echo.
echo Python Virtual Environment Setup For Windows
echo.

python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Environment is ready
pause
