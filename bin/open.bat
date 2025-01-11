@echo off

@REM Default directory for your projects
set "base_directory=C:\Users\gabri\Desktop\Code"
set "repo_name=%1"
set "repo_path=%base_directory%\%repo_name%"

if exist "%repo_path%" (
    cd "%repo_path%"
    code .
) else (
    echo Repository "%repo_name%" does not exist in %base_directory%.
)
