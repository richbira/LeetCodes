class Solution(object):
    def findMatrix(self, nums):
        final_list = []
        while True:
            length = len(nums)
            temp_list = []
            i = 0
            while i in range(length):
                first_element = nums.pop(0)
                if first_element not in temp_list:
                    temp_list.append(first_element)
                else:
                    nums.append(first_element)
                i += 1
            final_list.append(temp_list)
            if nums == []:
                break

        return final_list
            
        
s = Solution()
print(s.findMatrix([1,3,4,1,2,3,1]))
