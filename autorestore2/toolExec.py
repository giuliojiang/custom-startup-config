import sys
import subprocess

# Executes a subprocess call (no shell)
# exit_code: The required exit code to consider the command to be successful
# dir: The working directory to be used
def exec_required(cmd, exit_code=0, dir=None):

    print(">>> {}".format(" ".join(cmd)))
    code = subprocess.call(cmd, cwd=dir)
    if code != exit_code:
        print("ERROR: Required exit code of [{}] is different from actual exit code [{}] when executing {}".format(exit_code, code, cmd))
        sys.exit(1)
