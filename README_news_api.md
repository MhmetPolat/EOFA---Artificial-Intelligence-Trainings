# Kullanım

### 1. Tüm Haberleri Getirme (READ - GET)

get_all_news()

Tüm haberleri JSON formatında döndürür.

### 2. Başlık İçeriğine Göre Haber Getirme

get_news_by_title("kelime")

Belirtilen kelimeyi içeren başlıklara sahip haberleri getirir.

### 3. Belirli Bir Kullanıcının Haberlerini Getirme

get_news_by_user(3)

Belirtilen userId değerine sahip haberleri getirir.

### 4. Yeni Haber Ekleme (CREATE - POST)

create_news("Başlık", "İçerik", 1)

Yeni bir haber oluşturur ve eklenen haberi JSON formatında döndürür.

### 5. Haberi Güncelleme (UPDATE - PUT)

update_news(1, "Yeni Başlık", "Yeni İçerik")

Belirtilen haber ID’sini günceller.

### 6. Haberi Silme (DELETE)

delete_news(1)

Belirtilen haber ID’sine sahip haberi siler.

# Projeyi Çalıştırma

Terminal veya komut satırında aşağıdaki komutları çalıştırarak news_api.py dosyanızı çalıştırabilirsiniz:

python news_api.py

Bu komut, tüm CRUD işlemlerini sırayla çalıştıracaktır.
