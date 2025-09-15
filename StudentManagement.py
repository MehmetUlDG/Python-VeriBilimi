# 1. Değişkenler ve Veri Tipleri
sinif_adi= "11-C"
mevcut_ogrenci_sayisi=0
ortalama_basari_puanı=0.0
sinif_aktif=True

# 2. Öğrenci Bilgileri (dict ve list)
ogrenciler=[]

# 3. Operatörler ve String İşlemleri
def ogrenci_ekle():
   global mevcut_ogrenci_sayisi,ortalama_basari_puanı

   isim=input("Lütfen isminizi giriniz: ").strip().upper()
   yas=int(input("Lütfen yaşınızı giriniz: "))
   notu=int(input("Lütfen puanınızı giriniz: ")) 

# Geçti/Kaldı Kontrolu
   durum ="Geçti" if notu>=60 else "Kaldı"
   print(f"{isim}  {durum}!")

   yeni_ogrenci= {
     "isim":isim,
     "yas":yas,
     "not":notu
   }
    
ogrenciler.append(yeni_ogrenci)
mevcut_ogrenci_sayisi+=1
toplam_not=sum(ogrenci["not"] for ogrenci in ogrenciler)
ortalama_basari_puanı=toplam_not/mevcut_ogrenci_sayisi

print(f"{isim} öğrenci başarı ile eklendi.")



def ogrenci_listele():
  if not ogrenciler:
    print("Kayıtlı öğrenci yok!")
    return
  
  print("\n==Ögrenci Listesi==")
for i,ogrenci in enumerate(ogrenciler,1):
  durum= "Geçti" if ogrenci["not"]>=60 else "Kaldı"

print(f"{isim} adlı öğrenci {yas} yaşındadır.Notu: {notu} vaziyet: {durum}")

def ogrenci_ara():
  if not ogrenciler:
   print("Öğrenci yok!")
  return  
  
arama_terimi=input("Hangi öğrenciyi arıyorsunuz").strip().upper() 
bulunan_ogrenciler=[]

for ogrenci in ogrenciler:
 if arama_terimi in ogrenci["isim"]:
   bulunan_ogrenciler.append(ogrenci)

if bulunan_ogrenciler: 
  print(f"{arama_terimi} ile bağıntılı sonuçlar")
for i,ogrenci in enumerate(bulunan_ogrenciler,1):
  durum="Geçti" if ogrenci["not"] >= 60 else "Kaldı"

  print(f"{i}. ad: {isim} yas: {yas} not: {notu} durum: {durum}")

else:
  print("ogrenci bulunamadı")


def istatistikleri_goster():
  
  if not ogrenciler:
    print("Öğrenci yok veya bulunamadı!")
 
notlar=[ogrenci["not"] for ogrenci in ogrenciler ]
ort=sum(notlar)/len(notlar)
en_yuksek=max(notlar)
en_dusuk=min(notlar)

gecen_ogrenciler=[ogrenci["isim"] for ogrenci in ogrenciler if ogrenci["not"]>=60]
kareler=[notu**2 for notu in notlar] 

print("\n--- İstatistikler ---")
print(f"Sınıf Adı: {sinif_adi}")
print(f"Öğrenci Sayısı: {mevcut_ogrenci_sayisi}")
print(f"Ortalama Başarı Puanı: {ortalama_basari_puani:.2f}")
print(f"Sınıf Durumu: {'Aktif' if sinif_aktif else 'Pasif'}")
print(f"En Yüksek Not: {en_yuksek}")
print(f"En Düşük Not: {en_dusuk}")
print(f"Geçen Öğrenci Sayısı: {len(gecen_ogrenciler)}")
print(f"Geçen Öğrenciler: {', '.join(gecen_ogrenciler)}")
print(f"Not Kareleri: {not_kareleri}")


def benzersiz_isimler():
  if not ogrenciler:
    print("Öğrenci yok veya bulunamadı!")
  return

isimler=set(ogrenci["isim"] for ogrenci in ogrenciler )
print(f"\nBenzersiz İsimler: {isimler} Toplam Adedi {len(isimler)}")

def main(): 
 while True :

        print("\n--- Öğrenci Yönetim Sistemi ---")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Listele")
        print("3. Öğrenci Ara")
        print("4. İstatistikler")
        print("5. Benzersiz İsimleri Göster")
        print("6. Çıkış")

        secim=int(input("Lütfen seçiminizi yapınız(1-6)"))

        if(secim==1):
          ogrenci_ekle()
        
        elif(secim==2):
          ogrenci_listele()

        elif(secim==3):
          ogrenci_ara()

        elif(secim==4):
          istatistikleri_goster()
         
        elif(secim==5):
          benzersiz_isimler()
      
        elif(secim==6):
         print("Çıkış yapılıyor...")
         break

        else:
         print("Hatalı tuşlama.Lütfen 1-6 arası bir sayı tuşlayın.")
         continue


        if __name__=="__main__":
         main()