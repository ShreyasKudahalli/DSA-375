class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        def upper(nums,x):
            low = 0
            high = len(nums)-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid]>=x:
                    high = mid-1
                else:
                    low = mid+1
            return low
        def possible(x):
            lessthan = 0
            for i in range(n):
                lessthan += upper(mat[i],x)
            return lessthan <= (m*n)//2
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        
        while low <= high:
            mid = (low+high)//2
            if possible(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low