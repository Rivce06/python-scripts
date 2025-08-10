"""
Disk Usage Checker

Checks the disk usage of a specified path and warns if usage exceeds 80%.
"""

import shutil

def check_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return (used / total) * 100

def main():
    path = "/"  # Change this to another directory if needed
    usage = check_disk_usage(path)

    print(f"Disk usage at {usage:.2f}%")

    if usage > 80:
        print("⚠️ Warning: Disk usage is above 80%!")
    else:
        print("✅ Disk usage is within safe limits.")

if __name__ == "__main__":
    main()