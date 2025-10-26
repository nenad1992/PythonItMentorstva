# Total CPU Usage:
# Number of Physical Cores:
# Number of Logical Cores:
# Number of Threads in Current Process:
import os
import psutil

cpu_usage = psutil.cpu_percent(interval=1)
num_phy_cores = psutil.cpu_count(logical=False)
num_log_cores = psutil.cpu_count(logical=True)
current_process = psutil.Process(os.getpid())
num_threads = current_process.num_threads()

print(f"Total CPU Usage: {cpu_usage}%")
print(f"Number of Physical Cores: {num_phy_cores}")
print(f"Number of Logical Cores: {num_log_cores}")
print(f"Number of Threads in Current Process: {num_threads}")