from collections import defaultdict


class Subseq:
    def __init__(self, sec, da=[], dp=[]):
        self.secuencia = sec
        self.doubElem = da
        self.doubElem_ = dp

    def desarrollo(self):
        total = 0
        elem = len(self.secuencia)
        if elem < 3:
            print("Secuencia de tamaño NO aceptado")
            return 0

        for i in range(elem):
            self.doubElem.append(defaultdict(int))

        for i in range(elem):
            self.doubElem_.append(defaultdict(int))

        for i in range(1, elem):
            for j in range(i):
                self.doubElem[i][self.secuencia[i] - self.secuencia[j]] += 1

        self.doubElem_[0] = self.doubElem_[1] = {}

        for i in range(2, elem):
            for j in range(i):
                k = self.secuencia[i] - self.secuencia[j]

                if k in self.doubElem[j]:
                    self.doubElem_[i][k] += self.doubElem[j][k]
                    total += self.doubElem[j][k]

                if k in self.doubElem_[j]:
                    self.doubElem_[i][k] += self.doubElem_[j][k]
                    total += self.doubElem_[j][k]

        return total


#nums = []
#D = Subseq(nums)
#print(D.desarrollo())
'''
n = int(input("Tamaño de la lista:"))
nums = []
for x in range(n):
    valor = int(input("Ingrese valor entero: "))
    nums.append(valor)
print(nums)
D = Subseq(nums)
print(D.desarrollo())
'''
