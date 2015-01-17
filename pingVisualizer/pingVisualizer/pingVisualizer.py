# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
This script visualizes pings to a host,
via braille signs
"""
import subprocess
import os
import time
from braillegraph import horizontal_graph
import re
import sys

version = "0.1"


class pingVisualizer(object):
    def __init__(self, arguments=None):
        self.configDict = {
            'timeInterval': 2,
            'pingListLen': 50,
            'adress': '127.0.0.1',
            'maxHeightValue': 50,
            'pings': 200,
        }
        for argument in arguments:
            #Insert the arguments into the dict
            if arguments[argument] is not None:
                print(argument)
                self.configDict[argument] = arguments[argument]
        self.timeInterval = float(self.configDict['timeInterval'])
        self.pingListLen = self.configDict['pingListLen']
        self.adress = self.configDict['adress']
        self.maxHeightValue = self.configDict['maxHeightValue']
        self.pings = self.configDict['pings']
        self.platform = sys.platform

    def getPingTime(self):
        if 'linux' in self.platform:
            #If Linux
            from string import digits
            digits = digits + '.' + ','
            args = ['ping', self.adress, '-c 1']
            p = subprocess.Popen(args, stdout=subprocess.PIPE)
            out = str(p.stdout.read())
            match = re.search('(time=)(\d*\.\d*)', out)
            if match:
                return float(match.group(2))
            else:
                return 'No pingtime'

        elif 'win' in self.platform:
            #If Windows
            from string import digits
            digits = digits + '.' + ','
            args = ['ping', self.adress, '-n 1']
            p = subprocess.Popen(args, stdout=subprocess.PIPE)
            out = str(p.stdout.read())
            match = re.search('(time=)(\d*)', out)
            if match:
                return float(match.group(2))
            else:
                return 'No pingtime'

    def visualizeHorizontal(self):
        pingList = []
        for i in range(self.pings):
            pingList.append(self.getPingTime())
            if len(pingList) > self.pingListLen:
                #Limit the length of the list
                pingList.pop(0)
            #Clear screen
            os.system('clear')
            if len(pingList) > 1:
                #Only plot if there is more than 2 values
                maxValue = max(pingList)
                minValue = min(pingList)
                k = self.maxHeightValue / maxValue
                valuelist = [int(value * k) for value in pingList]
                print('{}'.format(horizontal_graph(valuelist)))
                print('Max: {} ms \nMin: {}\nActual: {} \nAdress: {}'.format(
                    maxValue, minValue, pingList[-1], self.adress))
            time.sleep(self.timeInterval)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="This is a pingvisualizer!"
        )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=version)
    parser.add_argument(
        'adress',
        help="Which adress to ping",
        action='store')
    parser.add_argument(
        '--timeinterval',
        '-t',
        action='store_const',
        help="How often to ping",
        dest="timeInterval",
        const=2)
    parser.add_argument(
        '--listlength',
        '-l',
        action='store_const',
        help="How long the plot will be",
        dest="pingListLen",
        const=50)
    parser.add_argument(
        '--height',
        '-H',
        action='store_const',
        help="How high the plot will be",
        dest="maxHeightValue",
        const=50)
    parser.add_argument(
        '--pings',
        '-p',
        action='store_const',
        help="How many times to ping",
        dest="pings",
        const=20)
    args = parser.parse_args()
    visualizer = pingVisualizer(vars(args))
    visualizer.visualizeHorizontal()
