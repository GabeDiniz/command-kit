import time
from playsound import playsound

def countdown_timer(minutes, alert_sound="alarm.mp3"):
    """
    Starts a countdown timer for the given number of minutes with a sound alert at the end.
    
    Parameters:
    - minutes: Number of minutes for the countdown
    - alert_sound: Path to the sound file to play when the timer finishes
    """
    total_seconds = int(minutes * 60)  # Convert to integer total seconds

    try:
        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            mins = int(mins)  # Ensure mins is an integer
            secs = int(secs)  # Ensure secs is an integer
            timer = f'{mins:02d}:{secs:02d}'
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1

        print("Time's up! 🚀")
        playsound(alert_sound)

    except KeyboardInterrupt:
        print("\nTimer interrupted.")

# Usage Example
countdown_timer(0.02, "alarm.mp3")
