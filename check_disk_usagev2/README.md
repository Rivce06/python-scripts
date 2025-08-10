# 🧠 Disk Usage Checker in Python

This is a lightweight Python script that checks the disk usage of a directory (default is `/`) and prints a warning if the usage exceeds 80%.

---

## 📌 When to Use This Script

- To monitor disk usage on Linux/macOS/Windows
- As part of an automated health check or cron job
- While learning how to interact with system-level disk information in Python

---

## 📂 Project Structure

---

## 🧠 What the Script Does (Line-by-Line Explanation)

### 1. Importing required module

```python
import shutil
```
-shutil is a standard Python module for high-level file and disk operations.

-We use it here to access shutil.disk_usage(path) — a method that retrieves disk statistics (total, used, free). 

### 2. Defining the disk usage check function

```python
def check_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return (used / total) * 100

```
* shutil.disk_usage(path) returns a tuple:

* total: Total disk space in bytes

* used: Used disk space in bytes

* free: Free disk space in bytes

-We calculate the percentage of disk used using (used / total) * 100.


### 3. Main logic

```python
def main():
    path = "/"  # Change this to "C:\\" on Windows
    usage = check_disk_usage(path)
```
-Sets the path to /, which is the root directory on Unix-like systems.

-Calls the function to calculate disk usage.

### 4. Printing results and checking limits

    print(f"Disk usage at {usage:.2f}%")

    if usage > 80:
        print("⚠️ Warning: Disk usage is above 80%!")
    else:
        print("✅ Disk usage is within safe limits.")
-Displays the usage value with two decimal places.

-If the usage is above 80%, it prints a warning. Otherwise, everything is okay.

### 5. Script entry point

```python
if __name__ == "__main__":
    main()
```
-This ensures the script only runs when executed directly (not when imported).

-It's standard practice in Python scripts to allow reuse of code without executing it on import.

## 🧑‍💻 Customization
-You can change the path in the script to check a different drive:
```python
Linux: /home, /var, etc.
```
```python
Windows: C:\\, D:\\, etc.
```
```python
path = "C:\\"