import re

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        largest = -1
        matches = re.finditer(r'(\d)\1{2}',num)
        for match in matches:
            num = int(match.group(0))
            if num > int(largest):
                largest = str(match.group(0))
        
        if largest == -1:
            return ""
        return largest
            

s = Solution()
print(s.largestGoodInteger("6777133339"))
print(s.largestGoodInteger("2300019"))
print(s.largestGoodInteger("42352338"))
        