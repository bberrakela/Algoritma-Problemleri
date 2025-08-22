class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        sol = 0
        sag = x
        sonuc = 0
        
        while sol <= sag:
            orta = (sol + sag) // 2
            
            if orta * orta == x:
                return orta
            elif orta * orta < x:
                sonuc = orta
                sol = orta + 1
            else:
                sag = orta - 1
                
        return sonuc
