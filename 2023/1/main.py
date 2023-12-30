import os
import sys

class Solution:
    def trebuchet(self, document: str) -> int:
        return sum([self.getVal(lines) for lines in document.split("\n")])
    
    def getVal(self, lines: str) -> int:
        digits = ''.join(filter(lambda i: i.isdigit(), lines))
        print(digits)
        return int(digits[0]) * 10 + int(digits[-1])

if __name__ == '__main__':
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        sumDoc = 0
        for line in f:
            sumDoc += Solution().getVal(line)
    print(sumDoc)