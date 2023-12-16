from math import ceil, floor


class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_matches  = 0
        if n == 2:
            return 1
        
        matches = floor(n/2)
        advances = ceil(n/2)
        total_matches  += matches
        return int(total_matches  + self.numberOfMatches(advances))
    
    #bestverson
    def numberOfMatches2(self, n):
        return n - 1
            
        
s = Solution()
print(s.numberOfMatches(7))
print(s.numberOfMatches(14))