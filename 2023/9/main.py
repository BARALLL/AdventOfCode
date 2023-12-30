import os
import sys
import math


class Solution:
    def OasisSensor(self, line) -> int:
        sequences = self.createSequences(line)
        return self.sequencesFillingBottomUp(sequences)

    def createSequences(self, line: str):
        sequences = list(list())
        digits = line.split(' ')
        wtd = list(filter(lambda s: str([c.isdigit() for c in s]), digits))
        sequences.append(list(map(lambda x: int(x), wtd)))
        allZeros = False
        sequenceID = 1
        while not allZeros:
            allZeros = True
            sequences.append([])
            for i in range(1, len(sequences[sequenceID - 1])):
                sequences[sequenceID].append(sequences[sequenceID - 1][i] - sequences[sequenceID - 1][i - 1])
                if sequences[-1][-1] != 0:
                    allZeros = False
            sequenceID += 1
        return sequences

    def sequencesFillingBottomUp(self, sequences):
        sequences[-1].append(0)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
        return sequences[0][-1]



if __name__ == '__main__':
    nextVal = 0
    sumVal = 0
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            nextVal = Solution().OasisSensor(line)
            sumVal += nextVal
            print(nextVal)
    print(sumVal)