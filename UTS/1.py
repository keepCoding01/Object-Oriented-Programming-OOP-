from tabulate import tabulate  # Supaya rapi pak hehe, pip install tabulate

class TasyaSyafriza: 
    def __init__(self, NIM, nama, alamat, kelas):
        self.NIM = NIM
        self.nama = nama
        self.alamat = alamat
        self.kelas = kelas
        self.angkatan = "20" + NIM[:2]

class Perkuliahan:
    def __init__(self):
        self.listMhs = [] 

    def TambahMahasiswa(self):
        NIM = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        alamat = input("Masukkan Alamat Mahasiswa: ")
        kelas = input("Masukkan Kelas Mahasiswa: ")
        mahasiswa = TasyaSyafriza(NIM, nama, alamat, kelas)
        self.listMhs.append(mahasiswa)
        print("Mantap! Data mahasiswa berhasil ditambahkan.\n")

    def UrutBerdasarkanNIM(self):
        self.listMhs.sort(key=lambda mhs: mhs.NIM)
        print("Daftar mahasiswa berhasil diurutkan berdasarkan NIM.\n")
        self.DetailKelas()  

    def DetailKelas(self):
        print("Berikut Daftar Mahasiswa:")
        if self.listMhs:
            table = []
            for mhs in self.listMhs:
                table.append([mhs.NIM, mhs.nama, mhs.alamat, mhs.kelas, mhs.angkatan])
            print(tabulate(table, headers=["NIM", "Nama", "Alamat", "Kelas", "Angkatan"], tablefmt="grid"))
        else:
            print("Belum ada mahasiswa yang ditambahkan.\n")

    def TampilkanMenu(self):
        menu = [
            ["1", "Tambah Mahasiswa"],
            ["2", "Urutkan Berdasarkan NIM"],
            ["3", "Detail Kelas"],
            ["4", "Keluar"]
        ]
        print("\n\tUTS-TasyaSyafriza\n\tMenu Perkuliahan")
        print(tabulate(menu, headers=["No", "Menu"], tablefmt="fancy_grid"))

kuliah = Perkuliahan()

while True:
    kuliah.TampilkanMenu()  
    pilihan = input("Silakan pilih menu sesuai yang ada ditabel : ")

    if pilihan == "1":
        kuliah.TambahMahasiswa()
    elif pilihan == "2":
        kuliah.UrutBerdasarkanNIM()
    elif pilihan == "3":
        kuliah.DetailKelas()
    elif pilihan == "4":
        print("Terima kasih sudah menggunakan program saya.")
        break
    else:
        print("Pilihan kamu tidak valid, silakan coba lagi ya.")
