class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sonuc_listesi=[]

        for i in range (1, n + 1):
            if i%3==0 and i%5==0:
                sonuc_listesi.append("FizzBuzz")
            elif i%3==0:
                sonuc_listesi.append("Fizz")
            elif i%5==0:
                sonuc_listesi.append("Buzz")
            else:
                sonuc_listesi.append(str(i))
        return sonuc_listesi    
        
