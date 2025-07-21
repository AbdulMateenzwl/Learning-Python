import subprocess

# Run a simple shell command
result = subprocess.run(["echo", "Hello from subprocess!"], capture_output=True, text=True)
print("Output:", result.stdout)

# List files using `ls` or `dir` (cross-platform)
import os
cmd = ["dir"] if os.name == "nt" else ["ls"]
result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
print("Files:\n", result.stdout)
