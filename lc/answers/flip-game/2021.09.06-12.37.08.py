"""
so an easy solution... if length of state is < 2, return []
else start on first index and do the whole, use previous index to see if there are two contiguous
+'s (++). If there are, then stamp out a version if those were to be flipped. 
"""
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []
        states = []
        for i in range(1, len(currentState)):
            if currentState[i] == '+' and currentState[i - 1] == '+':
                buffer = list(currentState)
                buffer[i] = '-'
                buffer[i - 1] = '-'
                states.append("".join(buffer))
        return states