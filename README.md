# Proje içeriği
### Web Scraping:
* URL, header, summary, text, img_url_list, publish_date ve update_date sütunları
için belirlenmiş haber sitesinden veri çekme işlemi.
* Eş zamanlı veri çekmek için requests ve beautifulsoup kütüphanelerini
kullanma.
* Çekilen veriyi MongoDB için yapılandırma.
### Veri Analizi:
* Metin sütununa odaklanarak çekilen veriler üzerinde analiz yapma işlemi.
* Metin sütunundaki en çok kullanılan kelimeleri belirleme ve sayma.
### Kelime Frekansı Grafiği :
* Metin sütunundaki en çok kullanılan kelimelerin sayısını gösteren bir grafik (ör.
çubuk grafik, kelime bulutu) oluşturma.
### MongoDB Entegrasyonu :
* pymongo kullanarak MongoDB veritabanına eş zamanlı bağlantılar için
işlevler/sınıflar oluşturma.
* URL, header, summary, text, img_url_list, publish_date ve update_date sütunları
için veritabanını oluşturma.
### Log Yönetimi :
* Loglama işlevselliği ekleyerek, veri çekme, analiz ve veritabanı işlemleri
sırasında olayları, hataları ve bilgileri loglama.
İzleme ve hata ayıklama amaçları için önemli olayları, istisnaları ve kritik bilgileri
kaydetme.
### Veri Manipülasyonu:
* update_date kolonuna göre gruplanmış verileri gösterme.
### Threading Kontrolü :
* Veri çekme, analiz ve veritabanı etkileşimi süreçlerine threadingpool
kütüphanesini entegre etme.
* Python'un threadingpool kütüphanesiyle eş zamanlı görevleri yönetme,
senkronizasyon ve thread güvenliği sağlama.
### Python Yetkinliği :
* PEP 8 kurallarına uygun temiz, okunabilir ve iyi açıklanmış kodlar yazma.
* Anlamlı değişken/fonksiyon isimleri kullanma ve hata yönetimi tekniklerini
uygulama.
### Dökümantasyon :
* README dosyasına kurulum talimatları, bağımlılıklar ve analiz edilen veri,
kelime frekansı grafiği ve log bilgilerinin nasıl anlaşılacağı konusunda açıklamalar
ekleme.
* Fonksiyonlar ve sınıflar için dokümantasyon içeren docstrings kullanma.
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
