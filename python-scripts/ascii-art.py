import sys
from art import text2art
from art import FONT_NAMES # print(FONT_NAMES)

def generate_ascii_art(input_text: str, font="standard"):
  """
  Generate ASCII art for the given text using the specified font.
  
  Parameters:
  - input_text (str): The text to convert to ASCII art.
  - font (str): The font style to use (default is "standard").
  """
  try:
    ascii_art = text2art(input_text, font=font)
    return ascii_art
  except Exception as e:
    return f"Error generating ASCII art: {e}"

def get_valid_input(prompt, allow_blank=False):
  """
  Continuously prompts the user until valid input is provided.
  
  Parameters:
  - prompt (str): The message to display to the user.
  - allow_blank (bool): Whether to allow blank input (defaults to False).
  """
  while True:
    user_input = input(prompt).strip()
    if allow_blank and not user_input:
      return "standard"  # Default font if left blank
    if user_input:
      return user_input
    print("Input cannot be empty. Please try again.")

if __name__ == "__main__":
  # List available fonts
  if "--list-fonts" in sys.argv:
    print("Available fonts:")
    print(", ".join(FONT_NAMES))
    sys.exit(0)

  print("Hint! To get the available fonts, run: ascii-art --list-fonts")
  if len(sys.argv) < 2:
    input_text = get_valid_input("Please enter the text you would like to convert: ")
    font = get_valid_input("Please enter the Font style (leave blank for 'standard'): ", allow_blank=True)

    if font not in FONT_NAMES:
      print(f"Font '{font}' is not valid. Defaulting to 'standard'.")
      font = "standard"
  else:
    input_text = sys.argv[1]
    font = sys.argv[2] if len(sys.argv) > 2 else "standard"
  result = generate_ascii_art(input_text, font)
  print(result)
