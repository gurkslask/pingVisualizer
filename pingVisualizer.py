#!/usr/bin/python3
import subprocess
import os
import time
from braillegraph import horizontal_graph

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
        if arguments is not None: self.configDict.update(arguments)
        self.timeInterval = float(self.configDict['timeInterval'])
        self.pingListLen = self.configDict['pingListLen']
        self.adress = self.configDict['adress']
        self.maxHeightValue = self.configDict['maxHeightValue']
        self.pings = self.configDict['pings']

    def getPingTime(self):
        from string import digits
        digits = digits + '.' + ','
        args = ['ping', self.adress, '-c 1']
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        out = str(p.stdout.read())
        return float(out[out.find('time=')+5:out.find(' ms')])

    def visualizeHorizontal(self):
        minLengthValue = 0
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
                print('max: {} ms \nmin: {}\nactual: {}'.format(
                    maxValue, minValue, pingList[-1]))
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
        action='store',
        help="How often to ping",
        dest="timeInterval")
    parser.add_argument(
        '--listlength',
        '-l',
        action='store',
        help="How long the plot will be",
        dest="pingListLen")
    parser.add_argument(
        '--height',
        '-H',
        action='store',
        help="How hig the plot will be",
        dest="maxHeightValue")
    parser.add_argument(
        '--pings',
        '-p',
        action='store',
        help="How hig many times to ping",
        dest="pings")
    args = parser.parse_args()
    visualizer = pingVisualizer(vars(args))
    visualizer.visualizeHorizontal()
