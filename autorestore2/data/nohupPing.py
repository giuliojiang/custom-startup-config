#!/usr/bin/env python3

import os
import subprocess
import datetime
import time

LOGFILENAME = "/tmp/nohupping.log"

class Log():

    def __init__(self):
        self.logf = open(LOGFILENAME, 'w')

    def info(self, t):
        self.logf.write(
            "{}:{}\n".format(
                datetime.datetime.now(),
                t
            )
        )
        self.logf.flush()

def main():
    if os.path.exists(LOGFILENAME):
        return

    logger = Log()
    logger.info("nohupPing started")

    devnull = open(os.devnull, 'w')

    while True:
        time.sleep(0.9)
        logger.info("Running ping")
        subprocess.call([
            "ping",
            "-c",
            "10",
            "1.1.1.1"
        ], stdout=devnull)

main()