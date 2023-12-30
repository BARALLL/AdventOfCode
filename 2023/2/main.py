import os
import sys

class Solution:
    def cubeConundrum(self, document: str) -> int:
        return sum([self.isGameValid(lines) for lines in document.split("\n")])
    
    def isGameValid(self, lines: str) -> int:
        cubesNumber = [0] * 3   #r, g, b
        parts = lines.split(":")
        gameID = int(''.join(filter(lambda i: i.isdigit(), parts[0])))

        cubes = parts[1].replace(';',',').split(",")
        
        for cube in cubes:
            val = int(''.join(filter(lambda i: i.isdigit(), cube)))
            if 'red' in cube:
                cubesNumber[0] += int(val)
            if 'green' in cube:
                cubesNumber[1] += int(val)
            if 'blue' in cube:
                cubesNumber[2] += int(val)

        if cubesNumber[0] < 12 and cubesNumber[1] < 13 and cubesNumber[2] < 14:
            return gameID
        else:
            return 0


if __name__ == '__main__':
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        sumValidGames = 0
        for line in f:
            sumValidGames += Solution().isGameValid(line)
    print(sumValidGames)