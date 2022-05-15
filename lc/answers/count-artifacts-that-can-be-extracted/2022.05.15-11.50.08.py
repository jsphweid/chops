"""
===== Initial Thoughts =====
quantities = [0, 0]
{
    (0,0) -> 0
    (0,1) -> 1
    (1,1) -> 1
}

=== Brute Force Approach ===
just store all the points and a mapping to them, and decrement some count

~~Complexity Analysis
Time - O(n**2)
Space - O(n**2)

=== Implemented Approach ===
we need a better way of figuring out which belongs to which (better than n^2)

~~Complexity Analysis
Time - 
Space - 

FAILED
2
[[0,0,0,0],[0,1,1,1]]
[[0,0],[0,1]]

apparently got 0.....
counts=[]
coord_to_artifact_i={}
"""

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        counts = []
        coord_to_artifact_i = {}

        def add_artifacts(data, idx):
            num_added = 0
            for i in range(data[0], data[2] + 1):
                for j in range(data[1], data[3] + 1):
                    coord_to_artifact_i[(i, j)] = idx
                    num_added += 1
            return num_added

        for i in range(len(artifacts)):
            counts.append(add_artifacts(artifacts[i], i))

        for i, j in dig:
            if (i, j) in coord_to_artifact_i:
                counts[coord_to_artifact_i[(i, j)]] -= 1

        return sum([c == 0 for c in counts])
            



