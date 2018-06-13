import os
import shutil

print("Setting up nohup ping...")

thisDir = os.path.abspath(os.path.dirname(__file__))
homeDir = os.path.abspath(os.path.expanduser("~"))

# Copy the aux file
auxSourcePath = os.path.join(thisDir, "data", "nohupPing.py")
auxDestPath = os.path.join(homeDir, "nohupPing.py")
shutil.copy(auxSourcePath, auxDestPath)

# Append to .profile

# Check that it's not already in
targetString = "\nnohup {} &\n".format(auxDestPath)
targetStringStripped = targetString.strip()
alreadyWritten = False
profilePath = os.path.join(homeDir, ".profile")
profileFile = open(profilePath, 'r')
for line in profileFile:
    line = line.strip()
    if targetStringStripped == line:
        print("Already written")
        alreadyWritten = True
profileFile.close()

if not alreadyWritten:
    profileFile = open(profilePath, 'a')
    profileFile.write(targetString)
    profileFile.close()
