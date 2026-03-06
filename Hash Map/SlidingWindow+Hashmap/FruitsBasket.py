class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        res = 0
        l = 0
        r = 0
        while r < len(fruits):
            fruit = fruits[r]

            if fruit in basket:
                basket[fruit] += 1
            else:
                basket[fruit] = 1
            
            while len(basket)>2:
                fruit = fruits[l]
                basket[fruit] -= 1
                if basket[fruit] == 0:
                    del basket[fruit]
                l += 1
            res = max(res, (r-l)+1)
            r += 1
        return res