class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1
        ans = float('inf')
        index = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                low = mid + 1
            else:
                if arr[mid] < ans:
                    ans = arr[mid]
                    index = mid
                high = mid - 1

        return index
        