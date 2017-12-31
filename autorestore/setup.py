#!/usr/bin/env python

import subprocess
import os
import time
import sys

# Helper functions ------------------------------------------------------------

# True iff the file contains [str_match] in any line
def file_contains_string(fpath, str_match):
    f = open(fpath, 'r')
    for line in f:
        if str_match in line:
            f.close()
            return True
    f.close()
    return False

# Replaces the line containing [matcher] with
# [replacement]
def file_replace_string(f_path, matcher, replacement):
    # Read input file and save to buffer
    f_file = open(f_path, 'r')
    out_lines = []
    for line in f_file:
        if line.endswith('\n'):
            a_line = line[:-1]
        else:
            a_line = line
        if matcher in a_line:
            out_lines.append(replacement)
        else:
            out_lines.append(a_line)
    f_file.close()

    # Write buffer
    f_file = open(f_path, 'w')
    for line in out_lines:
        f_file.write(line + '\n')
    f_file.close()

# Executes a subprocess call (no shell)
# exit_code: The required exit code to consider the command to be successful
# dir: The working directory to be used
def exec_required(cmd, exit_code=0, dir=None):
    saved_dir = os.path.abspath(os.getcwd())
    if dir is not None:
        os.chdir(dir)

    print(">>> {}".format(" ".join(cmd)))
    code = subprocess.call(cmd)
    if code != exit_code:
        print("ERROR: Required exit code of [{}] is different from actual exit code [{}] when executing {}".format(exit_code, code, cmd))
        sys.exit(1)

    os.chdir(saved_dir)

# Setup directories -----------------------------------------------------------

home_dir = os.path.abspath(os.path.expanduser("~"))
# custom-startup-config/autorestore
curr_dir = os.path.abspath(".")
git_dir = os.path.abspath(os.path.dirname(curr_dir));

# Setup xprofile --------------------------------------------------------------

print("Setting up xprofile...")

# Open the .xprofile
xprofile_file = open(os.path.abspath(os.path.join(home_dir, ".xprofile")), 'w')
xprofile_file.write("#! /bin/bash\n")
xprofile_file.write('screen -d -m "{}"\n'.format(os.path.abspath(os.path.join(git_dir, "xprofile", "start.sh"))))
xprofile_file.close()

# Make .xprofile executable
exec_required(["chmod", "+x", os.path.abspath(os.path.join(home_dir, ".xprofile"))])

# Setup CFQ elevator ----------------------------------------------------------

print("Setting up CFQ elevator")

grub_path = "/etc/default/grub"
if not file_contains_string(grub_path, "elevator=cfq"):
    file_replace_string(grub_path, "GRUB_CMDLINE_LINUX_DEFAULT", 'GRUB_CMDLINE_LINUX_DEFAULT="quiet splash elevator=cfq"')
    exec_required.call(["update-grub"])

# Setup fstab entries ---------------------------------------------------------

print("Setting up /etc/fstab")

fstab_path = "/etc/fstab"
if not file_contains_string(fstab_path, "/tmp"):
    fstab_file = open(fstab_path, 'a')
    fstab_file.write('\n')
    fstab_file.write("tmpfs   /tmp         tmpfs   rw,nodev,nosuid          0  0\n")
    fstab_file.close();

# Setup .bashrc ---------------------------------------------------------------

print("Setting up .bashrc")

bashrc_path = os.path.abspath(os.path.join(home_dir, ".bashrc"))
exec_required.call(["wget", "https://gist.githubusercontent.com/giuliojiang/0791395432526b5f6abad7f897d48d9a/raw/271a2dddc45ee97b1839f66cd5a6b4da922f7cd7/.bashrc", "-O", bashrc_path])

# Setup fonts -----------------------------------------------------------------

print("Setting up fonts")

fonts_dir = os.path.abspath(os.path.join(home_dir, ".fonts"))
exec_required.call(["mkdir", fonts_dir])
exec_required.call(["wget", "https://fonts.google.com/download?family=Roboto|Roboto%20Mono|Source%20Code%20Pro|PT%20Serif", "-O", "fonts.zip"], dir=fonts_dir)
exec_required.call(["unzip", "fonts.zip"], dir=fonts_dir)
exec_required.call(["fc-cache"], dir=fonts_dir)

# Setup .screenrc -------------------------------------------------------------

print("Setting up .screenrc")

screenrc_path = os.path.abspath(os.path.join(home_dir, ".screenrc"))
exec_required.call(["wget", "https://gist.githubusercontent.com/giuliojiang/0de93cc5c444676e770bec919eb8bccf/raw/b7741171ad345789c4a902803912f944841ab9fd/.screenrc", "-O", screenrc_path)

# Exit ------------------------------------------------------------------------

print("Setup complete. Please reboot your PC")
