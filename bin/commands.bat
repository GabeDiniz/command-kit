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

echo  convert_img ^<./directory or image.ext^> ^<png-jpg-jpeg-etc^>
echo    - Automatically convert image types file by file or by directory.
echo.

echo  open ^<github-repo^>
echo    - Open your GitHub project folders in VS Code. 
echo    - Note, you must edit the base_directory parameter with the
echo      directory where your projects are stored. Requires `code .`
echo      to be configured for opening directories in VS Code.
echo.
 
echo  example-command ^<parameter^>
echo    - This command does something
echo.

echo ================================================
