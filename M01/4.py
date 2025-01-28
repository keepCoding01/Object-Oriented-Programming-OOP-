class Gudang:
    def __init__(self) :
        self.data = []
        self.nomorToko = 1
    def cari(self, namaBarang):
        for i in range(0, len(self.data)):      #Perulangan sejumlah barang digudang
            if(self.data[i].nama == namaBarang):#Pengecekan nama barang yang sama dengan yang ada digudang
                print(self.data[i].nama)
                print(self.data[i].brand)
                print(self.data[i].jumlah)
                print("\n")
    def tambahBarang(self, barang):
        self.data.append(barang)                #Tambah barang baru kegudang
    def barangKeluar(self, namaBarang, jumlah):
        for i in range(0, len(self.data)):      #Perulangan sejumlah barang digudang
            if(self.data[i].nama == namaBarang):#Pengecekan nama barang yang sama dengan yang ada digudang
                self.data[i].jumlah -= jumlah   #Mengurangi jumlah barang
                break                           #Menghentikan perulangan setelah mengurangi jumlahbarang digudangs
class Komputer:
    def __init__(self):
        self.nama = "Komputer"
        self.ram = 16
        self.storage = 1
        self.brand = "HP"
        self.jumlah = 10

''' #Varian2
class Komputer:
    def __init__(self, nama, brand, jumlah):
        self.nama = nama
        self.brand = brand
        self.jumlah = jumlah
'''
objek1 = Komputer()
objek2= Komputer()
objek2.brand = "Samsung"    
toko = Gudang()
toko.tambahBarang(objek1)
toko.tambahBarang(objek2)
status = True
while(status):
    print("Menu Gudang PT.XYZ")
    print("1. Cari Barang")
    print("2. Simpan Barang")
    print("3. Keluarkan Barang")
    print("Pilihan : ")
    pil = input()
    if(pil=="1"):
        print("Cari Barang")
        nama = input("Nama Barang : ")
        toko.cari(nama)
        input("Tekan enter untuk kembali ke menu !!")
    elif(pil=="2"):
        print("Simpan Barang")
        nama = input("Nama Barang : ")
        brand = input("Brand : ")
        jlh = input("Jumlah : ")

        #Varian1
        objek3 =Komputer()
        objek3.nama = nama
        objek3.brand = brand
        objek3.jlh = jlh

        #Varian2
        #objek3 = Komputer(nama, brand, jlh)

        toko.tambahBarang(objek3)
        input("Tekan enter untuk kembali ke menu !")
    elif(pil=="3"):
        print("Keluarkan Barang")
        nama = input("Nama Barang : ")
        jlh = int(input("Jumlah Barang : "))
        toko.barangKeluar(nama, jlh)
        input("Tekan enter untuk kembali ke menu !!")
    else:
        status = False


    

