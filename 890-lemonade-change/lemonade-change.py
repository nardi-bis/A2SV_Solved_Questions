class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        diction = {5:0,10:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                diction[5] += 1
            elif bills[i] == 10:
                if diction[5] >= 1:
                    diction[5] -= 1
                    diction[10] += 1
                else:
                    return False
            else:
                if diction[5] >= 1 and diction[10] >= 1:
                    diction[5] -= 1
                    diction[10] -= 1
                elif diction[5] >= 3:
                    diction[5] -= 3
                else:
                    return False
        return True



