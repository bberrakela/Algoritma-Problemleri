class Solution:
    def isPalindrome(self, s: str) -> bool:
        temizlenmis_dize = ""
        for karakter in s:
            if karakter.isalnum():
                temizlenmis_dize += karakter.lower()
        
        return temizlenmis_dize == temizlenmis_dize[::-1]
