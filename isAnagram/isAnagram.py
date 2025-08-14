class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_harfleri={}
        t_harfleri={}

        for i in range(len(s)):
             s_harfleri[s[i]] = s_harfleri.get(s[i], 0)
             t_harfleri[t[i]] = t_harfleri.get(t[i], 0)

        return s_harfleri==t_harfleri
        
