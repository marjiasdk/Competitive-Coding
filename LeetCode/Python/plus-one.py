class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = ""
        for i in digits:
            new += str(i)
        
        new = int(new)
        new = new + 1
        new = str(new)

        output = []
        for i in new:
            output.append(int(i))
        
        return output