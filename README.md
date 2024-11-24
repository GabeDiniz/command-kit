# 🛠️ Command Kit: Your All-in-One Automation Script Depot

Welcome to Command Kit! This repository is a versatile template for storing and running automation scripts, designed to boost productivity and handle system maintenance tasks. With Command Kit, you can execute various automation commands from any directory on your command line, making repetitive tasks a breeze.

# 📁 Project Structure

```
Command Kit
│
├── 📂 bin
│   ├── dependency-check.bat        # Installs required Python libraries
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

Once the repository is cloned, simply run the `config.bat` file as **Administrator** to add the bin folder to your path environment variable. From there, you can open a command prompt and run any of the following commands from any directory. You may need to run the dependency-check command to install required libraries for some scripts.

Run 'commands' in the command prompt to get a list of current available commands.
