class Solution(object):
    def findContentChildren(self, greed, cookies):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        greed.sort() 
        cookies.sort()
        children_counter = 0
        i = 0
        j = 0
        while i< len(cookies) and j < len(greed):
            if cookies[i] >= greed[j]:
                children_counter += 1
                j += 1
            i += 1

        return children_counter
    
    #optimized solution