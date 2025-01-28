from GudangM12 import Gudang
import unittest

class testGudang(unittest.TestCase):
    def setUp(self):
        self.gudang = Gudang()

    def test_tambahBarang(self):
        tambah1 = self.gudang.tambahBarang("Kabel", "USB", "US01", 12000)
        self.assertEqual(tambah1, "Jenis Baru\nTipe Baru\nSeri Baru")

    def test_tambahSeri(self):
        self.test_tambahBarang()
        tambah2 = self.gudang.tambahBarang("Kabel", "USB", "US02", 15000)
        self.assertEqual(tambah2, "Jenis Lama\nTipe Lama\nSeri Baru")

    def test_tambahTipe(self):
        self.test_tambahSeri()
        tambah3 = self.gudang.tambahBarang("Kabel", "LAN", "LN01", 23000)
        self.assertEqual(tambah3, "Jenis Lama\nTipe Baru\nSeri Baru")

    def test_tambahJenis(self):
        self.test_tambahTipe()
        tambah4 = self.gudang.tambahBarang("Monitor", "21 Inch", "LG L001", 5100000)
        self.assertEqual(tambah4, "Jenis Baru\nTipe Baru\nSeri Baru")

if __name__ == "__main__":
    unittest.main()


# python testGudang.py
