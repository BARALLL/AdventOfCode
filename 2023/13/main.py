import os
import sys


class Solution:
    # part 1
    def detectMirrorFromReflexion(self, doc, facs) -> int:
        if len(facs) != 2:
            raise ValueError('Expect facs of size 2')
        
        totalCount = 0

        rows = doc.splitlines()
        totalCount += facs[0] * self.findSplitIndex(rows)

        cols = list(zip(*rows))
        totalCount += facs[1] * self.findSplitIndex(cols)

        return totalCount


    def findSplitIndex(self, pattern):
        for i in range(1, len(pattern)):
            topPart = pattern[:i][::-1] # flip the top part array to match index of split
            bottomPart = pattern[i:]

            topPart = topPart[:len(bottomPart)]
            bottomPart = bottomPart[:len(topPart)]

            if topPart == bottomPart:
                return i
        
        return 0



    # part 2
    def detectMirrorWithSmudgeFromReflexion(self, doc, facs) -> int:
        if len(facs) != 2:
            raise ValueError('Expect facs of size 2')
        
        totalCount = 0

        rows = doc.splitlines()
        totalCount += facs[0] * self.detectSmudgeChangingReflexionLine(rows)

        cols = list(zip(*rows))
        totalCount += facs[1] * self.detectSmudgeChangingReflexionLine(cols)

        return totalCount


    def detectSmudgeChangingReflexionLine(self, pattern):
        for i in range(1, len(pattern)):
            topPart = pattern[:i][::-1] # flip the top part array to match index of split
            bottomPart = pattern[i:]

            # does not need to fix the smudge or know its position, but only detect it
            smudgeCount = 0
            for rowTP, rowBP in zip(topPart, bottomPart):
                for elem0, elem1 in zip(rowTP, rowBP):
                    if elem0 != elem1:
                        smudgeCount += 1
            
            if smudgeCount == 1:
                return i
        
        return 0        


        


if __name__ == '__main__':
    facs = [100, 1]
    txt = ""
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            txt += line
    txt = txt.split("\n\n")

    # part 1
    sumPatterns = 0
    for i in range(len(txt)):
        sumPatterns += Solution().detectMirrorFromReflexion(txt[i], facs)

    print(sumPatterns)
    
    # part 2
    sumPatterns = 0
    for i in range(len(txt)):
        sumPatterns += Solution().detectMirrorWithSmudgeFromReflexion(txt[i], facs)

    print(sumPatterns)