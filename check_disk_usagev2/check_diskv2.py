# With this script we"ll check the next parameters:
#Check disk usage 
#Check CPU usage 
#Check RAM usage 

# First of all, we need to install psutil if we don't have it yet, with the command "pip install psutil"

import psutil

def check_disk_usage(path):
    usage = psutil.disk_usage(path)
    return usage.percent

def cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {usage}%")

def ram_usage():
    ram = psutil.virtual_memory()
    print(f"RAM usage: {ram.percent}%")
    print(f"RAM used (GB): {round(ram.used / 1e9, 2)}") #Converting bytes to GB	/ 1e9

def main():
    path = "/"
    usage = check_disk_usage(path)

    print(f"Disk usage at {usage:.2f}%")
    
    if usage > 80:
        print("⚠️ Warning: Disk usage is above 80%!")
    else:
        print("✅ Disk usage is within safe limits.")

    # Call CPU and RAM usage here
    cpu_usage()
    ram_usage()

if __name__ == "__main__":
    main()
