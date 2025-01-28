import os
import math
def clr():os.system('cls')

def penjumlahan(a, b, c):
    return a+b+c


def ntoletter(n):
    if(n==0):return " "
    return (chr(64+n))
def ntoletterLow(n):
    if(n==0):return " "
    return (chr(96+n))
def pangkat(x, y):
    return pow(x,y)


clr()
listAngka = ['5', '6', '1', '4', '2', '3']
listAngka2 =  [2,   2,   3,   2,   2,   2]

#Comprehension
dt2 = [int(i) for i in listAngka]
print("Comprehension Fungsi int( )\n", dt2)

dt3 = [ntoletter(i) for i in dt2 if i<4]
print("\nComprehension Fungsi ntoletter(n) dengan tambahan if i<4\n", dt3)

dt2 = [pangkat(dt2[n], listAngka2[n]) for n in range(len(listAngka))]
print("\nComprehension Fungsi pangkat(x, y) dengan banyak parameter\n", dt2)

#map
dt3 = map(lambda x:int(x), listAngka)
dt3 = list(dt3)
print("\nMap fungsi int( )\n", dt3)

#Format : (Fungsi, iterable)
dt4 = map(ntoletter, dt3)
print("\nMap fungsi ntoletter(n)\n", list(dt4))

#kondisi harus memiliki else, tidak bisa kosong. jika pada else tdk ada return maka akan menjadi "none"
#Gunakan lambda jika ingin membaca nilai iterable satu persatu
dt4 = map(lambda x:ntoletter(x) if x>4 else ntoletterLow(x), dt3)
print("\nMap fungsi ntoletter(n) dengan 2 kondisi if-else\n", list(dt4))

#Format : (Fungsi, iterable1, iterable2, iterable3, ...dst)
dt4 = map(lambda x,y:pangkat(x, y), dt3, listAngka2)
print("\nMap fungsi pangkat(x, y) dengan 2 parameter\n", list(dt4))

