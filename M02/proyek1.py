# Izin menggunakan komentar ya pak, agar memudahkan kami ketika melihat codenya kembali.
# kami membuat 8 class sebagai berikut :
# class orang, pengirim, penerima, barang, jadwal, status pengiriman, pengiriman(induk untuk merangkap semua),
# jasa pengiriman(untuk menginput data pengguna sekaligus menjalankan program pertama dengan beberapa fungsi).

# Kelas Orang = kelas induk untuk Pengirim dan Penerima
class Orang:
    def __init__(self, nama, alamat, noHp):
        self.nama = nama
        self.alamat = alamat
        self.noHp = noHp

    def infoOrang(self):
        return f"\nNama: {self.nama}, Alamat: {self.alamat}, No HP: {self.noHp}"

# Kelas Pengirim mewarisi kelas Orang
class Pengirim(Orang):
    def __init__(self, nama, alamat, noHp):
        super().__init__(nama, alamat, noHp)

# Kelas Penerima mewarisi kelas Orang
class Penerima(Orang):
    def __init__(self, nama, alamat, noHp):
        super().__init__(nama, alamat, noHp)

# Kelas Barang = menyimpan informasi barang yang dikirim
class Barang:
    def __init__(self, namaBarang, beratBarang, jenisBarang):
        self.namaBarang = namaBarang
        self.beratBarang = beratBarang
        self.jenisBarang = jenisBarang

    def infoBarang(self):
        return f"\nNama Barang: {self.namaBarang}, Berat: {self.beratBarang} kg, Jenis: {self.jenisBarang}"

# Kelas Jadwal = menyimpan informasi jadwal pengiriman
class Jadwal:
    def __init__(self, tanggalKirim, tanggalTiba):
        self.tanggalKirim = tanggalKirim
        self.tanggalTiba = tanggalTiba

    def infoJadwal(self):
        return f"\nTanggal Kirim: {self.tanggalKirim}, Perkiraan Tiba: {self.tanggalTiba}"

# Kelas StatusPengiriman = menyimpan status pengiriman
class StatusPengiriman:
    def __init__(self, status):
        self.status = status

    def infoStatus(self):
        return f"\n---> Status Pengiriman: {self.status}"

# Kelas Pengiriman = kelas induk yang mengelola seluruh data pengiriman untuk mencetak struk
class Pengiriman:
    def __init__(self, barang, pengirim, penerima, jadwal, statusPengiriman):
        self.barang = barang
        self.pengirim = pengirim
        self.penerima = penerima
        self.jadwal = jadwal
        self.statusPengiriman = statusPengiriman

    def cetakStruk(self):
        print("A. Data Pengirim", self.pengirim.infoOrang(), "\n")
        print("B. Data Penerima", self.penerima.infoOrang(), "\n")
        print("C. Data Barang",self.barang.infoBarang(), "\n")
        print("D. Data Jadwal",self.jadwal.infoJadwal())
        print(self.statusPengiriman.infoStatus(), "\n")
    
# Kelas utama untuk mengelola keseluruhan program jasa pengiriman
class JasaPengiriman:
    def __init__(self):
        self.dataPengiriman = []

    def pilihLayanan(self):
        print("\nSilakan Pilih Jenis Layanan Pengiriman Anda")
        print("1. Reguler (Tiba dalam 4 hari)")
        print("2. Same Day (Tiba hari ini)")
        print("3. Hemat (Tiba dalam 14 hari)")
        print("4. Express (Tiba dalam 1 hari)")
        pilihan = input("Pilih layanan (1/2/3/4)\t\t: ")

        if pilihan == "1":
            return 4  # Reguler
        elif pilihan == "2":
            return 0  # Same Day
        elif pilihan == "3":
            return 14  # Hemat
        elif pilihan == "4":
            return 1  # Express
        else:
            print("Pilihan Anda tidak terdaftar, kami akan gunakan Reguler sebagai default pengiriman.")
            return 4  # Default Reguler

    def buatPengiriman(self):
        print("\nSilakan Isi Data Pengiriman Barang Anda")
        # Input data barang
        print("DATA BARANG")
        print("-"*15)
        namaBarang = input("Nama Barang\t\t: ")
        beratBarang = float(input("Berat Barang (kg)\t: "))
        jenisBarang = input("Jenis Barang\t\t: ")
        barang = Barang(namaBarang, beratBarang, jenisBarang)
        print("\n")

        # Input data pengirim
        print("DATA PENGIRIM")
        print("-"*15)
        namaPengirim = input("Nama Pengirim\t\t: ")
        alamatPengirim = input("Alamat Pengirim\t\t: ")
        noHpPengirim = input("No HP Pengirim\t\t: ")
        pengirim = Pengirim(namaPengirim, alamatPengirim, noHpPengirim)
        print("\n")


        # Input data penerima
        print("DATA PENERIMA")
        print("-"*15)
        namaPenerima = input("Nama Penerima\t\t: ")
        alamatPenerima = input("Alamat Penerima\t\t: ")
        noHpPenerima = input("No HP Penerima\t\t: ")
        penerima = Penerima(namaPenerima, alamatPenerima, noHpPenerima)
        print("\n")


        # Input layanan jasa pengiriman
        hariPengiriman = self.pilihLayanan()

        # Hitung tanggal kirim dan tiba secara manual
        tanggalKirim = input("tanggal kirim (dd/mm/yy)\t: ")  
        if hariPengiriman == 0:  # Same Day
            tanggalTiba = tanggalKirim
        else:
            tanggalTiba = f"{hariPengiriman} hari setelah {tanggalKirim}"

        jadwal = Jadwal(tanggalKirim, tanggalTiba)

        # Status pengiriman secara manual
        status = "Barang sedang diproses"
        statusPengiriman = StatusPengiriman(status)

        # Buat objek pengiriman
        pengiriman = Pengiriman(barang, pengirim, penerima, jadwal, statusPengiriman)

        # Simpan data pengiriman
        self.dataPengiriman.append(pengiriman)
        print("\nData pengiriman berhasil dibuat!\n")

    def cetakStruk(self):
        if not self.dataPengiriman:
            print("Belum ada data pengiriman.")
        else:
            for i, pengiriman in enumerate(self.dataPengiriman, 1):
                print(f"\nStruk Pengiriman #{i}")
                print("-"*20)
                pengiriman.cetakStruk()

    def jalankan(self):
        status = True
        while status:
            print("\nMenu Jasa Pengiriman J&T Express")
            print("1. Buat Jasa Pengiriman")
            print("2. Cetak Struk Pengiriman")
            print("3. Keluar")
            pilihan = input("Pilih menu (1/2/3): ")

            if pilihan == "1":
                self.buatPengiriman()
            elif pilihan == "2":
                self.cetakStruk()
            elif pilihan == "3":
                print("Terima kasih telah menggunakan Jasa Pengiriman kami.")
                status = False
            else:
                print("Pilihan tidak valid, coba lagi.")


# Main program
jasaPengiriman = JasaPengiriman()
jasaPengiriman.jalankan()
