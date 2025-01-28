class Mahasiswa:
    def __init__(self, nim, nama, nohp):
        self.nim = nim
        self.nama = nama
        self.nohp = nohp
 
    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, NoHP: {self.nohp}"
 
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
   
    return daftarMhs
 
def tampilkanMhs(daftarMhs):
    print("\nDaftar Mahasiswa di Kelas Mikroskil:")
    for mahasiswa in daftarMhs:
        print(mahasiswa)
 
def cariMhs(daftarMhs, nim_dicari):
    for mahasiswa in daftarMhs:
        if mahasiswa.nim == nim_dicari:
            return mahasiswa
    return None
 
def cariMhsLain(daftarMhs):
    hasilNyari = []
    hasilTidakAda = []
    for i in range(3):  
        print("\n")
        nim = input(f"Masukkan NIM untuk pencarian ke-{i+1}: ")
        mahasiswa = cariMhs(daftarMhs, nim)
        if mahasiswa:
            print(f"Data ditemukan: {mahasiswa}")
            hasilNyari.append(mahasiswa)
            
        else:
            print(f"Data tidak ditemukan untuk NIM: {nim}")
            hasilTidakAda.append(mahasiswa)
            
    print(f"Total mahasiswa ditemukan: {len(hasilNyari)}")
    print(f"Total mahasiswa tidak ditemukan: {len(hasilTidakAda)}")

 
def main():
    daftarMhs = inputDataMhs()
    tampilkanMhs(daftarMhs)
    cariMhsLain(daftarMhs)

main()