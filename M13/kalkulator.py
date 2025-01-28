class kalku:
    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        if a > b:
            return a - b
        else:
            return b - a

    @staticmethod
    def kali(a, b):
        return a * b

    @staticmethod
    def bagi(a, b):
        if b == 0:
            raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
        return a / b
