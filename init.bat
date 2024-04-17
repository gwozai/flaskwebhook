@echo off
setlocal

rem Set the virtual environment directory
set VENV_DIR=.\venv

rem Check if the virtual environment exists, if not, create it
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

rem Activate the virtual environment
echo Entering virtual environment...
call %VENV_DIR%\Scripts\activate

rem Upgrade pip if needed
echo Checking for pip upgrade...
%VENV_DIR%\Scripts\python.exe -m pip install --upgrade pip

rem Install or update dependencies
echo Installing or updating dependencies...
pip install -r requirements.txt --upgrade

rem Generate the requirements file
echo Generating requirements file...
pip freeze > requirements.txt

rem Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

echo Done!
