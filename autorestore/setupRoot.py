#!/usr/bin/env python

import subprocess
import os
import time
import sys
import argparse
import shutil

parser = argparse.ArgumentParser()

args = parser.parse_args()

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

# Setup CFQ elevator ----------------------------------------------------------

print("Setting up CFQ elevator")

grub_path = "/etc/default/grub"
if not file_contains_string(grub_path, "elevator=cfq"):
    file_replace_string(grub_path, "GRUB_CMDLINE_LINUX_DEFAULT", 'GRUB_CMDLINE_LINUX_DEFAULT="quiet splash elevator=cfq"')
    exec_required(["update-grub"])

# Setup fstab entries ---------------------------------------------------------

print("Setting up /etc/fstab")

fstab_path = "/etc/fstab"
if not file_contains_string(fstab_path, "/tmp"):
    fstab_file = open(fstab_path, 'a')
    fstab_file.write('\n')
    fstab_file.write("tmpfs   /tmp         tmpfs   rw,nodev,nosuid          0  0\n")
    fstab_file.close();

# Setup mouse acceleration ----------------------------------------------------

print("Setting up mouse acceleration")

os.mkdir("/etc/X11/xorg.conf.d")

exec_required([
    "wget",
    "-O",
    "/etc/X11/xorg.conf.d/50-mouse-acceleration.conf",
    "https://gist.github.com/giuliojiang/861a2ce18fb7584474451484a6146fd4/raw/63d0796bf508947d645f8825a3869842e16a69fe/50-mouse-acceleration.conf"
])

# Exit ------------------------------------------------------------------------

print("Setup complete. Please reboot your PC")
