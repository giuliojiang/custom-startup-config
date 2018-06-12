import toolExec

print("Setting up git global configs")

# git config --global core.askPass ""
toolExec.exec_required([
    "git",
    "config",
    "--global",
    "core.askPass",
    ""
])

# git config --global core.editor "nano"
toolExec.exec_required([
    "git",
    "config",
    "--global",
    "core.editor",
    "nano"
])