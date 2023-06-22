class Solution(object):
    def maximumCount(self, nums):
        pos = []
        neg = []

        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
        
        if len(pos) > len(neg):
            return len(pos)
        elif len(pos) < len(neg):
            return len(neg)
        else:
            return len(pos)