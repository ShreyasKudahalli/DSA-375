class Solution:
    def findFloor(self, arr, x):
        low = 0
        high = len(arr)-1
        
        while low <= high:
            mid = (low + high)//2
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high
        