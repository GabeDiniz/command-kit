@echo off
echo ================================================
powershell -NoProfile -Command "& {Write-Host '          Welcome to Custom Scripts!' -ForegroundColor Cyan}"
echo ================================================

echo.
echo  Commands available:
echo.

echo.
echo  config-libs
echo    - Used for installing all required libraries
echo.

echo  timer ^<time-in-minutes^>
echo    - Set a timer that alerts you with a sound once its done
echo.

echo  example-command ^<parameter^>
echo    - This command does something
echo.

echo ================================================
