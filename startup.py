#!/usr/bin/env python

# WHAT THIS SCRIPT DOES
# 1 Disable mouse acceleration
# 2 Lower mouse speed to level 2

import subprocess
import time
import sys

MOUSE_XINPUT_NAME = "Xornet"

def run_command_shell_proc(cmd):
    print('>>> {}'.format(cmd))
    return subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)

def run_command_shell(cmd):
    the_process = run_command_shell_proc(cmd)
    the_process.wait()

# disable mouse acceleration
run_command_shell('xset m 0/1 4')

# retrieve list of devices
xinput_process = run_command_shell_proc('xinput list')
mouse_xinput_line = ''
while True:
    line = xinput_process.stdout.readline()
    if line != '':
        if MOUSE_XINPUT_NAME in line:
            mouse_xinput_line = line.rstrip()
    else:
        break
xinput_process.wait()

# guess the number of the mouse device
try:
    mouse_xinput_id = int(mouse_xinput_line.split("id=")[1].split('\t')[0])
except:
    print('Could not guess id of mouse from line:')
    print(mouse_xinput_line)
    sys.exit(1)

# set mouse speed
run_command_shell('xinput set-prop {} "Device Accel Constant Deceleration" 2'.format(mouse_xinput_id))
