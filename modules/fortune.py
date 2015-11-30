#!/usr/bin/env python
"""
rip.py - rest in peace
"""
import subprocess

def fortune(jenni, input):
    jenni.say(subprocess.check_output(['fortune', '-n', '60', '-s']).strip())
fortune.commands = ['fortune']
fortune.priority = 'low'

if __name__ == '__main__':
    print __doc__.strip()
