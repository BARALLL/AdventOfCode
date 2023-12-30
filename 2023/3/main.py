import os
import sys

class Solution:    
    def sumPartNumberEngineSchematic(self, text: str) -> int:
        sumAdjacentNumbers = 0
        startIndexNum = -1
        endIndexNum = -1

        lineIndex = 0
        lines = text.split('\n')
        for line in lines:
            for charIndex in range(len(line)):
                if line[charIndex] >= '0' and line[charIndex] <= '9':
                    if startIndexNum == -1:
                        startIndexNum = charIndex
                        endIndexNum = charIndex
                    else:
                        endIndexNum += 1
                if line[charIndex] == '.':
                    if startIndexNum != -1:
                        isAdjacent = self.adjency(lines, startIndexNum, endIndexNum, lineIndex)
                        if(isAdjacent):
                            sumAdjacentNumbers += int(line[startIndexNum:endIndexNum+1])
                        startIndexNum = -1
                        endIndexNum = -1
            lineIndex += 1
        return sumAdjacentNumbers
    
    def adjency(self, text: str, startY: int, endY: int, numX: int):
        for x in range(numX-1, numX+1 + 1):
            if x >= 0 and x < len(text):
                for y in range(startY-1, endY+1 + 1):
                    if y >= 0 and y < len(text[x]):
                        if text[x][y] != '.' and not (text[x][y] >= '0' and text[x][y] <= '9'):
                            return True
        return False


if __name__ == '__main__':
    os.chdir(sys.path[0])
    text = ""
    with open("input.txt", "r") as f:
        for lines in f:
            text += lines
    sumAdjacentNumbers = Solution().sumPartNumberEngineSchematic(text)
    print(sumAdjacentNumbers)