#!/bin/bash

# Get the absolute path of the current directory
CURRENT_DIR="$(pwd)"

# Define shell profile file (based on the system)
PROFILE_FILE=""
if [ -f "$HOME/.bashrc" ]; then
    PROFILE_FILE="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    PROFILE_FILE="$HOME/.zshrc"
elif [ -f "$HOME/.bash_profile" ]; then
    PROFILE_FILE="$HOME/.bash_profile"
elif [ -f "$HOME/.profile" ]; then
    PROFILE_FILE="$HOME/.profile"
else
    echo "❌ No compatible shell profile found!"
    exit 1
fi

# Check if the directory is already in PATH
if echo "$PATH" | grep -q "$CURRENT_DIR"; then
    echo "✅ The current directory is already in the PATH."
else
    echo "🛠  Adding $CURRENT_DIR to the PATH..."
    echo "export PATH=\"\$PATH:$CURRENT_DIR\"" >> "$PROFILE_FILE"

    # Apply changes to the current session
    export PATH="$PATH:$CURRENT_DIR"
    echo "✅ Successfully added $CURRENT_DIR to PATH."
    echo "🔄 Restart your terminal or run: source $PROFILE_FILE"
fi

# Make all scripts in the current directory executable
echo "🔧 Granting execute permission to all scripts in $CURRENT_DIR..."
chmod +x "$CURRENT_DIR"/* 2>/dev/null
echo "✅ All scripts in $CURRENT_DIR are now executable."

