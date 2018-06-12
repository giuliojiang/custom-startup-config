import os

import toolExec

print("Setting up mouse acceleration")

xorgPath = "/etc/X11/xorg.conf.d"

if not os.path.exists(xorgPath):
    os.mkdir("/etc/X11/xorg.conf.d")

toolExec.exec_required([
    "wget",
    "-O",
    "/etc/X11/xorg.conf.d/50-mouse-acceleration.conf",
    "https://gist.github.com/giuliojiang/861a2ce18fb7584474451484a6146fd4/raw/63d0796bf508947d645f8825a3869842e16a69fe/50-mouse-acceleration.conf"
])