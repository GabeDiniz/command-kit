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

echo  get-api ^<API-URL^>
echo    - Fetches an API endpoint (method GET)
echo.

echo  git-pull
echo    - Automatically git pull for multiple repositories in the directory you're in.
echo.

echo  organize ^<C:\path\to\folder^>
echo    - Automatically organize files in a folder based on extensions.
echo.
 
echo  example-command ^<parameter^>
echo    - This command does something
echo.

echo ================================================
