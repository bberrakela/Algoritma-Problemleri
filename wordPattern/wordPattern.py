class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p_to_s_map = {}
        s_to_p_map = {}

        for i in range(len(pattern)):
            char_p = pattern[i]
            word_s = words[i]
            
            if char_p in p_to_s_map:
                if p_to_s_map[char_p] != word_s:
                    return False
            else:
                if word_s in s_to_p_map:
                    return False
                p_to_s_map[char_p] = word_s
                s_to_p_map[word_s] = char_p
        
        return True

