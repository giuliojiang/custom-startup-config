import os
import toolExec

print("Setting up .screenrc")

homeDir = os.path.abspath(os.path.expanduser("~"))

screenrcPath = os.path.join(homeDir, ".screenrc")
toolExec.exec_required(["wget", "https://gist.githubusercontent.com/giuliojiang/0de93cc5c444676e770bec919eb8bccf/raw/b7741171ad345789c4a902803912f944841ab9fd/.screenrc", "-O", screenrcPath])