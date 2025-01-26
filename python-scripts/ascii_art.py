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

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python ascii_art.py <text> [font]")
    print("Example: python ascii_art.py Hello block")
  else:
    input_text = sys.argv[1]
    font = sys.argv[2] if len(sys.argv) > 2 else "standard"
    result = generate_ascii_art(input_text, font)
    print(result)
