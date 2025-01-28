class Mahasiswa:
    def __init__(self, nim, nama, nohp):
        self.nim = nim
        self.nama = nama
        self.nohp = nohp

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, NoHP: {self.nohp}"

def bubbleSort(daftarMhs):
    n = len(daftarMhs)
    for i in range(n):
        for j in range(0, n-i-1):
            if daftarMhs[j].nim > daftarMhs[j+1].nim:
                daftarMhs[j], daftarMhs[j+1] = daftarMhs[j+1], daftarMhs[j]
    return daftarMhs

def inputDataMhs():
    daftarMhs = []
    jlhMhs = int(input("Masukkan jumlah mahasiswa: "))
   
    for i in range(jlhMhs):
        print(f"\nMasukkan data mahasiswa ke-{i+1}:")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        nohp = input("Masukkan NoHP: ")
        mahasiswa = Mahasiswa(nim, nama, nohp)
        daftarMhs.append(mahasiswa)
   
    daftarMhs = bubbleSort(daftarMhs)
   
    return daftarMhs

def tampilkanMhs(daftarMhs):
    print("\nDaftar Mahasiswa di Kelas Mikroskil terurut berdasarkan NIM:")
    for mahasiswa in daftarMhs:
        print(mahasiswa)

def cariMhs(daftarMhs, cariNIM):
    for mahasiswa in daftarMhs:
        if mahasiswa.nim == cariNIM:
            return mahasiswa
    return None

def cariMhsLain(daftarMhs):
    hasilNyari = []
    hasilTidakAda = []
    print("\n")
    for i in range(3):  
        nim = input(f"Masukkan NIM untuk pencarian ke-{i+1}: ")
        mahasiswa = cariMhs(daftarMhs, nim)
        if mahasiswa:
            hasilNyari.append(mahasiswa)
        else:
            hasilTidakAda.append(mahasiswa)
            
    print("\n")
    print(f"Total mahasiswa ditemukan: {len(hasilNyari)}")
    print(f"Total mahasiswa tidak ditemukan: {len(hasilTidakAda)}")

def main():
    daftarMhs = inputDataMhs()
    tampilkanMhs(daftarMhs)
    hasilNyari = cariMhsLain(daftarMhs)

main()
