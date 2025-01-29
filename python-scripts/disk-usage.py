import os
from pathlib import Path

def format_size(size_in_bytes):
  """
  Formats the file size into human-readable format (e.g., KB, MB, GB).
  """
  for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
    if size_in_bytes < 1024:
      return f"{size_in_bytes:.2f} {unit}"
    size_in_bytes /= 1024

def get_largest_files(directory, top_n=10):
  """
  Finds the largest files in the given directory and its subdirectories.

  Args:
      directory (str): Path to the directory to analyze.
      top_n (int): Number of largest files to display.

  Returns:
      list: A list of tuples (file_path, file_size).
  """
  largest_files = []
  for root, _, files in os.walk(directory):
      for file in files:
          file_path = os.path.join(root, file)
          try:
              file_size = os.path.getsize(file_path)
              largest_files.append((file_path, file_size))
          except (PermissionError, FileNotFoundError):
              # Skip files that cannot be accessed
              continue
  # Sort by file size in descending order and return the top N results
  largest_files.sort(key=lambda x: x[1], reverse=True)
  return largest_files[:top_n]

def get_largest_folders(directory, top_n=10):
    """
    Finds the largest folders (by cumulative size) in the given directory.

    Args:
        directory (str): Path to the directory to analyze.
        top_n (int): Number of largest folders to display.

    Returns:
        list: A list of tuples (folder_path, folder_size).
    """
    folder_sizes = {}
    for root, dirs, files in os.walk(directory):
        folder_size = 0
        for file in files:
            file_path = os.path.join(root, file)
            try:
                folder_size += os.path.getsize(file_path)
            except (PermissionError, FileNotFoundError):
                continue
        folder_sizes[root] = folder_size
    # Sort by folder size in descending order and return the top N results
    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
    return sorted_folders[:top_n]

if __name__ == "__main__":
    directory = input("Enter the directory to analyze (default: current directory): ").strip()
    if not directory:
        directory = os.getcwd()

    if not os.path.exists(directory):
        print(f"❌ Error: Directory '{directory}' does not exist.")
    else:
        top_n = 10  # Default to showing top 10
        print(f"\n🔍 Analyzing disk usage in: {directory}\n")

        # Largest files
        print(f"📄 Top {top_n} Largest Files:")
        largest_files = get_largest_files(directory, top_n=top_n)
        for i, (file_path, size) in enumerate(largest_files, 1):
            print(f"{i}. {file_path} - {format_size(size)}")

        # Largest folders
        print(f"\n📁 Top {top_n} Largest Folders:")
        largest_folders = get_largest_folders(directory, top_n=top_n)
        for i, (folder_path, size) in enumerate(largest_folders, 1):
            print(f"{i}. {folder_path} - {format_size(size)}")
