def unicornBestie(func):
    def wrapper(*args, **kwargs):
        print("\n🦄✨ Unicorn Pinky: 'Hey Bestie, ayo kita buat pelangi bersama!'")
        print("🦄✨ Unicorn Sparkle: 'Yuk, Pinky! Siapkan warna-warna magis kita!'")
        print("🌈🌈 Pelangi mulai terbentuk... Woosh! 🥹✨✨")
        hasil = func(*args, **kwargs)
        print("🌟🦄 Pinky: 'We did it! Magic complete!'")
        print("🦄🌟 Sparkle: 'Harimu akan penuh pelangi dan cinta! Sampai jumpa lagi! 🌸🌈'\n")
        return hasil
    return wrapper

@unicornBestie
def kasiKabar(kabar):
    print(f"\n💌 Kabar: {kabar}")

kasiKabar("Python membuat hidupku penuh warna dan kegembiraan!\n")
