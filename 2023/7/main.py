import os
import sys
import math


class Solution:
    def camelCards(self, txt) -> int:

        hands, bids = self.parseDoc(txt)

        cards = 'AKQJT98765432'

        type = 0
        types = dict()
        ranks = list()
        tempTypesRanking = list()
        for i in range(len(hands)):
            type = self.handOrderOfStrength(hands[i])
            if type in types:
                l = len(types[type])
                for j in range(l):
                    newHandIsStronger = self.decideStrongestHand(hands[types[type][j]], hands[i], cards)
                    if not newHandIsStronger:
                        types[type].insert(j, i)
                        break
                    if j == l-1:
                        types[type].append(i)


            else:
                types[type] = [i]
        # types = [self.handOrderOfStrength(hands[i]) for i in range(len(hands))]

        for i in range(1, 7):
            if i in types:
                for handIndex in types[i]:
                    ranks.append(handIndex)


        return sum([(i+1) * bids[ranks[i]] for i in range(len(ranks))])


    def parseDoc(self, doc: str):
        lines = doc.split("\n")
        parts = list()
        hands = list()
        bids = list()

        for line in lines:
            parts = line.split(" ")
            hands.append(parts[0])
            bids.append(int(parts[1]))

        return hands, bids


    def handOrderOfStrength(self, hand):
        type = 0
        maxCount = 0
        pairNum = 0  
        freq = dict()
        for char in hand:
            freq[char] = 0

        for char in hand:
            freq[char] += 1

        for item in freq.items():
            if item[1] == 5:
                maxCount = 7
            elif item[1] == 4:
                maxCount = 6
            elif item[1] == 3:
                maxCount = 4
            elif item[1] == 2:
                pairNum += 1
        
        if maxCount == 3 and pairNum == 1:
            type = 5
        elif pairNum == 2:
            type = 3
        elif maxCount == 0 and pairNum == 1:
            type = 2
        elif maxCount != 0:
            type = maxCount
        else:
            type = 0            

        return type

    def decideStrongestHand(self, hand1: str, hand2: str, cards):
        for i in range(len(hand1)):
            if hand1[i] != hand2[i]:
                return False if cards.find(hand1[i]) < cards.find(hand2[i]) else True

if __name__ == '__main__':
    totalWinnings = -1
    os.chdir(sys.path[0])
    txt = ""
    with open("input.txt", "r") as f:
        for line in f:
            txt += line
    totalWinnings = Solution().camelCards(txt)
    print(totalWinnings)