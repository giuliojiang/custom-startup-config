import os
import toolExec
import shutil

print("Setting up .bashrc")

currentDir = os.path.abspath(os.path.dirname(__file__))
sourcePath = os.path.join(currentDir, 'data', 'bashrc')

homeDir = os.path.abspath(os.path.expanduser("~"))

bashrcPath = os.path.join(homeDir, ".bashrc")

shutil.copyfile(sourcePath, bashrcPath)

# Setup home/.bin directory

binSourceDir = os.path.join(currentDir, 'data', 'bin')
binDestDir = os.path.join(homeDir, 'bin')

if not os.path.exists(binDestDir):
    os.mkdir(binDestDir)

sourceFilesList = os.listdir(binSourceDir)
for sourceFilePath in sourceFilesList:
    sourceFileFullPath = os.path.join(binSourceDir, sourceFilePath)
    destFileFullPath = os.path.join(binDestDir, sourceFilePath)
    print("Copying {} to {}".format(sourceFileFullPath, destFileFullPath))
    shutil.copyfile(sourceFileFullPath, destFileFullPath)
    toolExec.exec_required([
        'chmod',
        '+x',
        destFileFullPath
    ])