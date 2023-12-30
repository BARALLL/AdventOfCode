import os
import sys



class Solution:
    def PipeMaze(self, doc) -> int:
        doc = doc.split("\n")
        posSY, posSX = self.getSPosition(doc)
        distanceMap = self.buildDistanceMapAndCycleFromPoint(posSX, posSY, doc)

        return max(map(max, distanceMap))

    # since we dont know the shape of S, we try all 4 directions
    def buildDistanceMapAndCycleFromPoint(self, posSX: int, posSY: int, doc):
        distanceMap = [[-1 for _ in range(len(doc[i]))] for i in range(len(doc))]
        distanceMap[posSY][posSX] = 0
        for x, y in [(posSX, posSY - 1), (posSX, posSY + 1), (posSX - 1, posSY), (posSX + 1, posSY)]:
            if y >= 0 and y < len(doc) and x >= 0 and x < len(doc[y]):
                if x != posSX or y != posSY:
                    isCycle, cycle = self.buildCycleFromPoint(1, distanceMap, posSX, posSY, x, y, doc)
                    if isCycle:
                        finalCycle = cycle
                        break

        return distanceMap, finalCycle

    def getSPosition(self, doc):
        for i in range(len(doc)):
            if 'S' in doc[i]:
                return i, doc[i].find('S')
        

    # recursive DP approach
    def buildCycleFromPoint(self, depth, distanceMap, fromX: int, fromY: int, x: int, y: int, doc) -> int:
        # make sure we are not on a invalid tile
        if y < 0 or y >= len(doc) or x < 0 or x >= len(doc[y]) or doc[y][x] == '.':
            return False, []

        # base case, we already explored this tile and found a shorter path to it
        if (distanceMap[y][x] != -1 and distanceMap[y][x] <= depth):
            return doc[y][x] == 'S', []


        # we travel to the next tile, while making sure we don't travel back
        match doc[y][x]:
            case '|':
                if fromY == y+1 and fromX == x: # if we come from the bottom we go up next step
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x, y-1, doc)
                elif fromY == y-1 and fromX == x:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap,  x, y, x, y+1, doc)
                else: return False, []
            case '-':
                if fromY == y and fromX == x-1:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x+1, y, doc)
                elif fromY == y and fromX == x+1:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x-1, y, doc)
                else: return False, []
            case 'L':
                if fromY == y and fromX == x+1:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x, y-1, doc)
                elif fromY == y-1 and fromX == x:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x+1, y, doc)
                else: return False, []
            case 'J':
                if fromY == y and fromX == x-1:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x, y-1, doc)
                elif fromY == y-1 and fromX == x:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x-1, y, doc)
                else: return False, []
            case '7':
                if fromY == y and fromX == x-1:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x, y+1, doc)
                elif fromY == y+1 and fromX == x:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x-1, y, doc)
                else: return False, []
            case 'F':
                if fromY == y and fromX == x+1:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x, y+1, doc)
                elif fromY == y+1 and fromX == x:
                    isCycle, cycle = self.buildCycleFromPoint(depth+1, distanceMap, x, y, x+1, y, doc)
                else: return False, []

        # we write the distance to travel in order to reach this tile
        if isCycle:
            distanceMap[y][x] = depth
            cycle.append((x, y))
        
        return isCycle, cycle


    # shoelace formula
    def calcAreaEnclosed(self, doc: str):
        doc = doc.split("\n")
        posSY, posSX = self.getSPosition(doc)

        distanceMap, cycle = self.buildDistanceMapAndCycleFromPoint(posSX, posSY, doc)

        area = 0
        n = len(cycle)
        for i in range(n):
            j = (i + 1) % n
            area += cycle[i][0] * cycle[j][1]
            area -= cycle[j][0] * cycle[i][1]
        area = abs(area) // 2
        return area - n // 2 + 1


        # areaWaitingToBeAccepted = 0
        # inLoop = False

        # for line in distanceMap:
        #     print(line)
        #     areaWaitingToBeAccepted = 0
        #     wasPipe = False
        #     inLoop = False

        #     for i in range(1, len(line)):
        #         if line[i] != -1:
        #             if wasPipe:
        #                 inLoop = not inLoop
        #                 area += areaWaitingToBeAccepted
        #                 areaWaitingToBeAccepted = 0
        #             else:
        #                 wasPipe = True
        #         else:
        #             if wasPipe:
        #                 areaWaitingToBeAccepted += 1
        # return area


if __name__ == '__main__':
    area = 0
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line
    
    area = Solution().calcAreaEnclosed(txt)
    print(area)