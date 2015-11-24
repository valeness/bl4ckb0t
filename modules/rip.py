#!/usr/bin/env python
"""
rip.py - rest in peace
"""

def rip(jenni, input):
    jenni.say('http://rip.timeshifter.xyz/')
rip.commands = ['rip']
rip.priority = 'low'

if __name__ == '__main__':
    print __doc__.strip()
