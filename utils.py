from datetime import datetime
import os

def log_action(action):
    file_path = os.path.join(os.getcwd(), "logs.txt")

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {action}\n")
