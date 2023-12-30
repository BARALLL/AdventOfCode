import os
import sys


class Solution:
    def hotSprings(self, doc) -> int:
        totalCount = 0
        doc = doc.splitlines()
        for line in doc:
            totalCount += self.countSpringArrangements(line)
            
        return totalCount

    def countSpringArrangements(self, line):
        parts = line.split(" ")
        springs = parts[0]
        # cGDS = contiguousGroupDamagedSprings
        cGDSRecord = parts[1]
        cGDSRecord = list(map(int, cGDSRecord.split(",")))
        
        memo = dict()
        
        return self.arrangementsDP(len(springs)-1, memo, springs, cGDSRecord, 0, len(cGDSRecord) - 1)
    
    def arrangementsDP(self, i: int, memo, springs, cGDSRecord, cGDSCount: int, indexCGDS: int):
        # base case, we reached the end of the string and everything was correct
        if i < 0:
            if (indexCGDS == -1 and cGDSCount == 0) or (indexCGDS == 0 and cGDSCount == cGDSRecord[indexCGDS]):
                return 1
            return 0

        # Check if the current state is in the memo dictionary
        if (i, cGDSCount, indexCGDS) in memo:
            return memo[(i, cGDSCount, indexCGDS)]

        nbArrangements = 0

        # -- check validity --
        # in case of '?', we want to try both cases ('?' is a '.' or a '#')
        if springs[i] == '?' or springs[i] == '.':
            sp = list(springs)
            sp[i] = "."
            sp = "".join(sp)
            # not (finished a group and it is not of the expected size)
            if not (cGDSCount > 0 and cGDSCount != cGDSRecord[indexCGDS]):
                # => restart for the next group
                if cGDSCount > 0:
                    nbArrangements += self.arrangementsDP(i-1, memo, sp, cGDSRecord, 0, indexCGDS - 1)
                else:
                    nbArrangements += self.arrangementsDP(i-1, memo, sp, cGDSRecord, 0, indexCGDS)

        if springs[i] == '?' or springs[i] == '#':
            # we continue if we did not already passed the number of contigious springs for this group
            if not (cGDSCount + 1 > cGDSRecord[indexCGDS]):
                sp = list(springs)
                sp[i] = "#"
                sp = "".join(sp)
                nbArrangements += self.arrangementsDP(i-1, memo, sp, cGDSRecord, cGDSCount + 1, indexCGDS)

        memo[(i, cGDSCount, indexCGDS)] = nbArrangements
        
        return nbArrangements


        
        #call recursively
        # put count in the memo
        # return count
        

if __name__ == '__main__':
    totalNumberOfArrangements = 0
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line
    
    totalNumberOfArrangements = Solution().hotSprings(txt)
    print(totalNumberOfArrangements)