import os
import sys
from PIL import Image

def convert_image(source_path, output_format):
  """
  Converts all images in the specified directory to the given format.
  
  Parameters:
  - source_path (str): Path to the folder containing images or a single image.
  - output_format (str): Desired output format (e.g., "JPEG", "PNG").
  """
  if not os.path.exists(source_path):
    print(f"Error: Path '{source_path}' does not exist.")
    return

  # Determine if the source_path is a file or a directory
  if not os.path.exists(source_path):
    files = [source_path]
    output_dir = os.path.dirname(source_path)  # Use the same directory as the source file
  # Else, source_path is a directory
  else:
    files = [os.path.join(source_path, f) for f in os.listdir(source_path)
              if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff')) and not f.startswith(".")]
    output_dir = os.path.join(source_path, "converted_images")
    os.makedirs(output_dir, exist_ok=True)

  if not files:
    print("No image files found to convert.")
    return

  for file_path in files:
    try:
      with Image.open(file_path) as img:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join(output_dir, f"{file_name}.{output_format.lower()}")
        img.convert("RGB").save(output_file, format=output_format.upper())
        print(f"Converted: {file_path} -> {output_file}")
    except Exception as e:
      print(f"Failed to convert {file_path}: {e}")
  
  # Handle output directory message for single files
  if os.path.abspath(output_dir) == os.getcwd():
    output_location = os.getcwd()
  else:
    output_location = f"'{os.path.abspath(output_dir)}'"
  print(f"Conversion completed! Output files are in: {output_location}.")


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("📌 Usage: python convert_img.py <source_path> <output_format>")
    print("Example 1: python convert_img.py ./images JPEG <- Convert ALL images in images/ dir")
    print("Example 2: python convert_img.py ./image.png BMP <- Convert single file")
    print("Example 3: python convert_img.py ./ PNG <- ALL images in current dir")
  else:
    source_path = sys.argv[1]
    output_format = sys.argv[2]
    convert_image(source_path, output_format)
