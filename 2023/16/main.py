import os
import sys
from typing import List
from collections import defaultdict

class Solution:
    
    def sendBeam(self, contraption, fromY: int, fromX: int, directionY: int, directionX: int) -> int:
        # DP
        memo = [[dict() for _ in range(len(contraption[0]))] for _ in range(len(contraption))]
        return self.sendBeamDP(fromY, fromX, memo, contraption, directionY, directionX)

    def sendBeamDP(self, y: int, x: int, memo, contraption, speedY: int, speedX: int):
        if y < 0 or y >= len(contraption) or x < 0 or x >= len(contraption[0]):
            return 0
        
        # a beam already passed here with the same direction, meaning all tiles on the path
        # have already been energized
        if memo[y][x].get((speedY, speedX), -1) != -1:
            return 0 #memo[y][x][(speedX, speedY)]

        energizedTiles = 0

        if len(memo[y][x]) == 0: # no beam passed through this tile yet
            energizedTiles += 1
        
        # write in memo that a beam already passed here in the same direction
        # in order to prevent cycling
        memo[y][x][(speedY, speedX)] = 0

        if contraption[y][x] == '.':
            energizedTiles += self.sendBeamDP(y+speedY, x+speedX, memo, contraption, speedY, speedX)
        elif contraption[y][x] == '/': # (-1, 0) <=> (0, 1) or (1, 0) <=> (0, -1)
            if speedX != 0: # arriving from left or right, left rotation
                energizedTiles += self.sendBeamDP(y-speedX, x+speedY, memo, contraption, -speedX, speedY)
            else:
                energizedTiles += self.sendBeamDP(y+speedX, x-speedY, memo, contraption, speedX, -speedY)
        elif contraption[y][x] == '\\': # (-1, 0) <=> (0, -1) or (1, 0) <=> (0, 1)
            if speedX != 0: # arriving from left or right, right rotation
                energizedTiles += self.sendBeamDP(y+speedX, x-speedY, memo, contraption, speedX, -speedY)
            else:
                energizedTiles += self.sendBeamDP(y-speedX, x+speedY, memo, contraption, -speedX, speedY)
        elif contraption[y][x] == '|':
            if speedY != 0: # pass through
                energizedTiles += self.sendBeamDP(y+speedY, x+speedX, memo, contraption, speedY, speedX)
            else: # split beam: (0, [-]1) <=> (1, 0) and (-1, 0)
                energizedTiles += self.sendBeamDP(y+speedX, x+speedY, memo, contraption, speedX, speedY)
                energizedTiles += self.sendBeamDP(y-speedX, x-speedY, memo, contraption, -speedX, speedY)
        elif contraption[y][x] == '-':
            if speedX != 0: # pass through
                energizedTiles += self.sendBeamDP(y+speedY, x+speedX, memo, contraption, speedY, speedX)
            else: # split beam: ([-]1, 0) <=> (0, 1) and (0, -1)
                energizedTiles += self.sendBeamDP(y+speedX, x+speedY, memo, contraption, speedX, speedY)
                energizedTiles += self.sendBeamDP(y+speedX, x-speedY, memo, contraption, speedX, -speedY)

        memo[y][x][(speedY, speedX)] = energizedTiles

        return memo[y][x][(speedY, speedX)]



if __name__ == '__main__':
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line

    txt = txt.splitlines()

    # part 1
    energizedTiles = Solution().sendBeam(txt, 0, 0, 0, 1)
    print(energizedTiles)

    # part 2
    maxEnergizedTile = 0
    # startingPointLeadingToMaxEnergizedTile

    for y in range(len(txt)):
        maxEnergizedTile = max(
            maxEnergizedTile,
            Solution().sendBeam(txt, y, 0, 0, 1),
            Solution().sendBeam(txt, y, len(txt)-1, 0, -1)
        )

    for x in range(len(txt[0])):
        maxEnergizedTile = max(
            maxEnergizedTile,
            Solution().sendBeam(txt, 0, x, 1, 0),
            Solution().sendBeam(txt, len(txt)-1, x, -1, 0)
        )

    print(maxEnergizedTile)