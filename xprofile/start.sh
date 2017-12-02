#!/usr/bin/env python

import subprocess
import os
import time

def run(cmd):
    subprocess.Popen(cmd)

# wait a little bit
time.sleep(2)

# custom-startup-config/xprofile
exec_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

# custom-startup-config/
root_dir = os.path.abspath(os.path.dirname(exec_dir))

# custom-startup-config/pingKeepAlive
ping_dir = os.path.abspath(os.path.join(root_dir, "pingKeepAlive"))

# custom-startup-config/mouseAcceleration
mouse_dir = os.path.abspath(os.path.join(root_dir, "mouseAcceleration"))

# Execute
run([os.path.abspath(os.path.join(ping_dir, "ping-keepalive.sh"))])
run([os.path.abspath(os.path.join(mouse_dir, "startup.py"))])

while True:
    time.sleep(100)
