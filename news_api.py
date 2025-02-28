import requests
from pprint import pprint

# API URL
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Tüm Haberleri Getirme (READ - GET)
def get_all_news():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Bağlantı hatası: {e}"}

# Başlık İçeriğine Göre Haber Getirme
def get_news_by_title(title_substring):
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        all_news = response.json()
        return [news for news in all_news if title_substring.lower() in news['title'].lower()]
    except requests.exceptions.RequestException as e:
        return {"error": f"Bağlantı hatası: {e}"}

# User ID'ye Göre Haber Getirme
def get_news_by_user(user_id):
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        all_news = response.json()
        return [news for news in all_news if news['userId'] == user_id]
    except requests.exceptions.RequestException as e:
        return {"error": f"Bağlantı hatası: {e}"}

# Yeni Haber Ekleme (CREATE)
def create_news(title, body, user_id):
    new_news = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.post(BASE_URL, json=new_news)
        response.raise_for_status()
        return {"message": "Yeni haber başarıyla eklendi!", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": f"Haber eklenemedi: {e}"}

# Haberi Güncelleme (UPDATE)
def update_news(news_id, new_title, new_body):
    updated_news = {
        "title": new_title,
        "body": new_body
    }
    try:
        response = requests.put(f"{BASE_URL}/{news_id}", json=updated_news)
        if response.status_code in [200, 204]:
            return {"message": "Haber başarıyla güncellendi!", "data": response.json()}
        else:
            return {"error": "Haberi güncellerken bir hata oluştu!"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Hata oluştu: {e}"}

# Haberi Silme (DELETE)
def delete_news(news_id):
    try:
        response = requests.delete(f"{BASE_URL}/{news_id}")
        if response.status_code in [200, 204]:
            return {"message": f"Haber {news_id} başarıyla silindi."}
        else:
            return {"error": "Silme işlemi başarısız!"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Hata oluştu: {e}"}

# CRUD Fonksiyonlarını Çalıştır
if __name__ == "__main__":
    print("\n🔹 Tüm Haberler:")
    pprint(get_all_news())

    print("\n🔹 Başlık İçeriğine Göre Haberler ('ut' içerenler):")
    pprint(get_news_by_title("ut"))

    print("\n🔹 User ID'ye Göre Haberler (User ID = 3):")
    pprint(get_news_by_user(3))

    print("\n🔹 Yeni Haber Ekleniyor...")
    new_news = create_news("Yeni Teknoloji", "Python ile REST API Kullanımı", 1)
    pprint(new_news)

    if "data" in new_news:
        print("\n🔹 Haber Güncelleniyor...")
        updated_news = update_news(new_news["data"]["id"], "Güncellenmiş Başlık", "Güncellenmiş İçerik")
        pprint(updated_news)

        print("\n🔹 Haber Siliniyor...")
        pprint(delete_news(new_news["data"]["id"]))