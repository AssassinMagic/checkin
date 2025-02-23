import datetime

def log_user(user):
    try:
        with open("log/attendance.txt", "w") as f:
            f.write(f"{datetime.datetime.now()}: {user}\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

    