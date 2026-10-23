import datetime
import psutil

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)

    print(f"Current CPU usage: {cpu_usage}%")

    if cpu_usage > 80:
        print("WARNING: High CPU usage detected!")
    else:
        print("CPU usage is within the expected range.")

print("Server health monitoring started")
print(f"Monitoring check time: {datetime.datetime.now()}")

check_cpu_usage()

print("Server monitoring script executed successfully")
