def capitalLast(str):
    katakata = str.split()
    hasil = []
    for kata in katakata:
        if len(kata) > 1:
            hasil.append(kata[:-1] + kata[-1].upper())
        else:
            hasil.append(kata.upper())
    return '\n'.join(hasil)
 
def capitalOdd(str):
    katakata = str.split()
    hasil = []
    for kata in katakata:
        kataBaru = ""
        for i in range(len(kata)):
            if i % 2 == 0:
                kataBaru += kata[i].upper()
            else:
                kataBaru += kata[i].lower()
        hasil.append(kataBaru)
    return '\n'.join(hasil)
 
def HitungVokal(str):
    vokal = "aeiou"
    jumlah = 0
    for char in str.lower():
        if char in vokal:
            jumlah += 1
    return jumlah
 
 
text = "saya suka makan"
print("Strategy1")
print(capitalLast(text))
print()
 
print("Strategy2")
print(capitalOdd(text))
print()
 
print("Decorator")
text = "saya suka makan keju"
print(capitalLast(text))
print()
 
print(capitalOdd(text))
print()
 
vowelCount = HitungVokal(text)
print(f"Jumlah huruf Vocal : {vowelCount}")