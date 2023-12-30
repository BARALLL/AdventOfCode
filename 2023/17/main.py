import os
import sys
from typing import List
from collections import defaultdict
from heapq import heappush, heappop
class Solution:

    # part 1
    def heatLoss(self, cityMap):
        cityMap = [list(map(int, line)) for line in cityMap]
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            hl, r, c, dr, dc, nbStep = heappop(pq)

            if r == len(cityMap) - 1 and c == len(cityMap[0]) - 1:
                return hl

            if (r, c, dr, dc, nbStep) in seen:
                continue

            seen.add((r, c, dr, dc, nbStep))

            if nbStep < 3 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(cityMap) and 0 <= nc < len(cityMap[0]):
                    heappush(pq, (hl + cityMap[nr][nc], nr, nc, dr, dc, nbStep + 1))

            for ndr, ndc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(cityMap) and 0 <= nc < len(cityMap[0]):
                        heappush(pq, (hl + cityMap[nr][nc], nr, nc, ndr, ndc, 1))
    


    def heatLossWithBetterCrucibles(self, cityMap):
        cityMap = [list(map(int, line)) for line in cityMap]
        seen = set()
        pq = [(0, 0, 0, 0, 0, 0)]

        while pq:
            hl, r, c, dr, dc, nbStep = heappop(pq)

            if r == len(cityMap) - 1 and c == len(cityMap[0]) - 1 and nbStep >= 4:
                return hl

            if (r, c, dr, dc, nbStep) in seen:
                continue

            seen.add((r, c, dr, dc, nbStep))

            if nbStep < 10 and (dr, dc) != (0, 0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(cityMap) and 0 <= nc < len(cityMap[0]):
                    heappush(pq, (hl + cityMap[nr][nc], nr, nc, dr, dc, nbStep + 1))

            if nbStep >= 4 or (dr, dc) == (0, 0):
                for ndr, ndc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                        nr = r + ndr
                        nc = c + ndc
                        if 0 <= nr < len(cityMap) and 0 <= nc < len(cityMap[0]):
                            heappush(pq, (hl + cityMap[nr][nc], nr, nc, ndr, ndc, 1))



if __name__ == '__main__':
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line

    txt = txt.splitlines()

    # part 1
    minimalHeatLoss = Solution().heatLoss(txt)
    print(minimalHeatLoss)

    # part 2
    minimalHeatLoss = Solution().heatLossWithBetterCrucibles(txt)
    print(minimalHeatLoss)