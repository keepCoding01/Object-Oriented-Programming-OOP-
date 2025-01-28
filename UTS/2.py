from tabulate import tabulate  # Supaya rapi pak hehe, pip install tabulate

class WargaKampus:
    def __init__(self, ID, nama, alamat):
        self.ID = ID
        self.nama = nama
        self.alamat = alamat

class Mahasiswa(WargaKampus): 
    def __init__(self, NIM, nama, alamat, kelas):
        super().__init__(NIM, nama, alamat)  
        self.kelas = kelas
        self.angkatan = "20" + NIM[:2]
        self.statusAbsensi = None 

    def Absensi(self):
        self.statusAbsensi = input(f"Masukkan status absensi untuk {self.nama} ({self.ID}): ")
        print(f"Status absensi {self.nama} ({self.ID}): {self.statusAbsensi}\n")

class Dosen(WargaKampus):
    def __init__(self, NIP, nama, alamat, pangkat):
        super().__init__(NIP, nama, alamat)  
        self.pangkat = pangkat 
        self.statusAbsensi = None 

    def Absensi(self):
        self.statusAbsensi = input(f"Masukkan status absensi untuk Dosen {self.nama} ({self.ID}): ")
        print(f"Status absensi Dosen {self.nama} ({self.ID}): {self.statusAbsensi}\n")

class Perkuliahan:
    def __init__(self):
        self.listMhs = [] 
        self.listDosen = [] 

    def TambahMahasiswa(self):
        NIM = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        alamat = input("Masukkan Alamat Mahasiswa: ")
        kelas = input("Masukkan Kelas Mahasiswa: ")
        mahasiswa = Mahasiswa(NIM, nama, alamat, kelas)
        self.listMhs.append(mahasiswa)
        print("Mantap! Data mahasiswa berhasil ditambahkan.\n")

    def TambahDosen(self):
        NIP = input("Masukkan NIP Dosen: ")
        nama = input("Masukkan Nama Dosen: ")
        alamat = input("Masukkan Alamat Dosen: ")
        pangkat = input("Masukkan Pangkat Dosen (AA, Lektor, Lektor Kepala, Guru Besar): ")
        dosen = Dosen(NIP, nama, alamat, pangkat)
        self.listDosen.append(dosen)
        print("Mantap! Data dosen berhasil ditambahkan.\n")

    def UrutBerdasarkanNIM(self):
        self.listMhs.sort(key=lambda mhs: mhs.ID) 
        print("Daftar mahasiswa berhasil diurutkan berdasarkan NIM.\n")
        if self.listMhs:
            table = []
            for mhs in self.listMhs:
                table.append([mhs.ID, mhs.nama, mhs.alamat, mhs.kelas, mhs.angkatan])
            print(tabulate(table, headers=["NIM", "Nama", "Alamat", "Kelas", "Angkatan"], tablefmt="grid"))

    def UrutBerdasarkanNIP(self):
        self.listDosen.sort(key=lambda dosen: dosen.ID) 
        print("Daftar dosen berhasil diurutkan berdasarkan NIP.\n")
        if self.listDosen:
            table = []
            for dosen in self.listDosen:
                table.append([dosen.ID, dosen.nama, dosen.alamat, dosen.pangkat])
            print(tabulate(table, headers=["NIP", "Nama", "Alamat", "Pangkat"], tablefmt="grid"))

    def DetailKelas(self):
        print("Berikut Daftar Mahasiswa:")
        if self.listMhs:
            table = []
            for mhs in self.listMhs:
                table.append([mhs.ID, mhs.nama, mhs.alamat, mhs.kelas, mhs.angkatan, mhs.statusAbsensi])
            print(tabulate(table, headers=["NIM", "Nama", "Alamat", "Kelas", "Angkatan", "Absensi"], tablefmt="grid"))
        else:
            print("Belum ada mahasiswa yang ditambahkan.\n")

    def DetailDosen(self):
        print("Berikut Daftar Dosen:")
        if self.listDosen:
            table = []
            for dosen in self.listDosen:
                table.append([dosen.ID, dosen.nama, dosen.alamat, dosen.pangkat, dosen.statusAbsensi])
            print(tabulate(table, headers=["NIP", "Nama", "Alamat", "Pangkat", "Absensi"], tablefmt="grid"))
        else:
            print("Belum ada dosen yang ditambahkan.\n")

    def TampilkanMenu(self):
        menu = [
            ["1", "Tambah Mahasiswa"],
            ["2", "Tambah Dosen"],
            ["3", "Urutkan Berdasarkan NIM Mahasiswa"],
            ["4", "Urutkan Berdasarkan NIP Dosen"],
            ["5", "Absensi Mahasiswa"],
            ["6", "Absensi Dosen"],
            ["7", "Detail Kelas Mahasiswa"],
            ["8", "Detail Dosen"],
            ["9", "Keluar"]
        ]
        print("\n\tUTS-TasyaSyafriza\n\tMenu Perkuliahan")
        print(tabulate(menu, headers=["No", "Menu"], tablefmt="fancy_grid"))

kuliah = Perkuliahan()

while True:
    kuliah.TampilkanMenu()
    pilihan = input("Silakan pilih menu sesuai yang ada ditabel: ")

    if pilihan == "1":
        kuliah.TambahMahasiswa()
    elif pilihan == "2":
        kuliah.TambahDosen()
    elif pilihan == "3":
        kuliah.UrutBerdasarkanNIM()
    elif pilihan == "4":
        kuliah.UrutBerdasarkanNIP()
    elif pilihan == "5":
        if kuliah.listMhs:
            for mhs in kuliah.listMhs:
                mhs.Absensi()
        else:
            print("Belum ada mahasiswa yang ditambahkan.\n")
    elif pilihan == "6":
        if kuliah.listDosen:
            for dosen in kuliah.listDosen:
                dosen.Absensi()
        else:
            print("Belum ada dosen yang ditambahkan.\n")
    elif pilihan == "7":
        kuliah.DetailKelas()
    elif pilihan == "8":
        kuliah.DetailDosen()
    elif pilihan == "9":
        print("Terima kasih sudah menggunakan program saya.")
        break
    else:
        print("Pilihan kamu tidak valid, silakan coba lagi ya.")
