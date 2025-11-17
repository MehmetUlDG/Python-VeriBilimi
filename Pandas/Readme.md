## IMDB Veri Seti Analiz

### Veri Kaynağı:
 https://developer.imdb.com/non-commercial-datasets

itle.basics.tsv.gz ve title.ratings.tsv.gz dosyalarını https://datasets.imdbws.com/ adresinden
indirin. (TSV, sıkıştırılmış .gz formatındadır.) 

### İçerik:

Pandas_Exercise.ipynb 

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

     pip install (pandas, numpy, matplotlib, seaborn, jupyterlab)


### Kullanım 
  
Jupyter Notebook'u başlat:

    jupyter notebook
####  veya
    jupyter lab

Pandas_Exercise.ipynb dosyasını aç ve hücreleri sırayla çalıştır.

Veri yolu/namespaces farklıysa notebook içindeki data_path değişkenini güncelle.

#### Hızlı Çalıştırma (script olarak)

Notebook'u script'e dönüştürüp çalıştırmak istersen:

    jupyter nbconvert --to script "Pandas_Exercise.ipynb"
    python "Pandas_Exercise.py"

(Not: Notebook'tan script üretildiğinde bazı interaktif hücreler eksik çalışabilir.)

### Değerlendirme
 
  ##### Veri setini analizimizin sonucundaki bulgular şunlardır;
   - Hikayesi güçlü,uzun soluklu veya etkisi yüksek yapımlara yönelmek daha mantıklı bir strateji olarak öne çıkıyor.
   - İzleyici/Eleştirmen en çok dizi ve filmlere olumlu tepki veriyor.
   - Bu ürünler puanlamada daha sürdürülebilir başarı sağlıyor.
   - Zaman içinde etkilerini arttırma potansiyeline sahip.
   - Her yıl artan ilgi nedeni ile talep büyüyerek gidiyor.