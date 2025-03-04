class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = False
        sum = 0
        for i in range(len(s)):
            if (flag == True): flag = False; continue
            if s[i] == 'I': 
                if (i + 1 < len(s)) and s[i + 1] == 'V': 
                    sum += 4
                    i = i + 1
                    flag = True
                elif (i + 1 < len(s)) and s[i + 1] == 'X': 
                    sum +=9
                    i = i + 1
                    flag = True
                else: sum += 1
                
            elif s[i] == 'V': sum += 5
            elif s[i] == 'X': 
                if (i + 1 < len(s)) and s[i + 1] == 'L': 
                    sum += 40
                    i = i + 1
                    flag = True
                elif (i + 1 < len(s)) and s[i + 1] == 'C': 
                    sum +=90
                    i = i + 1
                    flag = True
                else: sum += 10
            elif s[i] == 'L': sum += 50
            elif s[i] == 'C': 
                if (i + 1 < len(s)) and s[i + 1] == 'D': 
                    sum += 400
                    i = i + 1
                    flag = True
                elif (i + 1 < len(s)) and s[i + 1] == 'M': 
                    sum +=900
                    i = i + 1
                    flag = True
                else: sum += 100
                
            elif s[i] == 'D': sum += 500
            elif s[i] == 'M': sum += 1000
        return sum
sol = Solution()

print(sol.romanToInt("IV"))