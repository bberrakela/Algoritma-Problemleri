class Solution:
    def calPoints(self, operations: list[str]) -> int:
        skor_kaydi = []
        
        for op in operations:
            if op.lstrip('-').isdigit():
                skor_kaydi.append(int(op))
            elif op == "+":
                toplam = skor_kaydi[-1] + skor_kaydi[-2]
                skor_kaydi.append(toplam)
            elif op == "D":
                iki_kati = skor_kaydi[-1] * 2
                skor_kaydi.append(iki_kati)
            elif op == "C":
                skor_kaydi.pop()
        
        return sum(skor_kaydi)
