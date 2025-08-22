class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_degeri = x ^ y
        mesafe = 0
        
        while xor_degeri > 0:
            xor_degeri = xor_degeri & (xor_degeri - 1)
            mesafe += 1
            
        return mesafe
        
