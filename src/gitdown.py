#!/usr/bin/env python3

import subprocess
from time import sleep

def pull():
    return subprocess.call(["git", "pull"]) == 0

def main(interval):
    while 1:
        pull()
        sleep(interval)

if __name__ == '__main__':
    main()
