import os
import sys

class Solution:
    def Scratchcards(self, strInput: str) -> int:
        return sum([self.cardPointsValue(line) for line in strInput.split("\n")])
    
    def cardPointsValue(self, card: str) -> int:
        count = 0
        parts = card.split("|")
        winningNumbers = (parts[0].split(":"))[1].split(" ")
        cardNumbers = parts[1].split(" ")
        cardNumbers = list(map(lambda s: ''.join(filter(lambda i: i.isdigit(), s)), cardNumbers))
        for number in cardNumbers:
            if number != '' and number in winningNumbers:
                count += 1
        return 2**(count-1) if count > 1 else count


if __name__ == '__main__':
    sumPileScratchcards = 0
    os.chdir(sys.path[0])
    with open("input.txt", "r") as f:
        for line in f:
            sumPileScratchcards += Solution().cardPointsValue(line)
    print(sumPileScratchcards)