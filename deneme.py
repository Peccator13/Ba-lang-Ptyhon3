print("program girişi yapmanız gerekmektedir...")
kullanıcıayse = input("'kullanıcı adı' belirleyiniz:")
sifreayse = input("'şifre' belirleyiniz:")
print("kaydınız tamamlanıyor...")
print("lütfen bekleyin")
for i in range(0,100,5):
    print(i+5)
print("program kaydınız tamamlandı :) HOŞGELDİNİZ")
while True:
    cevap = input("giriş yapmak ister misiniz? (evet/hayır):")
    if cevap == "evet":
        kullanıcı = input ("kullaıcı adınızı giriniz:")
        şifre = input ("şifrenizi giriniz:")
        if ((kullanıcı == kullanıcıayse) and (şifre == sifreayse)):
            print("sisteme başarıyla giriş yaptınız")
            print("selamün aleykümm, nasılsınn?")
            nassın = input()
            if "iyi" in nassın:
                print("sen iyiysen bizde iyiyiizzz, Allah iyilik versin")
            elif "idare" in nassın and "iyi" in nassın:
                print("idare mi?? hmmm bir sorun yok inşallah")
            elif "kötü" in nassın:
                print("nasıl kötü yaw... seni kötü eden deyyus kimdir -_-")
            elif "bilmiyorum" in nassın:
                print("öğren o haldee ve iyi olmaya bakk :)")
            elif "elhamdülillah" in nassın and "iyi" in nassın:
                print("şükür şükür hep iyi ol inşallaahhh")
            elif "çok kötü" in nassın:
                print("çok mu kötü... dinlemeye her zaman hazırım gel anlat.")
            else:
                print("bu yazının çıkmaması dileğiyle :I")
            print("programı kapatmak için enter'a basman yeterli olacaktır")
            input()
            break
        elif ((kullanıcı != kullanıcıayse) and (şifre == sifreayse)):
            print("kullanıcı adınızı unutmuş gibisiniz")
        elif ((kullanıcı == kullanıcıayse) and (şifre != sifreayse)):
            print("şifrenizi mi unuttunuz?")
            print("değiştirmek ister misiniz? (E/H)")
            değiştirecekmi = input()
            if değiştirecekmi == "E":
                yenişifre = input("yeni şifrenizi giriniz")
                sifreayse = yenişifre
            elif değiştirecekmi == "H":
                print("giriş yapabilirsiniz")

    else:
        print("Hoşça kalın")
        break




