#! /bin/bash
echo "Ping keepalive silent started"
ping -v -O -D -i 1 192.168.1.1 > /dev/null
