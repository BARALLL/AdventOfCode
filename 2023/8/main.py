import os
import sys
import math

class State:
    def __init__(self, name: str, R=None, L=None):
        self.name = name
        self.R = R
        self.L = L

    def setRightState(self, state):
        self.R = state

    def setLeftState(self, state):
        self.L = state
    
    def getTransitionState(self, direction):
        if direction == 'R':
            return self.R
        if direction == 'L':
            return self.L

class Solution:
    def networkNavigation(self, txt) -> int:
        lines = txt.splitlines()
        instructionSequence = lines[0]
        initialState = self.buildStateMachine(lines)
        return self.transitionToZ(initialState, instructionSequence)


    def buildStateMachine(self, lines: str) -> State:
        states = dict()
        for i in range(2, len(lines)):
            if lines[i][0] not in states:
                # take AAA = (BBB, CCC) as example
                # lines[i][0] correspond to A
                # is this state was not already defined, create it
                states[lines[i][0]] = State(str(lines[i][0]))

            # parse next states on L/R transitions

            # the char just after '(', here B
            leftStateChar = lines[i][lines[i].find('(') + 1]
            # is this state already created then just set the left state of
            # ou current state be this state, otherwise create it first
            if leftStateChar in states:
                states[lines[i][0]].setLeftState(states[leftStateChar])
            else:
                states[leftStateChar] = State(str(leftStateChar))
                states[lines[i][0]].setLeftState(states[leftStateChar])
            
            # the char just before ')', here C
            # rfind for performances because ')' is closer of the end than the start
            rightStateChar = lines[i][lines[i].rfind(')') - 1]
            # same logic as left state for for the right state
            if rightStateChar in states:
                states[lines[i][0]].setRightState(states[rightStateChar])
            else:
                states[rightStateChar] = State(str(rightStateChar))
                states[lines[i][0]].setRightState(states[rightStateChar])

        # return the firstly added State, which is the initial state
        return states[lines[2][0]]


    def transitionToZ(self, initialState, inputSequence):
        count = 0
        state = initialState

        while state.name != 'Z':
            for direction in inputSequence:
                state = state.getTransitionState(direction)
                count += 1
        return count


if __name__ == '__main__':
    transitionNeededToReachZ = 0
    os.chdir(sys.path[0])
    txt = ""
    with open("input.txt", "r") as f:
        for line in f:
            txt += line
    transitionNeededToReachZ = Solution().networkNavigation(txt)
    print(transitionNeededToReachZ)