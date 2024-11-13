import time
import argparse
import sys
from playsound import playsound

def countdown_timer(minutes, alert_sound="../python-scripts/alarm.mp3"):
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

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Start a timer.",
        usage="timer.py <time_in_minutes>"
    )
    parser.add_argument("time_in_minutes", type=float, help="The number of minutes the timer should run for")
    
    # If no arguments are passed, print help and exit
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the move_project function with the provided arguments
    countdown_timer(args.time_in_minutes)


if __name__ == "__main__":
    main()