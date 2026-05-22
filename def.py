def cevap_anahtarı (cevaplar):
    print ("cevaplarınız değerlendiriliyor...")
    print ("cevaplarınız değerlendirildi")
    if cevaplar == 10:
        print("OOOO BU BAŞARI NE HOCAM MAŞALLAH MAŞALLAHHH, TÜ TÜ TÜ :)")
    elif cevaplar >= 5:
        print ("gayet başarılısınız")
    else:
        print("daha çok çalışın")
doğru_cevaplar = 0
print("sınava hoşgeldiniz")
print("kurallar:")
print("kopya halinde sınavınız iptal olur")
print("1-) 2+2 = ? ")
cevap1 = int(input("cevabınız:"))
if cevap1 == 4:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("2-) 7 x 5 = ?")
cevap2 = int(input("cevabınız:"))
if cevap2 == 35:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("3-) 4+6/2 = ?")
cevap3 = int(input("cevabınız:"))
if cevap3 == 7:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("4-) (√9+√25)/(√49-6) = ?")
cevap4 = int(input("cevabınız:"))
if cevap4 == 8:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("5-) √144+18/3x(5-2) = ?")
cevap5 = int(input("cevabınız:"))
if cevap5 == 30:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("6-) √196+24/3x(8-√16)² = ?")
cevap6 = int(input("cevabınız:"))
if cevap6 == 142:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("7-) (√225+3²x(10−√25))÷2+4 = ? ")
cevap7 = int(input("cevabınız:"))
if cevap7 == 29:
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış:")
print("8-) (√256−2³)²/4+18÷(3x(√36−1)) = ?")
cevap8 = input("cevabınız:")
if cevap8 == "17.2":
    print("doğru!")
    doğru_cevaplar += 1
elif cevap8 == "86/5":
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("9-) [(√324−3²)³/9+4²]/(2+√16) = ?")
cevap9 = input("cevabınız:")
if cevap9 == "97/6":
    print("doğru!")
    doğru_cevaplar += 1
elif cevap9 == "16.17":
    print ("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("10-) {[(√400−5²)²+3³x(√81−2)]/4}−√49 = ?")
cevap10 = input("cevabınız:")
if cevap10 == "93/2":
    print("doğru!")
    doğru_cevaplar += 1
elif cevap10 == "46.5":
    print("doğru!")
    doğru_cevaplar += 1
else:
    print("yanlış!")
print("tebriklerrr sınavı başarıyla tamamladınız.")
print("cevap durumlarınız toplanıyor...")
cevap_anahtarı(doğru_cevaplar)
print("programı kapatmak için ne yapman gerektiğini biliyosun ;I ")
input()