# Twitter Kullanıcı Verileri Analizi ve İlgi Alanı Tabanlı Eşleştirme Aracı

## Genel Bakış
Bu proje, yerel JSON dosyalarında saklanan Twitter kullanıcı verilerini analiz ederek ortak ilgi alanlarına sahip kullanıcıları belirlemeyi ve eşleştirmeyi amaçlamaktadır. Graf teorisi ve özel veri yapıları kullanarak verileri verimli bir şekilde organize eder ve görselleştirir, böylece Twitter'daki kullanıcı etkileşimleri hakkında içgörüler sunar.

## Proje Özellikleri
- Yerel JSON dosyalarından Twitter kullanıcı verilerini işleme
- Kullanıcıları ortak ilgi alanlarına göre eşleştirmek için hash tabloları ve arama algoritmaları kullanma
- Kullanıcı ilişkilerini ve ağlarını görselleştirmek için networkx ve matplotlib kullanımı
- Kolay kullanıcı etkileşimi için Tkinter ile oluşturulmuş grafiksel kullanıcı arayüzü (GUI)
- İlgi alanı tabanlı kullanıcı ağaçları oluşturma ve en küçük kapsayan ağaçlar (minimum spanning trees) ile bağlantıları optimize etme
- İlgi alanlarını analiz etmek için metin analizi ve doğal dil işleme (NLP) teknikleri

## Başlangıç

### Ön Gereksinimler
- Python 3.6 veya daha yeni bir sürüm
- Gerekli Python kütüphaneleri:
  - `faker`: Yeni test kullanıcıları oluşturmak için
  - `tqdm`: İlerleme çubuğu gösterimi için
  - `networkx`: Graf teorisi ve ağ görselleştirme için
  - `matplotlib`: Grafikleri görselleştirme için
  - `nltk`: Doğal dil işleme ve metin analizi için

### Kurulum
Gerekli Python kütüphanelerini kurmak için aşağıdaki komutu kullanın:
```bash
pip install -r requirements.txt
```

## Uygulamayı Çalıştırma
Uygulamayı başlatmak için main.py komut dosyasını çalıştırın:
```bash
python main.py
```

## Veri Yapısı
Projede kullanılan temel veri yapıları:
- **Hash Map**: Kullanıcılar ve ilgi alanları arasında hızlı erişim sağlar
- **Bağlı Listeler**: Dinamik veri depolama için kullanılır
- **Graf**: Kullanıcılar arasındaki ilişkileri göstermek için kullanılır
- **Yığın (Stack) ve Kuyruk (Queue)**: Graf gezinme algoritmaları için kullanılır

## Kullanıcı Arayüzü
Uygulama, aşağıdaki işlevleri sunan bir Tkinter arayüzü ile gelir:
- Kullanıcı arama ve grafik görüntüleme
- İlgi alanlarına göre kullanıcı ağlarını görüntüleme
- Tüm kullanıcıların graf görselleştirmesi
- Kullanıcıların ilgi alanlarını analiz etme ve görselleştirme
- İlgi alanı tabanlı bağlantıları BFS (Genişlik Öncelikli Arama) algoritması ile bulma

## Veri Hazırlama
Twitter kullanıcı verilerinizin analiz ve eşleştirme algoritmalarının düzgün çalışması için gerekli özellikleri içeren JSON formatında olduğundan emin olun. Gerekirse, yeni test kullanıcıları oluşturmak için DataGenerator.py'ı kullanabilirsiniz.

## Kullanım Örneği
1. GUI aracılığıyla kullanıcı verilerini oluşturun veya yükleyin
2. Görselleştirilmiş kullanıcı ağlarını ve ilişkilerini keşfedin
3. Ortak ilgi alanlarına göre kullanıcıları analiz edin ve eşleştirin
4. İlgi alanları arasındaki bağlantıları görselleştirin
5. Kullanıcılar için en küçük kapsayan ağaç oluşturun

## Algoritma Açıklamaları
- **DFS (Derinlik Öncelikli Arama)**: Metin analizi ve ilgi alanı çıkarımı için kullanılır
- **BFS (Genişlik Öncelikli Arama)**: Kullanıcı bağlantılarını keşfetmek için kullanılır
- **Minimum Spanning Tree**: Kullanıcılar arasındaki optimum bağlantıları bulmak için kullanılır

## Bağımlılıklar
- Python 3.6 veya daha yeni bir sürüm
- Gerekli Python kütüphaneleri: `faker`, `tqdm`, `networkx`, `matplotlib`, `nltk`

## Katkıda Bulunanlar
- Yunus Hanifi Öztürk
- Eyüp Ensar Kara

