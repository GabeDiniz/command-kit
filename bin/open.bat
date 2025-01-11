@echo off

:: Check if a parameter is passed
if "%1"=="" (
    echo You must provide the name of the GitHub repository.
    echo Usage: open.bat ^<github-repo^>
    exit /b 1
)

:: Default directory for your projects
set "base_directory=C:\Users\gabri\Desktop\Code"
set "repo_name=%1"
set "repo_path=%base_directory%\%repo_name%"

:: Check if the repository exists
if exist "%repo_path%" (
    cd "%repo_path%"
    code .
) else (
    echo Error: Repository "%repo_name%" does not exist in %base_directory%.
    exit /b 1
)