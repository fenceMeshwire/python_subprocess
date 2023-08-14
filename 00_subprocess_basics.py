#!/usr/bin/env python3

# Python 3.9.5

# 00_subprocess_basics.py

# Dependencies
import os

result = os.popen('whoami')
stdout = result.read()
print(stdout)
