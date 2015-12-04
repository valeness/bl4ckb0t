#!/usr/bin/env python
"""
feature.py - For making feature requests on the bot, appends to file
"""

def feature(jenni, input):
    with open("feature_requests.txt", "a") as f:
        feature = input.replace('.feature ', '')
        f.write(feature + "\n")
    jenni.say('Request added')

feature.commands = ['feature']
feature.priority = 'low'

if __name__ == '__main__':
    print __doc__.strip()
