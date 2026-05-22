import math as m

print("Hoşgeldiniz")
print("Hesap makinesi çalışıyor...")


def topla(sayıx, sayıy):
    return sayıx + sayıy


def çıkar(sayıx, sayıy):
    return sayıx - sayıy


def çarp(sayıx, sayıy):
    return sayıx * sayıy


def bölme(sayıx, sayıy):
    return sayıx / sayıy


def üçgen(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        s = (a + b + c) / 2
        return m.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return "Bir üçgen değildir..."


def dörtgen(a, b, c, d):
    if not (a < b + c + d and b < a + c + d and c < a + b + d and d < a + b + c):
        return "Hata: Bu kenarlarla kapalı bir dörtgen oluşturulamaz!"
    if a == b == c == d:
        return a * a
    elif (a == c and b == d) or (a == b and c == d) or (a == d and b == c):
        return a * b
    else:
        print("Bu bir düzensiz dörtgendir, çevre hesaplanıyor...")
        return a + b + c + d


# Programın ana döngüsü
while True:
    print("\n--- YENİ İŞLEM ---")
    print("Ne yapmak istersiniz? (Çıkış için 'Q' tuşuna basın)")
    durum = input("İşlem mi (İ), Alan hesaplama mı (A)?: ").upper()

    if durum == "Q":
        print("Programdan çıkılıyor...")
        break

    if durum == "İ":
        işlem = input("Hangi işlem? (+, -, x, /): ")
        if işlem in ["+", "-", "x", "/"]:
            sayı1 = int(input("İlk sayı: "))
            sayı2 = int(input("İkinci sayı: "))

            if işlem == "+":
                print("Sonuç:", topla(sayı1, sayı2))
            elif işlem == "-":
                print("Sonuç:", çıkar(sayı1, sayı2))
            elif işlem == "x":
                print("Sonuç:", çarp(sayı1, sayı2))
            elif işlem == "/":
                if sayı2 == 0:
                    print("Hata: Bir sayı 0'a bölünemez!")
                else:
                    print("Sonuç:", bölme(sayı1, sayı2))
        else:
            print("Geçersiz işlem seçtiniz.")

    elif durum == "A":
        alanH = input("Üçgen mi, Dörtgen mi?: ").lower()
        if alanH == "üçgen":
            k1 = int(input("1. Kenar: "))
            k2 = int(input("2. Kenar: "))
            k3 = int(input("3. Kenar: "))
            print("Sonuç:", üçgen(k1, k2, k3))
        elif alanH == "dörtgen":
            k1 = int(input("1. Kenar: "))
            k2 = int(input("2. Kenar: "))
            k3 = int(input("3. Kenar: "))
            k4 = int(input("4. Kenar: "))
            print("Sonuç:", dörtgen(k1, k2, k3, k4))
        else:
            print("Lütfen 'üçgen' veya 'dörtgen' yazın.")

    else:
        print("Lütfen geçerli bir seçim (İ, A veya Q) yapın.")