class Cookies:
    _COOKIES = {}

    def __init__(self):
        pass

class WebsiteMIKA(Cookies):
    def __init__(self, **data):
        super().__init__() 
        self._COOKIES.update(data)  

    def cetakCookies(self):
        for name, data in self._COOKIES.items():
            print(f"{name}: {data}")

    def cekData(self, data):
        return self._COOKIES.get(data, False) 

if __name__ == "__main__":
    login = WebsiteMIKA(login=True, uid="apriyanto.halim")
    print("Cookies Awal")
    login.cetakCookies()

    if login.cekData("login"):
        home = WebsiteMIKA(halaman="home")
        print("\nCookies Berikutnya")
        home.cetakCookies()

    if login.cekData("login"):
        profile = WebsiteMIKA(halaman="profile")
        print("\nCookies Terakhir")
        profile.cetakCookies()
