# 🛠️ Command Kit: Your All-in-One Automation Script Depot

Welcome to Command Kit! This repository is a versatile template for storing and running automation scripts, designed to boost productivity and handle system maintenance tasks. With Command Kit, you can execute various automation commands from any directory on your command line, making repetitive tasks a breeze.

# 📁 Project Structure

```
Command Kit
│
├── 📂 bin
│   ├── config-libs.bat             # Installs required Python libraries
│   ├── config.bat                  # Must be run from the directory - adds the bin directory to your path env
│   └── <other batch scripts>       # Additional batch scripts for quick commands
│
├── 📂 Scripts
│   └── <other Python scripts>      # Python scripts for various automation tasks
│
├── README.md                       # Project documentation
└── requirements.txt                # Python libraries required for this project
```

# 🚀 Getting Started

### Running Commands

Once the repository is cloned, simply run the `config.bat` file as **Administrator** to add the bin folder to your path environment variable. From there, you can open a command prompt and run any of the following commands from any directory. You may need to run the config-libs command to install required libraries for some scripts.

Run 'commands' in the command prompt to get a list of current available commands.

# ✍ Contributing

We welcome contributions to Command Kit! To maintain a consistent structure and ensure ease of use, please follow these guidelines when adding new scripts or features:

1. Scripts Folder:

- All scripts should be placed inside the scripts folder. This keeps the repository organized and makes it easier to locate the scripts.
- Use clear and descriptive filenames for your scripts, indicating their purpose (e.g., cleanup_logs.py, generate_report.bat).

2. Bin Folder:

- For every script added to the scripts folder, create a callable batch file or command that resides in the bin folder. This allows users to easily execute scripts from the command line.
- The batch file should invoke the corresponding script from the scripts folder. For example:

```bat
Copy code
@echo off
python "%~dp0\..\scripts\your_script_name.py" %\*
```

3. Coding Standards:

- Use clean and readable code with comments explaining non-obvious logic.
- Follow best practices for the scripting language you are using.

By following these steps, you'll help keep Command Kit organized, user-friendly, and easy to maintain. Thank you for your contributions! 🚀
