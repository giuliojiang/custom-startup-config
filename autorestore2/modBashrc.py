import os
import toolExec

print("Setting up .bashrc")

homeDir = os.path.abspath(os.path.expanduser("~"))

bashrcPath = os.path.join(homeDir, ".bashrc")
toolExec.exec_required(["wget", "https://gist.github.com/giuliojiang/0791395432526b5f6abad7f897d48d9a/raw/01c5eebf8df600cbafe8c17be6b5af7c9fbace89/.bashrc", "-O", bashrcPath])