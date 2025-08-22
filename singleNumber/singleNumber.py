class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        tek_sayi = 0
        
        for num in nums:
            tek_sayi ^= num
            
        return tek_sayi
        
