# 📦Disk Usage and Folder Size Analyzer (Linux/macOS)

This Python script helps you **monitor disk usage** and **identify the largest directories** on a Linux or macOS system using shell utilities like `df` and `du`.

For example, if we have a situation where one of our servers or devices are almos out of space, this a way in how we can clean it up.

we need to:
 1. Check disk usage
 2. Identify which directories or files are using the most space.
 3. Decide what can be deleted or compresed

---

## 📌 When to Use This Script

- To quickly check disk usage in a human-readable format
- To identify which directories are taking up the most space
- During troubleshooting low-disk-space issues

---

## 🧱 Requirements

This script runs only on **Linux/macOS systems**, as it uses Unix shell commands:
- `df` – to check disk space
- `du` – to analyze directory sizes
- `sort`, `head`, and shell piping

It **won’t work on Windows** without modifications.

---


## 🧠 What the Script Does (Line-by-Line)



### 1. Import the subprocess module

```python
import subprocess
```
The subprocess module is used to run shell commands directly from Python.

This allows us to use Linux utilities like df and du.

### 2. Define `check_disk_usage()` function

```python
def check_disk_usage():
    print("📦 Disk usage:\n")
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    print(result.stdout)
```
Runs the command: `df` `-h`

* `-h` stands for "human-readable" (displays sizes in MB, GB, etc.)

* Captures the output and prints it.

Useful to quickly view the usage of all mounted filesystems.

### 3. Define `find_largest_dirs()` function

```python
def find_largest_dirs(path="/", count=5):
    print(f"\n📂 Top {count} largest folders in {path}:\n")
    command = f"du -h {path} 2>/dev/null | sort -hr | head -n {count}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
```
**Finds the largest folders inside a given path.**

The command used:


 ```python
 du -h /path | sort -hr | head -n {count}
 ```

* `du -h`: shows folder sizes

* `2>/dev/null`: ignores permission errors

* `sort -hr`: sorts by size (largest first)

* `head -n {count}`: shows only the top 5

The path defaults to `/` but can be changed.

### 4. Main function to run both checks

```python
def main():
    check_disk_usage()
    find_largest_dirs("/var", 5)

```
* First prints overall disk usage

* Then prints the **largest 5 directories** inside `/var`

* You can **change** "`/var`" to "`/`", "`/home`", or any other directory

### 5. Script entry point

```python
if __name__ == "__main__":
    main()
```

**Ensures the script only runs when executed directly.**

Standard Python best practice.

🔧 **Example Output**

```bash
📦 Disk usage:

Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   30G   20G  60% /

📂 Top 5 largest folders in /var:

2.1G    /var/log
1.5G    /var/cache
900M    /var/lib
400M    /var/tmp
300M    /var/backups
```

🧑‍💻 Customization
Change the path or number of results:

`find_largest_dirs("/home", 10)`

-You can even wrap this script in a loop or schedule it with cron to monitor disk usage over time.

**🚫 Limitations**

* Only works on Unix-based systems (Linux/macOS).

* Requires permission to run `du` and `df` in the specified directories.

* For very large filesystems, it may take time to compute folder sizes.