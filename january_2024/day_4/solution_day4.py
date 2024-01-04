class Solution(object):
    def count_occ(self,nums):
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        return num_counts

    def minOperations(self, nums):
        dict = self.count_occ(nums)
        print(dict)
        counter = 0
        for value in dict.values():
            if value == 1:
                return -1
            counter += value // 3
            if value % 3 != 0:
                counter += 1

        return int(counter)               
        
s = Solution()
print(s.minOperations([2,3,3,2,2,4,2,3,4]))
#print(s.minOperations([2,1,2,2,3,3]))
a= [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(s.minOperations(a))
      
      
      
      # 5 / 3 + 1