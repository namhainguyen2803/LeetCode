import math
import collections
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        def count_len_digit(n):
            if n > 0:
                digits = int(math.log10(n))+1
            elif n == 0:
                digits = 1
            else:
                digits = int(math.log10(-n))+2 
            return digits
        
        res = list()
        number = k
        i = 1
        while number % 10**i != number:
            a = number % 10**i
            res.append(a//10**(i-1))
            number -= a
            i += 1
        res.append(number//10**(i-1))
        res_2 = list()
        for i in range(1, len(res)+1):
            res_2.append(res[len(res)-i])
        # if len(num) > k:
        print(res_2)
        len_k = len(res_2)
        
        result = collections.deque()
        if len_k > len(num):
            larger = res_2
            smaller = num
        else:
            smaller = res_2
            larger = num
        
        i = 1
        remainder = 0
        # print(larger)
        # print(smaller)
        while True:
            if len(smaller)-i >= 0:
                a = larger[len(larger)-i]
                b = smaller[len(smaller)-i]
                
                c = a + b + remainder
                if remainder != 0:
                    remainder -= 1
                if c < 10:
                    result.appendleft(c)
                else:
                    d = c
                    while d >= 10:
                        d -= 10
                        remainder += 1
                    result.appendleft(d)
                i += 1
            else:
                if len(larger)-i < 0:
                    break
                else:
                    a = larger[len(larger)-i]
                    c = a + remainder
                    if remainder != 0:
                        remainder -= 1
                    if c < 10:
                        result.appendleft(c)
                    else:
                        d = c
                        while d >= 10:
                            d -= 10
                            remainder += 1
                        result.appendleft(d)
                    i += 1
        
        if remainder != 0:
            result.appendleft(remainder)
        return result

sol = Solution()
print(sol.addToArrayForm([9,9,9,9], 9999))