all:
    sudo ./modOpensuseInstalls.sh
	sudo python3 modMouseAccel.py
	python3 modScreenrc.py
	python3 modBashrc.py
	python3 modFonts.py
	python3 modGit.py