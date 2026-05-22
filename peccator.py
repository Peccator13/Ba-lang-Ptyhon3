import random
import os
import pyaudio
import json
import win32com.client
from datetime import datetime
from vosk import Model, KaldiRecognizer, SetLogLevel
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import comtypes


def konuş(metin):
       speaker = win32com.client.Dispatch("SAPI.SpVoice")
       speaker.Speak(metin)

print("online and ready... :) ")
konuş("online and ready... :) ")
print("Welcome Peccator...")
konuş("Welcome Peccator...")
print("Your personal asistant, at your command sir.")
konuş("Your personal asistant, at your command sir.")
print("Complete identity verification...")
konuş("Complete identity verification...")

#giriş seronomisi hazırladık

kullanıcı = "Peccator"
şif = "Jre,13zo"

#kayıtlı kullanıcı bilgileri.
#kayıt usulüyle bir list oluşturup kullanıcıya kayıt yaptırabiliriz.

try:
   SetLogLevel(-1)

   model = Model("vosk-model-en-us-0.22")
except Exception as e:
    print("vosk model is not installed...")
    konuş("vosk model is not installed")

# modeli tanımladık ve çalıştırdık

while True:
    x = input("User:")
    y = input("Password:")
    if ((x == kullanıcı) and (y == şif)):
        print("Welcome Peccator")
        konuş("Welcome Peccator")

        #giriş başarıyla sağlandı

        while True:
            okuma = KaldiRecognizer(model, 16000)
            okuma.SetWords(True)
            okuma.SetPartialWords(True)

            p = pyaudio.PyAudio()
            kayıt = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=4096)
            print("Recording...")

            #ses kaydı başladı

            uyan = ["hey system", "system open"]
            aktif = False

            try:
                while True:
                   data = kayıt.read(1024, exception_on_overflow=False)
                   if okuma.AcceptWaveform(data):
                       metin = json.loads(okuma.Result())["text"]
                       if metin:
                           print(f"dinlendi:, {metin}")
                           if any(kelime in metin for kelime in uyan) and not aktif:
                               aktif = True
                               print("ım ready sir")
                               konuş("ım ready sir")

                           elif aktif:
                               emir = metin
                               if ("hello" in emir) or ("hi" in emir) or ("hey" in emir) or ("selamün aleyküm" in emir):
                                   cevap1 = ["hello peccator", "whatsapp bro", "aleyküm selam habibii"]
                                   z = random.choice(cevap1)
                                   print(z)
                                   konuş(z)





                               elif ("how are you" in emir) or ("what's up" in emir) or ("how it's going" in emir):
                                   cevap2 = ["are you seriously... you asking how a program is doing ha -_-",
                                             "buddy, ı am not a human... ı am a robot, ROBOT"]
                                   z = random.choice(cevap2)
                                   print(z)
                                   konuş(z)


                               elif ("clock" in emir) or ("time" in emir) or ("what time" in emir):
                                   z = str(datetime.now())
                                   print(z)
                                   konuş(z)


                               elif ("stop" in emir) or ("enough" in emir) or ("close" in emir):
                                   print("the systems shuts down...")
                                   konuş("the system shuts down...")
                                   break

                               elif ("calculator" in emir) or ("process" in emir) or ("nobody" in emir) or (
                                       "calc" in emir):
                                   print(" open the calculator...")
                                   konuş("open the calculator")
                                   os.startfile("calc")

                               elif ("disco" in emir) or ("music" in emir) or ("spotify" in emir):
                                   print(" open the spotify...")
                                   konuş("open the spotify")
                                   os.startfile("spotify")

                               elif ("firefox" in emir) or ("fox" in emir) or ("search" in emir):
                                   print(" open the firefox...")
                                   konuş("open the firefox")
                                   os.startfile("firefox")

                               elif ("file" in emir) or ("note" in emir) or ("write" in emir):
                                   print(" open the file and taking notes... ")
                                   konuş("open the file and taking notes")

                                   p = pyaudio.PyAudio()
                                   kayıt = p.open(format=pyaudio.paInt16,
                                                  channels=1,
                                                  rate=16000,
                                                  input=True,
                                                  frames_per_buffer=1024)
                                   print("taking notes...")

                                   kayıtlar = []
                                   for i in range(0, 150):
                                       data = kayıt.read(1024)
                                       kayıtlar.append(data)
                                   kayıt.stop_stream()
                                   kayıt.close()
                                   p.terminate()
                                   print("take a note...")
                                   konuş("take a note")

                                   for data in kayıtlar:
                                       okuma.AcceptWaveform(data)
                                   sonuç = okuma.FinalResult()

                                   metin = json.loads(sonuç)["text"]

                                   with open("metin.txt", "w") as dosya:
                                       dosya.write(metin)

                               elif ("close the computer" in emir) or ("finish" in emir) or (
                                       "shut down the computer" in emir) or ("shut down" in emir):
                                   print("computer shuts down...")
                                   konuş("computer shuts down")
                                   os.system("shutdown /s /t 3")

                               elif ("volume up" in emir) or ("sound up" in emir):
                                   print("volume up...")
                                   konuş("volume up")
                                   devices = AudioUtilities.GetSpeakers()
                                   interface = devices._dev.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL,
                                                                     None)
                                   sesseviye = cast(interface, POINTER(IAudioEndpointVolume))

                                   mevcut_ses = sesseviye.GetMasterVolumeLevelScalar()
                                   yeni_ses = mevcut_ses + 0.1  # %10 ekle
                                   sesseviye.SetMasterVolumeLevelScalar(yeni_ses, None)
                                   yüzdeses = yeni_ses * 100
                                   print(str(int(yüzdeses)))
                                   konuş(str(int(yüzdeses)))

                               elif ("volume down" in emir) or ("sound down" in emir):
                                   print("volume down...")
                                   konuş("volume down")
                                   devices = AudioUtilities.GetSpeakers()
                                   interface = devices._dev.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL,
                                                                     None)
                                   sesseviye = cast(interface, POINTER(IAudioEndpointVolume))

                                   mevcut_ses = sesseviye.GetMasterVolumeLevelScalar()
                                   yeni_ses = mevcut_ses - 0.1  # %10 azalt
                                   sesseviye.SetMasterVolumeLevelScalar(yeni_ses, None)
                                   yüzdeses = yeni_ses * 100
                                   print(str(int(yüzdeses)))
                                   konuş(str(int(yüzdeses)))

                               elif ("get around" in emir) or ("find" in emir) or ("program" in emir):
                                    program_files = os.environ["PROGRAMFILES"]
                                    for root, dirs, files in os.walk(program_files):

                                        for dosya in files:

                                            if dosya.endswith(".exe") and emir in dosya.lower():
                                                os.startfile(os.path.join(root, dosya))
                                                break







            except Exception as e:
                print(e)
                konuş("the sound system is broken")


    else:
        print("Your information is incorrect...")
        konuş("Your information is incorrect...")





