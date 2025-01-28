listNilai = [80, 90, 100, 75, 10] #objek iterable
myIter = iter(listNilai)    #Objek iterator
print("Cetak-1:", next(myIter))
a = next(myIter) #pemanggilan next tetap harus ditampung agar nilai tidak hilang begitu saja
print("Cetak-2:", a)

print("Cetak-3:", next(myIter))

print("\nPerbedaan Kode iterator dengan iterasi manual")
def lanjutAntrian(que, index):
    print(que[index])

c=0
que = ["Budi", "Anto", "Cici", "Zilong"]
myIter = iter(que)
lanjutAntrian(que, c)
c+=1
lanjutAntrian(que, c)
c+=1
lanjutAntrian(que, c)
c+=1
lanjutAntrian(que, c)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))

