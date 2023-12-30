import os
import sys

class Solution:
    def seedAndFertilizer(self, f) -> int:
        txt = ""
        for line in f:
            txt += line
        seeds, almanac = self.parseDoc(txt)
        return min(self.seedToLocation(seeds, almanac))

    def parseDoc(self, doc: str):
        almanac = list(list())
        maps = doc.split(":")

        seeds = maps[1].split("\n")[0].split(" ")
        seeds = list(map(lambda s: int(''.join(filter(lambda i: i.isdigit(), s))), seeds[1:]))

        k = 0
        for mapInfo in maps[2:]:
            parts = mapInfo.split("\n")
            almanac.append([])
            
            for i in range(len(parts) - 1):
                if(parts[i] != ''):
                    infoList = parts[i].split(" ")
                    almanac[k].append([int(infoList[0].strip()), int(infoList[1].strip()), int(infoList[2].strip())])
            k += 1
        return seeds, almanac


    def seedToLocation(self, seeds, almanac):
        src = seeds
        for tMap in almanac:
            src = self.applyMap(src, tMap)
        return src


    def applyMap(self, src, tMap):
        mappedInfo = []
        for srcNumber in src:
            mappingFound = False
            for [value, start, size] in tMap:
                if srcNumber >= start and srcNumber < start + size:
                    mappingFound = True
                    mappedInfo.append(value + srcNumber - start)
            if not mappingFound:
                mappedInfo.append(srcNumber)
        return mappedInfo
                



if __name__ == '__main__':
    seedAndFertilizer = -1
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
            seedAndFertilizer = Solution().seedAndFertilizer(f)
    print(seedAndFertilizer)