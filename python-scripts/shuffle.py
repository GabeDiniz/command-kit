import os
import random
import ctypes

# Set your wallpaper folder path
WALLPAPER_DIR = r"C:\Users\gabri\Pictures\Saved Pictures"

def get_random_wallpaper():
  """Select a random image from the wallpaper directory."""
  if not os.path.exists(WALLPAPER_DIR):
    print(f"❌ Error: Folder '{WALLPAPER_DIR}' does not exist.")
    return None

  images = [f for f in os.listdir(WALLPAPER_DIR) if f.lower().endswith(('.jpg', '.png', '.bmp'))]

  if not images:
    print(f"❌ No images found in {WALLPAPER_DIR}.")
    return None

  return os.path.join(WALLPAPER_DIR, random.choice(images))

def set_wallpaper(image_path):
  """Set the selected image as the desktop wallpaper."""
  if image_path:
    print(f"🔄 Changing wallpaper to: {image_path}")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    print("✅ Wallpaper changed successfully!")

if __name__ == "__main__":
  wallpaper = get_random_wallpaper()
  set_wallpaper(wallpaper)
