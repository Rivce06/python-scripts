import subprocess

def check_disk_usage():
    print("📦 Disk usage:\n")
    result = subprocess.run(["df", "-h"], capture_output=True, text=True)
    print(result.stdout)

def find_largest_dirs(path="/", count=5):
    print(f"\n📂 Top {count} largest folders in {path}:\n")
    command = f"du -h {path} 2>/dev/null | sort -hr | head -n {count}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main():
    check_disk_usage()
    find_largest_dirs("/var", 5)  # You can change this path to "/" or "/home"

if __name__ == "__main__":
    main()
