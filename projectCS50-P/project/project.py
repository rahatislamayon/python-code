import csv
from datetime import date


FILE = "study_log.csv"


def main():
    while True:
        print("\nStudy Time Tracker")
        print("1. Log study session")
        print("2. View total study time")
        print("3. View today's summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            subject = input("Subject: ").strip()
            minutes = int(input("Minutes studied: "))
            log_session(subject, minutes)

        elif choice == "2":
            total = get_total_minutes()
            print(f"Total study time: {total} minutes")

        elif choice == "3":
            today = date.today().isoformat()
            total = get_daily_minutes(today)
            print(f"Today's study time: {total} minutes")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def log_session(subject, minutes):
    if minutes <= 0:
        raise ValueError

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date.today().isoformat(), subject, minutes])


def get_total_minutes():
    total = 0
    try:
        with open(FILE) as f:
            reader = csv.reader(f)
            for _, _, minutes in reader:
                total += int(minutes)
    except FileNotFoundError:
        pass
    return total


def get_daily_minutes(day):
    total = 0
    try:
        with open(FILE) as f:
            reader = csv.reader(f)
            for d, _, minutes in reader:
                if d == day:
                    total += int(minutes)
    except FileNotFoundError:
        pass
    return total


if __name__ == "__main__":
    main()

