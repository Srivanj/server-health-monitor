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

print("Server monitoring script executed successfully")
print("Monitoring environment: Production")

check_cpu_usage()

print("CPU monitoring completed successfully")
print("CPU monitoring feature enabled")
