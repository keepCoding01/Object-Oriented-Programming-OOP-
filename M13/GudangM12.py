class Gudang:
    def __init__(self):
        self.data = {}

    def tambahBarang(self, jenis, tipe, seri, harga):
        if jenis not in self.data:
            self.data[jenis] = {}
            self.data[jenis][tipe] = {seri: harga}
            return "Jenis Baru\nTipe Baru\nSeri Baru"
        elif tipe not in self.data[jenis]:
            self.data[jenis][tipe] = {seri: harga}
            return "Jenis Lama\nTipe Baru\nSeri Baru"
        elif seri not in self.data[jenis][tipe]:
            self.data[jenis][tipe][seri] = harga
            return "Jenis Lama\nTipe Lama\nSeri Baru"
        else:
            return "Barang sudah ada!"
