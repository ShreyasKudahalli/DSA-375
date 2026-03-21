class Solution:
    def merge(self,arr,left,mid,right):
        l = left
        r = mid+1
        res = []
        
        while l <= mid and r <= right:
            if arr[l] <= arr[r]:
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r += 1
        while l <= mid:
            res.append(arr[l])
            l += 1
        
        while r <= right:
            res.append(arr[r])
            r += 1
            
        for i in range(len(res)):
            arr[left + i] = res[i]
 
    def mergeSort(self, arr, l, r):
        #code 
        
        if l >= r:
            return
        mid = (l+r)//2
        
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        
        self.merge(arr,l,mid,r)