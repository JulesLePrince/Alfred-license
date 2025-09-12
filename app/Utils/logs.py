import datetime

def write_log(message, filename="log.txt"):
    # Open file in append mode, create if it doesn't exist
    with open(filename, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

