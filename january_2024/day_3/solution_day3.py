class Solution(object):
    def trasform_to_number(self, numero):
        for x in numero:
            if x == "0":
                numero = numero.replace("0", "")
        
        return len(numero)

    def numberOfBeams(self, bank):
        list_len = []
        for i in bank:
            value = self.trasform_to_number(i)
            if value > 0:
                list_len.append(value)
        i = 0
        sum = 0
        while i < len(list_len)-1:
            x = list_len[i] * list_len[i+1]
            sum += int(x)
            i += 1
        return sum
    
s = Solution()
bank = ["011001","000000","010100","001000"]
print(s.numberOfBeams(bank))