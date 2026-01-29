class Solution:
    def findPages(self, arr, k):
        if len(arr)<k:
            return -1
        def possible(pages):
            student = 1
            count = 0

            for x in arr:
                if count + x > pages:
                    student += 1
                    count = x
                else:
                    count += x

            return student <= k
            
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = (low+high)//2
            if possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
            