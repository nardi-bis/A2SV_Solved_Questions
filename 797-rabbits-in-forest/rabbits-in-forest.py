class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashmap = {}
        total = 0

        for a in answers:
            if a not in hashmap:
                hashmap[a] = a   # remaining spots in this group
                total += a + 1   # create a new group
            else:
                hashmap[a] -= 1  # fill the group

                if hashmap[a] < 0:
                    hashmap[a] = a   # start a new group
                    total += a + 1

        return total