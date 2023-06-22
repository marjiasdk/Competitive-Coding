class Solution(object):
    def isAnagram(self, s, t):
        lst_s = []
        lst_t = []

        for i in s:
            lst_s.append(i)
        for i in t:
            lst_t.append(i)
        
        if sorted(lst_s) == sorted(lst_t):
            return True
        else:
            return False