import os
import sys

targetLine = 'gj - rtprio 99'
limitsConfPath = '/etc/security/limits.conf'

def lineAlreadyExists():
    with open(limitsConfPath, 'r') as limitsConfFile:
        for line in limitsConfFile:
            if line.strip() == targetLine:
                return True
        return False
            
def main():
    if lineAlreadyExists():
        print("Line already exists")
        sys.exit(0)
    else:
        limitsConfFile = open(limitsConfPath, 'a')
        limitsConfFile.write('\n{}\n'.format(targetLine))
        limitsConfFile.close()
        print("done.")

main()