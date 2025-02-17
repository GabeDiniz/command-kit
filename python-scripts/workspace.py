import sys
import webbrowser

# Define workspaces here with associated URLs
WORKSPACES = {
    "coding": [
        "https://github.com",
        "https://www.youtube.com"
    ],
}

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
        print("📌 Available workspaces:", ", ".join(WORKSPACES.keys()))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("📌 Usage: python workspace.py <workspace-name>")
        print("🔹 Example: python workspace.py coding")
    else:
        open_workspace(sys.argv[1])
