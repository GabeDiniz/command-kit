@echo off

REM Get the current directory
set "current_dir=%cd%"

REM Check if the current directory is already in the PATH
echo %PATH% | find /i "%current_dir%" >nul
if %errorlevel%==0 (
    echo The current directory is already in the PATH.
) else (
    REM Use PowerShell to add the current directory to the PATH
    echo Adding %current_dir% to the PATH.
    powershell -Command "[Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';%current_dir%', 'Machine')"

    REM Confirm the addition
    if %errorlevel%==0 (
        echo Successfully added %current_dir% to the PATH.
    ) else (
        echo Failed to add %current_dir% to the PATH. Try running as administrator.
    )
)

pause
