import json

def get_json_length(filename):
    """
    Reads a JSON file and returns the number of top-level elements.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return len(data)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

if __name__ == "__main__":
    filename = input("Enter the JSON file name: ")
    length = get_json_length(filename)

    if length is not None:
        print(f"The JSON file '{filename}' contains {length} top-level elements.")
