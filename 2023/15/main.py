import os
import sys
from typing import List
from collections import defaultdict

class Solution:
    
    # part 1
    def getSumHashAlgo(self, steps) -> int:
        sumHashAlgo = 0
        steps = steps.split(",")
        for step in steps:
            sumHashAlgo += self.HASH(step)
        return sumHashAlgo

    def HASH(self, s: str):
        current = 0
        for i in range(len(s)):
            current = ((current + ord(s[i])) * 17) % 256
        return current 


    # part 2
    def getFocusingPowerLensConfiguration(self, steps):
        boxes = [[] for _ in range(256)]
        focalLengths = {}
        labels = defaultdict(dict)
        steps = steps.split(",")
        for step in steps:
            if "=" in step:
                label, focalLength = step.split("=")
                focalLengths[label] = focalLength
                boxID = self.HASH(label)
                if label in boxes[boxID]:
                    labelIndex = boxes[boxID].index(label)
                    boxes[boxID][labelIndex] = label
                else:
                    boxes[boxID].append(label)
            
            elif "-" in step:
                label = step[:-1]
                boxID = self.HASH(label)
                if label in boxes[boxID]:
                    boxes[boxID].remove(label)


        focusingPower = 0
        for i in range(len(boxes)):
            for j in range(len(boxes[i])):
                focusingPower += (i + 1) * (j + 1) * int(focalLengths[boxes[i][j]]) 
        return focusingPower





if __name__ == '__main__':
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line

    # part 1
    sumHashAlgo = Solution().getSumHashAlgo(txt)
    print(sumHashAlgo)

    # part 2
    focusingPower = Solution().getFocusingPowerLensConfiguration(txt)
    print(focusingPower)