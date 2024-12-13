@echo off

REM Check if parameter is provided
if "%1"=="" (
  echo Usage: organize ^<C:\path\to\folder^>
  exit /b 1
)

set "source=%1"

for %%f in ("%source%\*") do (
    for %%x in (%%~xf) do (
        if not exist "%source%\%%x\" mkdir "%source%\%%x"
        move "%%f" "%source%\%%x\"
    )
)