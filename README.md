# Proje içeriği
Web Scraping:
- [x] URL, header, summary, text, img_url_list, publish_date ve update_date sütunları
için belirlenmiş haber sitesinden veri çekme işlemi.
- [x] Eş zamanlı veri çekmek için requests ve beautifulsoup kütüphanelerini
kullanma.
- [x] Çekilen veriyi MongoDB için yapılandırma.
 Veri Analizi:
- [x] Metin sütununa odaklanarak çekilen veriler üzerinde analiz yapma işlemi.
- [x] Metin sütunundaki en çok kullanılan kelimeleri belirleme ve sayma.
Kelime Frekansı Grafiği :
- [x] Metin sütunundaki en çok kullanılan kelimelerin sayısını gösteren bir grafik (ör.
çubuk grafik, kelime bulutu) oluşturma.
MongoDB Entegrasyonu :
- [x] pymongo kullanarak MongoDB veritabanına eş zamanlı bağlantılar için
işlevler/sınıflar oluşturma.
- [x]  URL, header, summary, text, img_url_list, publish_date ve update_date sütunları
için veritabanını oluşturma.
Log Yönetimi :
- [x] Loglama işlevselliği ekleyerek, veri çekme, analiz ve veritabanı işlemleri
sırasında olayları, hataları ve bilgileri loglama.
İzleme ve hata ayıklama amaçları için önemli olayları, istisnaları ve kritik bilgileri
kaydetme.
 Veri Manipülasyonu:
* update_date kolonuna göre gruplanmış verileri gösterme.
Threading Kontrolü :
- [x] Veri çekme, analiz ve veritabanı etkileşimi süreçlerine threadingpool
kütüphanesini entegre etme. 
- [x] Python'un threadingpool kütüphanesiyle eş zamanlı görevleri yönetme,
senkronizasyon ve thread güvenliği sağlama.
Python Yetkinliği :
- [x] PEP 8 kurallarına uygun temiz, okunabilir ve iyi açıklanmış kodlar yazma.
- [x] Anlamlı değişken/fonksiyon isimleri kullanma ve hata yönetimi tekniklerini
uygulama.
Dökümantasyon :
* README dosyasına kurulum talimatları, bağımlılıklar ve analiz edilen veri,
kelime frekansı grafiği ve log bilgilerinin nasıl anlaşılacağı konusunda açıklamalar
ekleme.
- [x] Fonksiyonlar ve sınıflar için dokümantasyon içeren docstrings kullanma.
### Ölçeklenebilirlik ve Verimlilik :
* Veri çekme hızı, kaç veri çekildiği, verinin çekilme tarihi, veri çekilirken kaç
başarılı kaç başarısız istek yapıldığını sunma.
* Bu verimlilik verilerinin MongoDB yeni açılan koleksiyona kaydedilmesi

# Kullanılan Teknolojiler
* Python programlama dili
* nltk
* matplotlib
* wordcloud 
* nltk
* requests
* bs4
# Kurulum
* git clone https://github.com/mertorelio/news-scraper/tree/master
* pip install -r requirements.txt
* python main.py

# Yöntem
## Threading
*  Projede kullanılan thread yönetimi ThreadPoolExecutor kullanılarak gerçekleştirilmiştir. Aynı zamandan çok fazla request atılmaması için önce kullanılcak urller eşit parçalara ayırılıp (25), her bir parça
içindeki elemanların tek bir seferde threadler ile çalıştırılacak ve verileri kaydedecek şekilde düzenlenmiştir. Her bir parçanın işlemi bittikten sonra 5 saniyelik bir bekleme süresi eklenmiş ve siteye yoğun istek gönderimi seyreltilmiştir.
