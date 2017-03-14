#! /bin/bash
xrandr --newmode "2560x1440_60.00" 311.83 2560 2744 3024 3488 1440 1441 1444 1490 -HSync +Vsync
xrandr --addmode DisplayPort-0 "2560x1440_60.00"
xrandr --output DisplayPort-0 --mode "2560x1440_60.00"
