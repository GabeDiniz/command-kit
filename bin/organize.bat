@echo off
setlocal enabledelayedexpansion

:: Set default source directory to the current working directory
set "source=%cd%"

:: Check if a parameter is provided, use it as the source directory
if not "%~1"=="" set "source=%~1"

:: Ensure the source directory exists
if not exist "%source%" (
    echo ❌ Error: The directory "%source%" does not exist.
    exit /b 1
)

echo 📂 Organizing files in: %source%

:: Iterate through all files in the directory
for %%f in ("%source%\*.*") do (
    set "ext=%%~xf"
    set "ext=!ext:~1!"  :: Remove the leading dot

    if not "!ext!"=="" ( 
        if not exist "%source%\!ext!\" mkdir "%source%\!ext!"
        move "%%f" "%source%\!ext!\"
    )
)

echo ✅ Organization complete!
endlocal