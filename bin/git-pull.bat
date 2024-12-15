@echo off

REM Get the current directory
set "current_dir=%cd%"

REM Iterate over all subdirectories in the current directory
for /d %%d in ("%current_dir%\*") do (
    echo .
    echo Pulling changes in %%d...
    cd %%d
    git pull
    cd "%current_dir%"
)