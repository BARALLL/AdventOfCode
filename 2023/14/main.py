import os
import sys
from typing import List

class Solution:
    
    # part 1
    def tiltPlatformNorth(self, platform) -> int:
        platform = platform.splitlines()
        titledPlatform = self.rollNorth(platform)
        return self.getPlatformLoad(titledPlatform)

    # naive solution
    def rollInDirection(self, platform: List[str]):
        # somethingMoved = True
        numPass = 1
        while numPass < len(platform):
            for i in range(1, len(platform)):
                # somethingMoved = False
                for j in range(len(platform[i])):
                    if platform[i][j] == 'O' and platform[i-1][j] == '.':
                            platform[i][j] = '.'
                            platform[i-1][j] = 'O'
                            # somethingMoved = True
            numPass += 1
        return platform

    def rollNorth(self, platform: List[str]):
        # transpose platform
        tPlatform = list(map("".join, zip(*platform)))
        newPlatform = list()

        for row in tPlatform:
            newRow = list()
            # get all parts that will stop the rocks from rolling
            for part in row.split('#'):
                # sort the part in reverse: 
                # all the rocks will end up at the left to the empty spots
                newRow.append("".join(sorted(part, reverse=True)))
            
            # the new row is now a list containing the non moving rock followed
            # by all the rocks prior to the next non moving rock, followed by the empty spots
            newPlatform.append("#".join(newRow))

        # transpose it back
        return list(map("".join, zip(*newPlatform)))

    def getPlatformLoad(self, titledPlatform):
        load = 0
        l = len(titledPlatform)
        for i in range(l):
            load += (l - i) * titledPlatform[i].count('O')
        return load

    # part 2
    def tiltPlatformForCycle(self, platform, numCycle) -> int:
        platform = platform.splitlines()

        # because brute force over the 1.10^9 cycles wont work,
        # we need to store previously encountered platforms to detect a cycle
        encounteredPlatforms = {tuple(platform)}
        # to keep the indices
        encounteredPlatformsList = [platform]

        cycledAtIndex = -1
        
        for i in range(numCycle):
            platform = self.completeCycle(platform)
            # already encountered the platform
            if tuple(platform) in encounteredPlatforms:
                cycledAtIndex = i
                break
            encounteredPlatforms.add(tuple(platform))
            encounteredPlatformsList.append(platform)

        # find the index of the previous similar plaform 
        indexPrevEncounteredPlatform = encounteredPlatformsList.index(platform)

        # the index of the final plaform is the modulo of how many cycle remaining by how many cycle between the two encounter
        # that we offset by the index of the first encounter        
        finalPlatform = encounteredPlatformsList[(numCycle - indexPrevEncounteredPlatform) % (cycledAtIndex + 1 - indexPrevEncounteredPlatform) + indexPrevEncounteredPlatform]

        return self.getPlatformLoad(finalPlatform)


    def completeCycle(self, platform: List[str]):
        for i in range(4):
            platform = self.rotatePlatform(platform)
            platform = self.rollNorth(platform)
        return platform


    def rotatePlatform(self, platform):
        #rotate platform by 90° clockwise
        return list(["".join(row[::-1]) for row in zip(*platform)])



if __name__ == '__main__':
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line

    # part 1
    totalLoad = Solution().tiltPlatformNorth(txt)

    print(totalLoad)

    # part 2
    totalLoad = Solution().tiltPlatformForCycle(txt, 1000000000)

    print(totalLoad)