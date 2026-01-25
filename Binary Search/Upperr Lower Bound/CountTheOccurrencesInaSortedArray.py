class Solution:
    def countFreq(self, arr, target):
        low = 0
        high = len(arr)-1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if first == -1:
            return 0
        low = 0
        high = len(arr) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last-first+1
        