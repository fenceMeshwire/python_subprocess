#!/usr/bin/env python3

# Python 3.9.5

# 00_subprocess_basics.py

# Dependencies
import subprocess

result = subprocess.run(["whoami"], capture_output=True, text=True)
print(result.stdout)
