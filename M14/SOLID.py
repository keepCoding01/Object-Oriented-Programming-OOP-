from abc import ABC, abstractmethod

def cekNama (nama):
    for kar in nama :
        if (not(ord("A") <= ord(kar) <= ord("Z") or ord("a") <= ord(kar) <= ord("z") or kar == " ")):
            return False
    return True

class absHasil(ABC):
    @abstractmethod
    def hasil():
        pass

class simpanData(absHasil):
    def hasil(nama):
        if(cekNama(nama)):
            print(f"{nama} berhasil disimpan ke dalam data")
        else :
            print("Mohon maaf nama tidak bisa disimpan ya....!!!")

class loginNama(absHasil):
    def hasil(nama):
        if (cekNama(nama)):
            print(f'{nama} sesuai dengan ketentuan yang ada dan bisa login\n')
        else :
            print("Mohon maaf nama tidak sesuai, sehingga Anda tidak bisa login.\n")


if __name__ == '__main__':
    nama = "Apriyanto Halim"
    for proses in absHasil.__subclasses__():
        proses.hasil(nama)

    nama = "S1@p@ y@ng t@hu"
    for proses in absHasil.__subclasses__():
        proses.hasil(nama)

    nama = "AnEh sAjA sIh"
    for proses in absHasil.__subclasses__():
        proses.hasil(nama)
