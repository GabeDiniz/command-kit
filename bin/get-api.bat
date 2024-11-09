@echo off
REM Check if parameter is provided
if "%1"=="" (
  echo Usage: get ^<api-url^>
  exit /b 1
)

set "URL=%1"

REM Debug output
echo Running curl --request GET %URL%

curl --request GET %URL%