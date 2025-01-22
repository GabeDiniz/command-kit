import speedtest
import time
from datetime import datetime

def measure_speed():
  """
  Measure internet download and upload speed using the speedtest library.
  """
  try:
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e6  # Convert to Mbps
    upload_speed = st.upload() / 1e6  # Convert to Mbps
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
      "timestamp": timestamp,
      "download_speed": round(download_speed, 2),
      "upload_speed": round(upload_speed, 2)
    }
  except Exception as e:
    print(f"Error measuring speed: {e}")
    return None

if __name__ == "__main__":
  interval = int(input("Enter interval (in seconds) between speed tests (0 for one-time): "))
  while True:
    speed_data = measure_speed()
    if speed_data:
      print(f"{speed_data['timestamp']} - Download: {speed_data['download_speed']} Mbps | Upload: {speed_data['upload_speed']} Mbps")
    else:
      print("Failed to retrieve speed data.")

    if not interval:
      break
    print(f"Waiting {interval} seconds...\n")
    time.sleep(interval)
