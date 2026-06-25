class TrieNode:
    def __init__(self):
        self.children = [None,None]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        root = TrieNode()

        def insert(num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1

                if node.children[bit] is None:
                    node.children[bit] = TrieNode()

                node = node.children[bit]

        def query(num):
            node = root
            ans = 0

            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opp = 1 - bit

                if node.children[opp]:
                    ans |= (1 << i)
                    node = node.children[opp]
                else:
                    node = node.children[bit]

            return ans

        insert(nums[0])
        res = 0

        for i in range(1, len(nums)):
            res = max(res, query(nums[i]))
            insert(nums[i])

        return res