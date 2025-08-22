class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        beklenen_toplam = n * (n + 1) // 2
        gercek_toplam = sum(nums)
        return beklenen_toplam - gercek_toplam
