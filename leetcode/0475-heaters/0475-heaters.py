class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0
        
        for house in houses:
            i = bisect.bisect_left(heaters, house)
            
            if i == 0:
                closest = heaters[0] - house
            elif i == len(heaters):
                closest = house - heaters[-1]
            else:
                closest = min(
                    house - heaters[i - 1],
                    heaters[i] - house
                )
            
            radius = max(radius, closest)
        
        return radius
            