#!/usr/bin/env python3

import sys
import os
import subprocess
from time import sleep

def git(*args, **kwargs):
    method = kwargs.get('method') or 'call'
    
    args = list(args)
    args.insert(0, 'git')
    return getattr(subprocess, method)(args)

def has_local_changes():
    return git("status", "--porcelain", method="check_output")

def commit():
    return git("add", "--all", ".") == 0 and \
        git("commit", "-a", "-m", "Auto-commit by gitsync") == 0

def push():
    return git("push") == 0

def main(interval):
    while 1:
        if has_local_changes():
            if commit() and push():
                print("Pushed to remote git")
            else:
                print("Could not commit & push")
        
        sleep(interval)

if __name__ == '__main__':
    main(60)
