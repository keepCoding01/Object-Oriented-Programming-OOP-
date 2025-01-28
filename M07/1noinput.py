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
    dataMhs = [
        ("12345", "Tasya Syafriza", "081234567890"),
        ("12346", "Andi Rahman", "081234567891"),
        ("12347", "Budi Santoso", "081234567892"),
        ("12348", "Citra Dewi", "081234567893"),
        ("12349", "Diana Putri", "081234567894")
    ]
    
    for nim, nama, nohp in dataMhs:
        yield Mahasiswa(nim, nama, nohp)

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
        nim = input(f"Masukkan NIM untuk pencarian ke-{i + 1}: ")
        mahasiswa = cariMhs(daftarMhs, nim)
        if mahasiswa:
            hasilNyari.append(mahasiswa)
        else:
            hasilTidakAda.append(nim)
            
    print("\n")
    print(f"Total mahasiswa ditemukan: {len(hasilNyari)}")
    print(f"Total mahasiswa tidak ditemukan: {len(hasilTidakAda)}")

def main():
    generator = inputDataMhs()
    daftarMhs = list(generator)
    daftarMhs = bubbleSort(daftarMhs)  
    
    print(f'\nJumlah mahasiswa yang sudah di dalam kelas: {len(daftarMhs)} orang')
    tampilkanMhs(daftarMhs)
    
    cariMhsLain(daftarMhs)

main()
