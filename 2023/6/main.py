import os
import sys
import math


class Solution:
    def toyRace(self, f) -> int:
        txt = ""
        for line in f:
            txt += line
        times, distances = self.parseDoc(txt)
        product = 1
        for i in range(len(times)):
            product *= self.waysBeatRecord(times[i], distances[i])
        return product

    def parseDoc(self, doc: str):
        lines = doc.split("\n")
        times = lines[0].split(":")[1].split(' ')
        distances = lines[1].split(":")[1].split(' ')

        times = list(filter(lambda s: s != '' and s != ' ', times))
        times = list(map(lambda s: int(''.join(filter(lambda i: i.isdigit(), s))), times))

        distances = list(filter(lambda s: s != '' and s != ' ', distances))
        distances = list(map(lambda s: int(''.join(filter(lambda i: i.isdigit(), s))), distances))

        return times, distances


    def waysBeatRecord(self, time: int, distanceToBeat: int):
        count = 0
        dist = 0
        for chargeTime in range(time):
            dist = chargeTime * (time - chargeTime)
            if dist > distanceToBeat:
                count += 1
        return count

if __name__ == '__main__':
    productNumberOfSol = -1
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
            productNumberOfSol = Solution().toyRace(f)
    print(productNumberOfSol)