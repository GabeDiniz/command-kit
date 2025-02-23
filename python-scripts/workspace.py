import sys
import webbrowser
import os
import yaml

# Define the YAML file path for workspaces
script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
WORKSPACE_FILE = os.path.normpath(os.path.join(script_dir, "../data/workspaces.yaml"))

def load_workspaces():
  """Load workspaces from the YAML file."""
  if not os.path.exists(WORKSPACE_FILE):
    print("❌ Error: Workspace file not found.")
    return {}

  try:
    with open(WORKSPACE_FILE, "r", encoding="utf-8") as file:
      return yaml.safe_load(file) or {}
  except yaml.YAMLError as e:
    print(f"❌ Error loading YAML file: {e}")
    return {}
    

def list_workspaces():
  """Lists all available workspaces."""
  workspaces = load_workspaces()
  if not workspaces:
    print("📌 No workspaces defined. Add one using: python workspace.py add <name> <url1> <url2> ...")
  else:
    print("📌 Available workspaces:")
    for name, urls in workspaces.items():
      print(f"  - {name}: {', '.join(urls)}")

def open_workspace(workspace_name):
  """Opens all URLs associated with the given workspace."""
  workspaces = load_workspaces()

  if workspace_name in workspaces:
    print(f"🌐 Opening workspace: {workspace_name}")
    for url in workspaces[workspace_name]:
      print(f"🔗 Opening: {url}")
      webbrowser.open(url)
    print("✅ All tabs opened successfully.")
  else:
    print(f"❌ Workspace '{workspace_name}' not found.")
    print("📌 Available workspaces:", ", ".join(workspaces.keys()))
    
def add_workspace(workspace_name, urls):
  """Adds a new workspace to the YAML file."""
  workspaces = load_workspaces()
  workspaces[workspace_name] = urls
  save_workspaces(workspaces)
  print(f"✅ Workspace '{workspace_name}' added successfully!")

def save_workspaces(workspaces):
  """Save workspaces to the YAML file."""
  print(WORKSPACE_FILE)
  with open(WORKSPACE_FILE, "w", encoding="utf-8") as file:
    yaml.dump(workspaces, file, default_flow_style=False)
  print("✅ Workspaces saved successfully!")

def remove_workspace(workspace_name):
  """Removes a workspace from the YAML file."""
  workspaces = load_workspaces()

  if workspace_name in workspaces:
    del workspaces[workspace_name]  # Delete the workspace
    save_workspaces(workspaces)
    print(f"✅ Workspace '{workspace_name}' removed successfully!")
  else:
    print(f"❌ Workspace '{workspace_name}' not found.")
    print("📌 Available workspaces:", ", ".join(workspaces.keys()))

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("📌 Usage:")
    print("  python workspace.py <workspace-name>  # Open a workspace")
    print("  python workspace.py add <name> <url1> <url2> ...  # Add a new workspace")
    print("  python workspace.py list  # List all workspaces")
    sys.exit(1)

  command = sys.argv[1].lower()

  if command == "add" and len(sys.argv) > 3:
    workspace_name = sys.argv[2]
    urls = sys.argv[3:]
    add_workspace(workspace_name, urls)
  elif command == "remove" and len(sys.argv) > 2:
    workspace_name = sys.argv[2]
    remove_workspace(workspace_name)
  elif command == "list":
    list_workspaces()
  else:
    open_workspace(command)
