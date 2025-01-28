import os

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

class State:
    def tapIn(self, mahasiswa):
        print(f"{mahasiswa.nama} telah tap in.")

    def tapOut(self, mahasiswa):
        print(f"{mahasiswa.nama} telah tap out.")

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.state = State()  

    def setState(self, state):
        self.state = state

    def tapIn(self):
        self.state.tapIn(self)

    def tapOut(self):
        self.state.tapOut(self)

class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

class Perkuliahan:
    def __init__(self):
        self.mahasiswa = []
        self.dosen = []

    def detailKelas(self):
        print("\nMahasiswa")
        if self.mahasiswa:
            for i, mahasiswa in enumerate(self.mahasiswa, 1):
                print(f"{i}. {mahasiswa.nama} - {mahasiswa.nim}")
        else:
            print("Belum ada mahasiswa yang ditambahkan.")

        print("\nDosen")
        if self.dosen:
            for i, dosen in enumerate(self.dosen, 1):
                print(f"{i}. {dosen.nama} - {dosen.nip}")
        else:
            print("Belum ada dosen yang ditambahkan.")

    def tambahMahasiswa(self):
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        self.mahasiswa.append(Mahasiswa(nama, nim))

    def tambahDosen(self):
        nama = input("Masukkan nama dosen: ")
        nip = input("Masukkan NIP dosen: ")
        self.dosen.append(Dosen(nama, nip))

    def tapIn(self):
        if not self.mahasiswa:
            print("Belum ada mahasiswa yang bisa tap in.")
            return
        nim = input("Masukkan NIM mahasiswa yang tap in: ")
        mahasiswa = next((m for m in self.mahasiswa if m.nim == nim), None)
        if mahasiswa:
            mahasiswa.tapIn()
            print("Berhasil tap in.")
        else:
            print("Mahasiswa tidak ditemukan.")

    def tapOut(self):
        if not self.mahasiswa:
            print("Belum ada mahasiswa yang bisa tap out.")
            return
        nim = input("Masukkan NIM mahasiswa yang tap out: ")
        mahasiswa = next((m for m in self.mahasiswa if m.nim == nim), None)
        if mahasiswa:
            mahasiswa.tapOut()
            print("Berhasil tap out.")
        else:
            print("Mahasiswa tidak ditemukan.")

    def templateMethod(self):
        self.start()
        self.greet()
        self.absen()
        self.ceramah()
        self.diskusi()
        self.penutup()

    def start(self):
        print("Dosen membuka perkuliahan.")

    def greet(self):
        print("Pembelajaran akan segera dimulai.")

    def absen(self):
        print("Melakukan absensi.")

    def ceramah(self):
        pass

    def diskusi(self):
        pass

    def penutup(self):
        print("Dosen menutup perkuliahan.")

class Teori(Perkuliahan):
    def ceramah(self):
        print("Dosen memaparkan teori.")

    def diskusi(self):
        print("Melakukan diskusi teori.")

class Praktek(Perkuliahan):
    def ceramah(self):
        print("Dosen memberikan arahan praktikum.")

    def diskusi(self):
        print("Diskusi masalah praktikum.")

clr()
ob = Perkuliahan()

while True:
    print("\nMenu")
    print("=====")
    print("1. Tambah Dosen")
    print("2. Tambah Mahasiswa")
    print("3. Detail Kelas")
    print("4. Tap In")
    print("5. Tap Out")
    print("6. Tampilkan Template")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan sesuai yang ada di menu: ")
    if pilihan == "1":
        ob.tambahDosen()
    elif pilihan == "2":
        ob.tambahMahasiswa()
    elif pilihan == "3":
        ob.detailKelas()
    elif pilihan == "4":
        ob.tapIn()
    elif pilihan == "5":
        ob.tapOut()
    elif pilihan == "6":
        print("\nTemplate Teori:")
        teori = Teori()
        teori.templateMethod()

        print("\nTemplate Praktek:")
        praktek = Praktek()
        praktek.templateMethod()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
