import argparse
import sys
import requests

# API Endpoint
API_URL = "http://ip-api.com/json"

def lookup_ip(ip=""):
  """
  Fetches geolocation data for the provided IP address.
  If no IP is provided, it looks up the user's own IP.
  
  Parameters:
  - ip-address (str): The IP address that will be geolocated.
  """
  url = f"{API_URL}/{ip}"
  response = requests.get(url)
  
  if response.status_code != 200:
    print("❌ Error: Unable to reach the API.")
    return

  data = response.json()
  
  if data.get("status") == "fail":
    print(f"❌ Error: {data.get('message', 'Invalid IP address')}")
    return

  print("\n🌍 IP Geolocation")
  print("=" * 60)
  print(f"📍 Country      : {data.get('country', 'N/A')}")
  print(f"🌆  City        : {data.get('city', 'N/A')}")
  print(f"📡 ISP         : {data.get('isp', 'N/A')}")
  print(f"🗺  Latitude   : {data.get('lat', 'N/A')}")
  print(f"🗺  Longitude  : {data.get('lon', 'N/A')}")
  print("=" * 60)

if __name__ == "__main__":
  # Set up argument parsing
  parser = argparse.ArgumentParser(
    description="Find IP location.",
    usage="ip-lookup <ip-address>"
  )
  parser.add_argument("ip-address", type=str, help="The IP address to be geolocated.")
    
  # If no arguments are passed, print help and exit
  if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

    # Parse the arguments
    args = parser.parse_args()

  ip = sys.argv[1] if len(sys.argv) > 1 else ""
  lookup_ip(ip)
