class RandomizedSet:
    def __init__(self):
        self.nums = []     
        self.pos = {}       

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.nums.append(val)       
        self.pos[val] = len(self.nums) - 1  
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]         
        last_val = self.nums[-1]  

        
        self.nums[idx] = last_val
        self.pos[last_val] = idx

        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)