class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        
        Input: words = ["cat","bt","hat","tree"], chars = "atach"
        Output: 6
        Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
        """
        sum = 0
        for word in words:
            charsTemp = chars
            toAdd = True
            for i in range(len(word)):
                #print(word[i])
                if word[i] in charsTemp:
                    charsTemp = charsTemp.replace(word[i], "",1)
                    #print(charsTemp)
                else:
                    toAdd = False
                    break
            if toAdd:
                sum += len(word)
        return sum
        

words = ["cat","bt","hat","tree"]
chars = "atach"
s = Solution()
print(words, chars)
print(s.countCharacters(words,chars))
        
        