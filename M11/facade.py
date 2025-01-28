# menyediakan antarmuka yang lebih sederhana untuk sistem kompleks dengan menyembunyikan detail di balik layar.

class kasir :
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
    def minta(self):
        print("Kasir diminta proses bon untuk pelanggan {}".format(self.pelanggan))
    def proses(self):
        print("Kasir mencetak bon untuk pelanggan {}".format(self.pelanggan))
    
class pelayan :
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
    def pemesanan (self):
        print("Pelayan mencetak pesanan pelanggan {}".format(self.pelanggan))
    def antarPesan(self):
        print("Pelayan mengantar pesanan pelanggan {}".format(self.pelanggan))
    def mintaBon (self):
        print("Pelayan meminta bon sama kasir")
    def antarBon (self):
        print("Pelayan mengantar bon pelanggan {}".format(self.pelanggan))

class restoran :
    def __init__(self, pelanggan):
        self.kasir = kasir(pelanggan)
        self.pelayan = pelayan(pelanggan)
    def prosesPemesanan (self):
        self.pelayan.pemesanan()
        self.pelayan.antarPesan()
        self.pelayan.mintaBon()
        self.kasir.minta()
        self.kasir.proses()
        self.pelayan.antarBon()

if __name__ == '__main__':
    pelanggan = "budi"
    Resto_apri = restoran(pelanggan)
    Resto_apri.prosesPemesanan()