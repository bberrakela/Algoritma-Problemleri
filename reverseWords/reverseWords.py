class Solution:
    def reverseWords(self, s: str) -> str:
        kelimeler = s.split(' ')
        
        ters_kelimeler = []
        for kelime in kelimeler:
            ters_kelime = kelime[::-1]
            ters_kelimeler.append(ters_kelime)
            
        return " ".join(ters_kelimeler)
        
