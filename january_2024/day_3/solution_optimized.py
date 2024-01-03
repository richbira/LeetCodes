class Solution(object):
    def numberOfBeams(self, bank):
        prev, ans = 0, 0
        for i in bank:
            current = i.count('1')
            if current:
                ans += prev * current
                prev = current
        return ans
        
s = Solution()
bank = ["011001","000000","010100","001000"]
print(s.numberOfBeams(bank))