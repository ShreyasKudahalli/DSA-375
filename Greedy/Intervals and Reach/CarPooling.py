class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        events = []
        for num, start, end in trips:
            events.append((start, num))
            events.append((end, -num))
        
        events.sort()
        passengers = 0
        for _, change in events:
            passengers += change
            if passengers > capacity:
                return False
        return True


