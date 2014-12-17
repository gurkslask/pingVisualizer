import subprocess
import os
import time
from braillegraph import horizontal_graph


class pingVisualizer(object):
    def __init__(self, **kwargs):
        self.configDict = {
            'timeInterval': 2,
            'pingListLen': 50,
            'adress': '127.0.0.1',
            'maxHeightValue': 50,
            'pings': 200
        }
        self.configDict.update(kwargs)
        self.timeInterval = self.configDict['timeInterval']
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
        outlist = out.split('\\n')
        outlist = outlist[1].split('=')
        pingtime = outlist[-1].split(' d')[0]
        pingtime = float(
            ''.join(number for number in pingtime if number in digits))
        return pingtime

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
    visualizer = pingVisualizer(maxHeightValue=100)
    visualizer.visualizeHorizontal()
