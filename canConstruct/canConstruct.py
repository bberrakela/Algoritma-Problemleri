class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_harfleri = Counter(magazine)

        for harf in ransomNote:
             if magazine_harfleri[harf]==0:
                 return False
             magazine_harfleri[harf] -= 1
        return True

        
