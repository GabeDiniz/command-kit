@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

REM Define protected branches
set PROTECTED=main master develop dev prod uat

REM Get current branch
FOR /F %%i IN ('git rev-parse --abbrev-ref HEAD') DO set CURRENT_BRANCH=%%i

echo Fetching remote...
git fetch --prune

echo Checking merged branches...
FOR /F "delims=" %%b IN ('git branch --merged ^| findstr /V "*"') DO (
    set BRANCH=%%b
    set BRANCH=!BRANCH:~2!

    REM Check if branch is protected
    set DELETE=1
    for %%p in (%PROTECTED%) do (
        if "!BRANCH!"=="%%p" set DELETE=0
    )
    if "!BRANCH!"=="%CURRENT_BRANCH%" set DELETE=0

    if "!DELETE!"=="1" (
        echo Branch to delete: !BRANCH!
        echo !BRANCH!>>.branches_to_delete.tmp
    )
)

if not exist .branches_to_delete.tmp (
    echo No merged branches to delete.
    goto end
)

echo.
set /p CONFIRM=Proceed to delete these branches locally and remotely? (y/n):
if /I not "%CONFIRM%"=="y" (
    echo Aborted.
    del .branches_to_delete.tmp
    goto end
)

REM Delete local and remote branches
for /F %%b in (.branches_to_delete.tmp) do (
    echo Deleting local branch: %%b
    git branch -d %%b

    echo Deleting remote branch: %%b
    git push origin --delete %%b
)

del .branches_to_delete.tmp
echo 🎉 Cleanup complete.

:end
endlocal
