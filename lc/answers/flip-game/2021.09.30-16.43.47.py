class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) == 1: return []
        states = []
        for i in range(1, len(currentState)):
            if currentState[i] == "+" and currentState[i - 1] == "+":
                buffer = list(currentState)
                buffer[i] = "-"
                buffer[i - 1] = "-"
                states.append("".join(buffer))
        return states