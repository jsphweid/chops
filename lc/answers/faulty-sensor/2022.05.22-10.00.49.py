"""
===== Initial Thoughts =====
[2,3,4,5]
[2,1,3,4]

[2,3,4]
[2,4,1] (bad)

[3]

[2,3,2,2,3,2]
[2,3,2,3,2,7] (bad)

[2]

[2,3,4,5]
[2,1,3,4]

change top
[2,n5,3,4]
[2,1, 3,4]

change bottom
[2,3, 4,5]
[2,n4,1,3]

[2,3,4,5]
[2,1,3,4]

[2,2,2,2,2]
[2,2,2,2,5]

[2,4]
[4,6]

[4,2,4]
[4,6]

[2,4]
[6,4,6]

[2,3,2]
[3,2,3]

[2,2,3,2]
[3,2,3]
"""

def num_diffs(arr1, arr2):
    return sum([l != r for l, r in zip(arr1, arr2)])

class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        if num_diffs(sensor1, sensor2) == 0:
            return -1

        for i, (l, r) in enumerate(zip(sensor1, sensor2)):
            if l != r:
                if i == len(sensor1) - 1:
                    return -1
                answers = []
                if sensor1[-1] != sensor2[i] and num_diffs([sensor1[-1]] + sensor1[i:], sensor2[i:]) == 1:
                    answers.append(1)
                if sensor2[-1] != sensor1[i] and num_diffs(sensor1[i:], [sensor2[-1]] + sensor2[i:]) == 1:
                    answers.append(2)
                return -1 if len(answers) != 1 else answers[0]
        return -1
                




