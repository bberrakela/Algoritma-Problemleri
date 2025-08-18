class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            
            next_number = 0
            while n > 0:
                digit = n % 10
                next_number += digit * digit
                n //= 10
            n = next_number
            
        return n == 1
          
