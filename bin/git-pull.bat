@echo off
chcp 65001 >nul  & REM Set UTF-8 Encoding

:: Get the current directory
set "CURRENT_DIR=%cd%"

echo 📂 Scanning subdirectories in: %CURRENT_DIR%

:: Iterate over all subdirectories
for /d %%D in (*) do (
    if exist "%%D\.git" (
        echo.
        echo 🔄 Pulling changes in: %%D
        cd "%%D"
        git pull
        cd "%CURRENT_DIR%"
    ) else (
        echo ⚠️ Skipping %%D (Not a Git repository)
    )
)

echo.
echo ✅ All repositories updated.
