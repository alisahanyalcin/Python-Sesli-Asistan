#Gerekli Kütüphanelerimizi Dahil ediyoruz
from datetime import datetime
from gtts import gTTS
from playsound import playsound
"""
@author: alisahanyalcin
"""
import speech_recognition as sr
import webbrowser
import random
import os


r = sr.Recognizer() #sesleri Tanımamız için fonksiyonu çağırıp değişkene atıyoruz

#Fonksiyonlar oluşturup gerektiği yerde çağırmamız/kullanmamız daha derli bir yapı oluşturacağı için projemizi fonksiyonel kodluyoruz
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.Recognizer:
            speak('sistem çalışmıyor')
        return voice

#sorulan sorulara vereceği cevapları belirliyoruz
#yeni bir cevap eklemek istiyorsanız if 'söyleyeceğiniz şey' in voice speak('programın bize söyleyeceği şey') şeklinde tanımlamanız yeterli olacaktır
def response(voice):
    if 'nasılsın' in voice:
        speak('iyiyim siz nasılsınız')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:#googlede arama yaptırıp arama sayfasını açtırıyoruz
        search = record('ne aramak istiyorsunuz')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
    if 'kapan' in voice:
        speak('görüşürüz')
        exit() #kapan dediğimizde döngüyü kırıp çıkması için exit() fonksiyonunu kullandık

#bir üst satırlarda response() fonksiyonumuzdan dönen değerleri sese dönüştürmek için gtts (google text to sound) kütüphanemizi kullanıyoruz
#işlem sonunda yer kaplamaması adına siliyoruz ad verirken random kullanma sebebimiz ise silme işleminde herhangi bir sorun yaşanırsa bir sonraki söyleyeceği şeyde sorun olmasın isimleri çakışmasın
def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

#program ilk çalıştığında çalışacak kodlar
speak('Nasıl yardımcı olabilirim') #açılışta söyleceği şey
#neden döngü kullandık?; örneğin saat kaç diye sorduğumuzda saati söylüyor burada bir sorun yok ama işlemi bitirip kapanıyor tekrar soru sormamız için tekrar başlatmamız lazım bu yüzden döngüye alıp işlemlerimizi bu şekilde gerçekleştiriyoruz
while True:
    voice = record()
    print(voice)
    response(voice)
