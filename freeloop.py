#! /usr/bin/env python3

import subprocess
import time

while True:
  print()
  print()
  subprocess.run(['free', '-h'])
  time.sleep(2)
