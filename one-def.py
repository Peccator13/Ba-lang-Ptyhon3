şifrex = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7",
          "h": "8", "ı": "9", "j": "0", "k": "10", "l": "11", "m": "12", "n": "13", "o": "14",
          "p": "15", "r": "16", "s": "17", "t": "18", "u": "19", "v": "20", "w": "21", "x": "22",
          "y": "23", "z": "24", "ç": "25", "ğ": "26", "i": "27", "ö": "28", "ş": "29", "ü": "30",}
rakamlar = {"1": "31", "2":"32", "3":"33", "4":"34",
            "5":"35", "6":"36", "7":"37", "8":"38", "9":"39", "0":"40", " ":"00"}
şifrex.update(rakamlar)
şifrey = {str(sayı): harf for harf, sayı in şifrex.items()}
for harf, sayı in şifrex.items():
    şifrey[str(sayı)] = harf
def şifreleme (mesaj):
    açıkmesaj = ""
    mesaj = mesaj.lower()
    for karakter in mesaj:
        if karakter in şifrex:
            açıkmesaj = açıkmesaj + str(şifrex[karakter]) + "-"
        else:
            açıkmesaj = açıkmesaj + karakter
    return açıkmesaj
def çözüm (gönderilen):
    şifrem = ""
    parçalar = gönderilen.split("-")
    gönderilen = gönderilen.lower()
    for sayılar in parçalar:
        if sayılar in şifrey:
            şifrem = şifrem + str(şifrey[sayılar])
        elif sayılar == "":
            continue
        else:
            şifrem = şifrem + sayılar
    return şifrem

print ("Hoşgeldiniz")

while True:
    x = input("mesajı giriniz:")
    şifrelimesaj = şifreleme(x)
    print("\n [giden mesaj]:", şifrelimesaj)

    çözülmüşmesaj = çözüm(şifrelimesaj)
    print("\n [gelen mesaj]:", çözülmüşmesaj)
    if x == "çıkış":
        break
    print("iyi eğlenceler, çıkış yapmak için 'çıkış' yazmanız yeterli")

