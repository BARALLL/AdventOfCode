import os
import sys


class Solution:
    def CosmicExpansion(self, doc, expansionFac) -> int:
        doc = doc.splitlines()
        distances = list()
        knownGalaxies = list()
        rowHasGalaxy = [False] * len(doc)
        colHasGalaxy = [False] * len(doc[0])

        # parse the document, writing galaxy presence and its indices
        for i in range(len(doc)):
            for j in range(len(doc[i])):
                if doc[i][j] == '#':
                    colHasGalaxy[j] = True
                    rowHasGalaxy[i] = True
                    knownGalaxies.append((i, j))

        # calc the distance between each pair of galaxies, counting (A, B) but not (B, A)
        for i in range(len(knownGalaxies) - 1):
            for j in range(i+1, len(knownGalaxies)):
                distances.append(self.getShortestDistanceBetweenTwoPoints(knownGalaxies[i], knownGalaxies[j], colHasGalaxy, rowHasGalaxy, expansionFac))
        
        return sum(distances)

    # manhattan distance
    def getShortestDistanceBetweenTwoPoints(self, pointA, pointB, colHasGalaxy, rowHasGalaxy, expansionFac) -> int:
            dist = 0
            maxX = max(pointA[1], pointB[1])
            minX = min(pointA[1], pointB[1])
            maxY = max(pointA[0], pointB[0])
            minY = min(pointA[0], pointB[0])

            return maxX - minX + colHasGalaxy[minX:maxX].count(False) * (expansionFac - 1) + maxY - minY + rowHasGalaxy[minY:maxY].count(False) * (expansionFac - 1)


if __name__ == '__main__':
    expansionFac = 100

    sumDist = 0
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line
    
    sumDist = Solution().CosmicExpansion(txt, expansionFac)
    print(sumDist)