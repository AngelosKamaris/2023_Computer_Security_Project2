import subprocess
process = subprocess.Popen("python3 1/attack.py", shell=True)
process.wait()
process = subprocess.Popen("python3 2/attack2.py", shell=True)
process.wait()