# X (Twitter) Veri Analizi ve Kullanıcı İlişkilendirmesi

## 📋 Proje Bilgisi

Bu proje, **Kocaeli Üniversitesi Bilgisayar Mühendisliği Bölümü Programlama Lab. I** dersi kapsamında **2023-2024 Güz dönemi** için hazırlanmıştır (Proje III).

## 📋 Proje Hakkında

Bu proje, X (Twitter) platformundaki kullanıcı verilerini analiz ederek, kullanıcılar arasındaki ilişkileri ve ortak ilgi alanlarını tespit etmek için geliştirilmiştir. Proje, veri yapıları, graf teorisi ve arama algoritmaları kullanarak kullanıcı ilişkilerini görselleştirir ve analiz eder.


## ✨ Özellikler

- **Hash Tabloları** ile kullanıcı verilerinin hızlı erişimi
- **Graf Yapısı** ile kullanıcı ilişkilerinin modellenmesi
- **DFS (Depth-First Search)** ile tweet içeriklerinden ilgi alanı analizi
- **BFS (Breadth-First Search)** ile benzer ilgi alanına sahip kullanıcı bulma
- **Minimum Spanning Tree** ile minimum bağlantılı kullanıcı ağları oluşturma
- **Grafiksel Arayüz** ile görselleştirme ve analiz

---

## 🚀 Kurulum

### Gereksinimler

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

```bash
pip install networkx matplotlib tqdm nltk faker
```

### NLTK Veri Seti

NLTK stopwords veri setini indirmeniz gerekiyor:

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

---

## 📁 Proje Yapısı

```
Twitter_Analysis_Project/
├── main.py              # Ana program dosyası
├── variables.py         # Veri yapıları ve algoritmalar
├── initTkinter.py      # GUI arayüzü
├── DataGenerator.py    # Test verisi oluşturucu
├── users1k.json        # Kullanıcı verileri
└── README.md           # Bu dosya
```

---

## 🎯 Kullanım

### Programı Çalıştırma

```bash
python main.py
```

Program çalıştığında bir GUI penceresi açılır ve aşağıdaki özellikleri kullanabilirsiniz:

### Kullanılabilir Özellikler

1. **Kullanıcı Arama**: Kullanıcı adı girerek kullanıcının takip ettiği kişilerin grafını görüntüleyin
2. **İlgi Alanı Arama**: Dropdown menüden ilgi alanı seçerek o ilgi alanına sahip kullanıcıları görüntüleyin
3. **Tüm Kullanıcı Grafı**: Tüm kullanıcıların ilişkilerini gösteren grafı görüntüleyin
4. **İlgi Alanı Bağlantıları**: Belirli bir kullanıcıdan başlayarak benzer ilgi alanına sahip kullanıcıları BFS ile bulun
5. **İlgi Alanları Grafiği**: İlgi alanlarının kullanıcı sayısına göre dağılımını görüntüleyin

---

## 🔧 Teknik Detaylar

### Veri Yapıları

- **LinkedList**: Bağlı liste yapısı
- **HashMap**: Hash tablosu ile hızlı erişim
- **Graph**: Graf yapısı ile ilişki modelleme
- **User**: Kullanıcı nesnesi (tweet, takipçi, takip edilen bilgileri)

### Algoritmalar

- **DFS (Depth-First Search)**: Tweet içeriklerinden ilgi alanı çıkarma
- **BFS (Breadth-First Search)**: Benzer ilgi alanına sahip kullanıcı bulma
- **Minimum Spanning Tree**: Minimum bağlantılı ağ oluşturma

---

## 📊 Veri Formatı

Kullanıcı verileri JSON formatında saklanır:

```json
{
  "username": "kullanici_adi",
  "name": "Ad Soyad",
  "followers_count": 100,
  "following_count": 50,
  "region": "tr",
  "language": "tr",
  "tweets": ["tweet1", "tweet2", ...],
  "following": ["kullanici1", "kullanici2", ...],
  "followers": ["kullanici3", "kullanici4", ...]
}
```

---

## 🛠️ Test Verisi Oluşturma

Kendi test verilerinizi oluşturmak için:

```bash
python DataGenerator.py
```

Bu komut, `users60k.json` dosyasına test verileri oluşturur.

---

## 📝 Notlar

- Tüm veri yapıları ve algoritmalar sıfırdan yazılmıştır
- Proje, hazır kütüphaneler kullanmadan temel veri yapılarını uygular
- Görselleştirme için `networkx` ve `matplotlib` kullanılmıştır

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.
