@echo off
setlocal
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -NoLogo -File .\env\dev\run_tests_internal.ps1

endlocal

echo %CMDCMDLINE% | findstr /C:"/c" >nul
if %errorlevel% == 0 (
    cmd /k
)
