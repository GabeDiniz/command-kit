import sys
import webbrowser

# Define workspaces here with associated URLs
WORKSPACES = {
  "coding": [
    "https://github.com/GabeDiniz",
    "https://www.youtube.com"
  ],
}

def list_workspaces():
  '''
  func. description.
  '''
  print("Available workspaces:", ", ".join(WORKSPACES.keys()))

def open_workspace(workspace_name):
  '''
  func. description.
  '''
  if workspace_name in WORKSPACES:
    print(f"🌐 Opening workspace: {workspace_name}")
    for url in WORKSPACES[workspace_name]:
      print(f"🔗 Opening: {url}")
      webbrowser.open(url)
    print("✅ All tabs opened successfully.")
  else:
    print(f"❌ Workspace '{workspace_name}' not found.")
    list_workspaces()
    

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("📌 Usage: python workspace.py <workspace-name>")
    list_workspaces()
  else:
    open_workspace(sys.argv[1])
