#! /usr/bin/env python3
import os
import shutil
import toolExec

def main():
    homeDir = os.path.abspath(os.path.expanduser("~"))
    xProfilePath = os.path.join(homeDir, ".xprofile")

    currDir = os.path.abspath(os.path.dirname(__file__))
    sourceXProfile = os.path.join(currDir, "data", "customResolutionXprofile")

    shutil.copyfile(sourceXProfile, xProfilePath)

    toolExec.exec_required([
        "chmod",
        "+x",
        xProfilePath
    ])

main()