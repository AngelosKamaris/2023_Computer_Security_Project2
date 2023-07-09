import subprocess

process = subprocess.Popen("python3 1/attack.py", shell=True)
process.wait()
process = subprocess.Popen("python3 2/attack.py", shell=True)
process.wait()

# process = subprocess.Popen("python3 3/attack3.py", shell=True)
# process.wait()
# process = subprocess.Popen("python3 4/attack4.py", shell=True)
# process.wait()