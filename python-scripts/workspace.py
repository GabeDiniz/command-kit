import sys
import webbrowser
import os
import yaml
import subprocess

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define workspace file relative to script location
WORKSPACE_FILE = os.path.normpath(os.path.join(script_dir, "../data/workspaces.yaml"))

def load_workspaces():
  """Load workspaces from the YAML file."""
  if not os.path.exists(WORKSPACE_FILE):
    print(f"❌ Error: Workspace file not found at {WORKSPACE_FILE}")
    return {}

  try:
    with open(WORKSPACE_FILE, "r", encoding="utf-8") as file:
      return yaml.safe_load(file) or {}
  except yaml.YAMLError as e:
    print(f"❌ Error loading YAML file: {e}")
    return {}

def save_workspaces(workspaces):
  """Save workspaces to the YAML file."""
  with open(WORKSPACE_FILE, "w", encoding="utf-8") as file:
    yaml.dump(workspaces, file, default_flow_style=False)
  print("✅ Workspaces saved successfully!")

def open_workspace(workspace_name):
  """Opens all resources associated with the given workspace."""
  workspaces = load_workspaces()

  if workspace_name not in workspaces:
    print(f"❌ Workspace '{workspace_name}' not found.")
    print("📌 Available workspaces:", ", ".join(workspaces.keys()))
    return

  print(f"🌐 Opening workspace: {workspace_name}")

  for action, items in workspaces[workspace_name].items():
    for item in items:
      if action == "chrome":
        print(f"🔗 Opening in Chrome: {item}")
        webbrowser.open(item)

      elif action == "code":
        print(f"📝 Opening in VS Code: {item}")
        item = os.path.normpath(item)
        subprocess.run(["code", item], check=False, shell=True)

      elif action == "terminal":
        print(f"💻 Running terminal command: {item}")
        # subprocess.run(["gnome-terminal", "--", "bash", "-c", item], check=False)  # For Linux
        subprocess.run(["open", "-a", "Terminal", item], check=False)  # For macOS

      elif action == "explorer":
        print(f"📂 Opening in File Explorer: {item}")
        subprocess.run(["explorer", item], check=False)  # Windows only

  print("✅ All tasks completed.")

def add_workspace(workspace_name, action, items):
  """Adds a new action to a workspace in the YAML file."""
  workspaces = load_workspaces()
  
  if workspace_name not in workspaces:
    workspaces[workspace_name] = {}

  if action not in workspaces[workspace_name]:
    workspaces[workspace_name][action] = []

  workspaces[workspace_name][action].extend(items)
  save_workspaces(workspaces)
  print(f"✅ Added '{action}' to workspace '{workspace_name}'.")

def remove_workspace(workspace_name):
  """Removes a workspace from the YAML file."""
  workspaces = load_workspaces()

  if workspace_name in workspaces:
    del workspaces[workspace_name]
    save_workspaces(workspaces)
    print(f"✅ Workspace '{workspace_name}' removed successfully!")
  else:
    print(f"❌ Workspace '{workspace_name}' not found.")
    print("📌 Available workspaces:", ", ".join(workspaces.keys()))

def list_workspaces():
  """Lists all available workspaces."""
  workspaces = load_workspaces()
  if not workspaces:
    print("📌 No workspaces defined. Add one using: python workspace.py add <name> <action> <item1> <item2> ...")
  else:
    print("📌 Available workspaces:")
    for name, actions in workspaces.items():
      print(f"  - {name}:")
      for action, items in actions.items():
        print(f"    📌 {action}: {', '.join(items)}")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("📌 Usage:")
    print("  python workspace.py <workspace-name>  # Open a workspace")
    print("  python workspace.py add <name> <action> <item1> <item2> ...  # Add a new action to a workspace")
    print("  python workspace.py remove <name>  # Remove a workspace")
    print("  python workspace.py list  # List all workspaces")
    sys.exit(1)

  command = sys.argv[1].lower()

  if command == "add" and len(sys.argv) > 4:
    workspace_name = sys.argv[2]
    action = sys.argv[3]
    items = sys.argv[4:]
    add_workspace(workspace_name, action, items)
  elif command == "remove" and len(sys.argv) > 2:
    workspace_name = sys.argv[2]
    remove_workspace(workspace_name)
  elif command == "list":
    list_workspaces()
  else:
    open_workspace(command)
