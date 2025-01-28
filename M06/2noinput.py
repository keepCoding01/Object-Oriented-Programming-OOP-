class Mahasiswa:
    def __init__(self, nim, nama, nohp):
        self.nim = nim
        self.nama = nama
        self.nohp = nohp

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, NoHP: {self.nohp}"

def inputDataMhs():
    daftarMhs = [
        Mahasiswa("12345", "Tasya Syafriza", "081234567890"),
        Mahasiswa("12346", "Andi Rahman", "081234567891"),
        Mahasiswa("12347", "Budi Santoso", "081234567892"),
        Mahasiswa("12348", "Citra Dewi", "081234567893"),
        Mahasiswa("12349", "Diana Putri", "081234567894")
    ]
    
    daftarMhs.sort(key=lambda mhs: mhs.nim)
   
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
        nim = input(f"Masukkan NIM untuk melakukan absensi mahasiswa ke-{i+1}: ")
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
