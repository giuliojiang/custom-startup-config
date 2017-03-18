#!/usr/bin/env python

# WHAT THIS SCRIPT DOES
# 1 Disable mouse acceleration
# 2 Lower mouse speed to level 2

import subprocess
import time
import sys

MOUSE_XINPUT_NAME = ["Xornet", "Synaptics", "Naos"]

def run_command_shell_proc(cmd):
    print('>>> {}'.format(cmd))
    return subprocess.Popen(['/bin/bash', '-c', cmd], stdout=subprocess.PIPE)

def run_command_shell(cmd):
    the_process = run_command_shell_proc(cmd)
    the_process.wait()

def any_contains(matches, candidate):
    for match in matches:
        if match in candidate:
            return True
    return False

# disable mouse acceleration
run_command_shell('xset m 0/1 4')

# retrieve list of devices
xinput_process = run_command_shell_proc('xinput list')
mouse_xinput_lines = []
while True:
    line = xinput_process.stdout.readline()
    if line != '':
        if any_contains(MOUSE_XINPUT_NAME, line):
            mouse_xinput_lines.append(line.rstrip())
    else:
        break
xinput_process.wait()

# guess the number of the mouse device
mouse_xinput_ids = []
for mouse_line in mouse_xinput_lines:
    try:
        mouse_xinput_id = int(mouse_line.split("id=")[1].split('\t')[0])
        mouse_xinput_ids.append(mouse_xinput_id)
    except:
        print('Could not guess id of mouse from line:')
        print(mouse_line)

# set mouse speed
for mouse_id in mouse_xinput_ids:
    run_command_shell('xinput set-prop {} "Device Accel Constant Deceleration" 2'.format(mouse_id))
