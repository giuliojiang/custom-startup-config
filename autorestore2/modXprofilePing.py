import os
import stat

print("Setting up xprofile...")

# Create xprofile_aux.sh
homeDir = os.path.abspath(os.path.expanduser("~"))
auxPath = os.path.join(homeDir, "xprofile_aux.sh")
auxFile = open(auxPath, 'w')
auxFile.write("#! /bin/bash\n")
auxFile.write("ping -v -O -D -i 1 192.168.1.1\n")
auxFile.close()
os.chmod(auxPath, 0o711) # Others have execute permission

# Create .xprofile
xprofilePath = os.path.join(homeDir, ".xprofile")
xprofileFile = open(xprofilePath, 'w')
xprofileFile.write("#! /bin/bash\n")
xprofileFile.write('screen -d -m "{}"\n'.format(auxPath))
xprofileFile.close()
os.chmod(xprofilePath, 0o711) # Others have execute permission