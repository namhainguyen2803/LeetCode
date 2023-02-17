class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 10 + 1 = 100
        
        if len(a) > len(b):
            while len(a) > len(b):
                b = "0" + b
        elif len(b) > len(a):
            while len(b) > len(a):
                a = "0" + a
        # print(a, b)
        length = len(a)
        res = str()
        remainder = [0 for i in range(length)]
        i = 1
        while i <= length:

            num_a = int(a[length-i])
            num_b = int(b[length-i])
            # print(num_a, num_b)
            if length - i == 0:
                if remainder[length-i] != 0:
                    if (num_a == 1 and num_b == 0) or (num_a == 0 and num_b == 1):
                        res = "10" + res
                    elif num_a == 1 and num_b == 1:
                        res = "11" + res
                    else:
                        res = "1" + res
                    remainder[length-i] -= 1
                else:
                    if (num_a == 1 and num_b == 0) or (num_a == 0 and num_b == 1):
                        res = "1" + res
                    elif num_a == 1 and num_b == 1:
                        res = "10" + res
                    else:
                        res = "0" + res
                break
                
            
            else:
                
                if num_a == 0 and num_b == 0:
                    res = str(num_a + num_b + remainder[length-i]) + res
                    if remainder[length-i] != 0:
                        remainder[length-i] -= 1
                    
                elif (num_a == 1 and num_b == 0) or (num_a == 0 and num_b == 1):
                    if remainder[length-i] == 0:
                        res = "1" + res
                        if remainder[length-i] != 0:
                            remainder[length-i] -= 1
                    else:
                        remainder[length-i-1] += 1
                        res = "0" + res
                
                else:
                    if remainder[length-i] == 0:
                        remainder[length-i-1] += 1
                        res = "0" + res
                    else:
                        remainder[length-i-1] += 1
                        res = "1" + res
                        remainder[length-i] -= 1
                i += 1
        return res

sol = Solution()

str1 = "11"
str2 = "1"
print(sol.addBinary(str1, str2))