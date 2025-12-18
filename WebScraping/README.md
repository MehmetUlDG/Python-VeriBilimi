## Sahibinden Web Scarping Veri Seti Analiz

### Veri Kaynağı:
  https://www.sahibinden.com/kiralik/isparta-merkez 

### İçerik:

Sahibinden_data_analysis.ipynb 
web_scraping.ipynb(Csv formatına dönüştürüp kullandığımız veri setini oluşturan script dosyası)
data/ — (opsiyonel) kullanılacak ham/veri dosyaları (.csv)

README.md — Bu dosya

### Kurulum:

Repo'yu klonla (veya notebook dosyasını bulunduğun yere kopyala):

     git clone <REPO_URL>
      cd <repo_klasoru>

Sanal ortam oluştur (conda veya venv önerilir):

#### conda örneği
     conda create -n imdb_data python=3.10 -y
     conda activate imdb_data

#### veya venv örneği
    python -m venv .venv
#### Windows PowerShell
    .\.venv\Scripts\Activate.ps1
#### Git Bash / Linux / Mac
    source .venv/bin/activate

Gereksinimleri yükle:

     pip install (pandas, numpy, matplotlib, seaborn, selenium,jupyterlab)


### Kullanım 
  
Jupyter Notebook'u başlat:

    jupyter notebook
####  veya
    jupyter lab

web_scraping.ipynb dosyasını aç ve hücreleri sırayla çalıştır.

Sahibinden_data_analysis.ipynb dosyasını aç ve hücreleri sırası ile çalıştır.

Veri yolu/namespaces farklıysa notebook içindeki data_path değişkenini güncelle.

#### Hızlı Çalıştırma (script olarak)

Notebook'u script'e dönüştürüp çalıştırmak istersen:

    jupyter nbconvert --to script "Sahibinden_data_analysis.ipynb"
    python "Sahibinden_data_analysis.ipynb"

(Not: Notebook'tan script üretildiğinde bazı interaktif hücreler eksik çalışabilir.)

### Değerlendirme
 
  ##### Veri setini analizimizin sonucundaki bulgular şunlardır;
   - Piyasanın genel durumu ortalama sizi yanıltmasın: Isparta ili genelindeki ev kiralarının
ortalama değeri 14.986 TL ancak medyan değerimiz 13.000 TL bu da ortalamayı yükselten
(villa,lüks daire,vb) meskenlerin de veri setimizde olduğuna işaret eder.
- Arzın kalbi nerde atıyor: Isparta Merkez genelinde yaptığımız analizde en çok ilanın Fatih
ve Çünür mahellerinde olduğunu görüyoruz. Fatih Mahallesi: 154 ilanla lider. Şehrin
kalabalık, hareketli ve sirkülasyonun en bol olduğu yer. Çünür Mahallesi: 143 ilanla
ensesinde. Burası üniversiteye yakınlığı ve yeni yapılaşmasıyla "Yeni Isparta" diyebiliriz.
- Ev tipleri aileler ve öğrencilier arasında sıkışan emlak pazarı: En çok ilan 3+1 daireler için
verilmiş. (yaklaşık 290-300 ilan) Bu durum bize Isparta ilinin hala aile yapı stokunun
olduğunu gösteriyor.Ardından gelen 1+1 daireler (yaklaşık 230-240 ilan) Isparta’nın bir
öğrenci şehri olduğunu gösteriyor.
- Fiyatlandırma Stratejisi: "Oda Sayısı Çarpanı": Veri setimizdeki verilere göre oda sayısının
kira fiyatlarına doğrusal bir şekilde ilişkiye sahip olduğunu görüyoruz.Örneğin; 1+0 (Stüdyo)
dairelerde ortalama 8.000 TL bandında iken 3+1 dairelerde fiyat bir anda 20.000 TL
seviyesine fırlıyor.Burada ilgi çeken bir konu ise şu; Çok ilginç bir şekilde 1+1 ve 2+1 daire
kiralarının birbirine yakın ve 12.000 - 14.000 TL bandında olması bize talep bakımından 1+1
ve 2+1 dairelerin pek beligin bir ücret farkı oluşturmadığını görüyoruz.
- Metrekare ve Fiyat İlişkisi: 50-100 m² arasında fiyatlar dalgalı ama stabil artıyor. Ancak
200 m² üzerine çıkıldığında fiyatlar çok sert yükseliyor (Lineer bir artış). Bu durumdan küçük
metrekareli dairelerin fiyatını metrekare değil eşyalı,konumu vb. durumlar daha çok
etkiliyor.Büyük metrekareli dairelerde ise her bir metrekare için ekstra para ödüyorsun.
- İlanı Ne Zaman Aramalısın :Elimizdeki grafikleri inceledğimizde şöyle şaşırtıcı bir sonuçla
karşılaşıyoruz; Ayın başı (1'i ile 5'i arası) ilan girişlerinde patlama var. Ayın 20'sinden sonra
piyasa durgunlaşıyor.Bu durum ise bize ay başı kiralık daire aramanın bize daha bol bir
seçenek sunacağını gösteriyor.
- Sihirli Sözcük “Sahibinden”: En çok tekrar eden kelimelerde "Isparta", "Kiralık"
kelimelerinden hemen sonra ne geliyor? "Sahibinden".Bu kelime boş bir anlam ifade etmiyor
çünkü bu piyasada mülk sahipleri komisyon vermemek için kendileri ilan vermeyi seviyor.
Ancak “emlaktan” kelimesinin yüzdesi de oldukça yüksek. Yani piyasa %50-%50 bölünmüş

durumda. 
