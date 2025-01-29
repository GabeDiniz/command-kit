@echo off
echo ================================================
powershell -NoProfile -Command "& {Write-Host '          Welcome to Command Kit!' -ForegroundColor Cyan}"
echo ================================================

echo.
echo  Available Commands:
echo  -------------------
echo.

echo  SYSTEM UTILITIES
echo.
echo      config-libs
echo        - Installs all required libraries.
echo.

echo      timer ^<time-in-minutes^>
echo        - Sets a timer that alerts you with a sound once it's done.
echo.

echo      organize ^<C:\path\to\folder^>
echo        - Automatically organizes files in a folder by file type.
echo.

echo  NETWORKING and INTERNET
echo.
echo      get-api ^<API-URL^>
echo        - Fetches an API endpoint (method: GET).
echo.

echo      speed-test
echo        - Logs internet download and upload speeds at a set interval.
echo.

echo  DEVELOPMENT and GIT
echo.
echo      git-pull
echo        - Runs 'git pull' automatically for multiple repositories in the current directory.
echo.

echo      open ^<github-repo^>
echo        - Opens your GitHub project folders in VS Code.
echo        - Note: Update the `base_directory` variable with the directory 
echo            where your projects are stored. Requires `code .` to be set up.
echo.

echo  FILE and IMAGE UTILITIES
echo.
echo      convert-img ^<./directory or image.ext^> ^<png-jpg-jpeg-etc^>
echo        - Converts image formats (file by file or entire directories).
echo.

echo      ascii-art "<text>" [font]
echo        - Converts text into ASCII art. 
echo        - [font] specifies the font style (e.g., block, slant, thin).
echo        - To list available fonts, run: ascii-art --list-fonts
echo.

echo ================================================
