import os
import toolExec

print("Setting up fonts")

homeDir = os.path.abspath(os.path.expanduser("~"))

fontsDir = os.path.join(homeDir, ".fonts")

if not os.path.exists(fontsDir):
    os.mkdir(fontsDir)

toolExec.exec_required(["wget", "https://fonts.google.com/download?family=Roboto|Roboto%20Mono|Source%20Code%20Pro|PT%20Serif", "-O", "fonts.zip"], dir=fontsDir)

toolExec.exec_required(["unzip", "fonts.zip"], dir=fontsDir)

toolExec.exec_required(["fc-cache"], dir=fontsDir)