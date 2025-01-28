class Mahasiswa:
    def halo(self, nim):
        self.nim = nim
        print("Halo", nim)

class Mahasiswa2:
    _instance= None
    def __new__(kelas,  *args, **kwargs) :
        if not kelas._instance:
            kelas._instance = super(Mahasiswa2, kelas).__new__(kelas, *args, **kwargs)
        return kelas._instance
    def halo(self, str, nim, nama):
        self.str = str
        self.nim = nim
        self.nama = nama
        print("Halo", str)

obj1 = Mahasiswa2()
obj1.halo("Hai", "231119990", "Budi")
obj2 = Mahasiswa2()
obj1.halo("Hai", "231119992", "Ani")
obj3 = Mahasiswa2()
print("Str Obj1:",obj1.str, obj1.nim, obj1.nama)
print("Str Obj2:",obj2.str, obj2.nim, obj2.nama)
print("Str Obj3:",obj3.str, obj3.nim, obj3.nama)

obj2.halo("Hai", "231119995", "Jojo")
print("Setelah diubah obj2")
print("Str Obj1:",obj1.str, obj1.nim, obj1.nama)
print("Str Obj2:",obj2.str, obj2.nim, obj2.nama)
print("Str Obj3:",obj3.str, obj3.nim, obj3.nama)