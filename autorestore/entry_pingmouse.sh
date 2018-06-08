sudo apt update && \
    sudo apt-get -y install git && \
    cd && \
    mkdir git ; \
    cd git && \
    rm -rf custom-startup-config-bak ; \
    mv custom-startup-config custom-startup-config-bak ; \
    git clone https://github.com/giuliojiang/custom-startup-config --depth 1 && \
    cd custom-startup-config && \
    cd autorestore && \
    sudo ./install.sh && \
    sudo ./setup.py --pingmouse