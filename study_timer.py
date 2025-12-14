import time

modes = {
    "short": 25,
    "long": 50,
    "break": 10
}

def countdown(minutes):
    total_seconds = minutes * 60

    try:
        while total_seconds > 0:
            mins = total_seconds // 60
            secs = total_seconds % 60
            print(f"{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            total_seconds -= 1

        print("\n⏰ Time's up! Great work.")

    except KeyboardInterrupt:
        print("\n⛔ Timer stopped early by user.")

def main():
    print("📚 Study Focus Timer")
    print("Available modes:")
    for mode, mins in modes.items():
        print(f"- {mode} ({mins} min)")

    choice = input("Choose mode: ").strip().lower()

    if choice not in modes:
        print("Invalid choice.")
        return

    print(f"Starting {choice} session for {modes[choice]} minutes.")
    print("Press Ctrl + C anytime to stop.\n")
    countdown(modes[choice])

if __name__ == "__main__":
    main()
