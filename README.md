# Twitter User Data Analysis and Interest-based Matching Tool

## Overview
This project aims to analyze Twitter user data stored in local JSON files to identify and match users with shared interests. Leveraging graph theory and custom data structures, it organizes and visualizes data efficiently, providing insights into user interactions on Twitter.

## Project Features
- Processing Twitter user data from local JSON files
- Using hash tables and search algorithms to match users based on shared interests
- Employing networkx and matplotlib for visualizing user relationships and networks
- Featuring a GUI built with Tkinter for easier user interaction
- Creating interest-based user trees and optimizing connections with minimum spanning trees
- Using text analysis and natural language processing (NLP) techniques to analyze interests

## Getting Started

### Prerequisites
- Python 3.6 or newer
- Required Python libraries:
  - `faker`: For generating new test users
  - `tqdm`: For progress bar display
  - `networkx`: For graph theory and network visualization
  - `matplotlib`: For visualization of graphs
  - `nltk`: For natural language processing and text analysis

### Installation
To install the necessary Python libraries, use the following command:
```bash
pip install -r requirements.txt
```

## Running the Application
To start the application, run the main.py script:
```bash
python main.py
```

## Data Structures
The core data structures used in the project:
- **Hash Map**: Provides fast access between users and interests
- **Linked Lists**: Used for dynamic data storage
- **Graph**: Used to represent relationships between users
- **Stack and Queue**: Used for graph traversal algorithms

## User Interface
The application comes with a Tkinter interface offering the following functions:
- User search and graph display
- Visualization of user networks by interests
- Graph visualization of all users
- Analyzing and visualizing user interests
- Finding interest-based connections using BFS (Breadth-First Search) algorithm

## Data Preparation
Ensure your Twitter user data is in JSON format, including necessary attributes for analysis and matching algorithms to function properly. If needed, you can use DataGenerator.py to create new test users.

## Usage Example
1. Generate or load user data through the GUI
2. Explore visualized user networks and relationships
3. Analyze and match users based on shared interests
4. Visualize connections between interests
5. Create a minimum spanning tree for users

## Algorithm Explanations
- **DFS (Depth-First Search)**: Used for text analysis and interest extraction
- **BFS (Breadth-First Search)**: Used to explore user connections
- **Minimum Spanning Tree**: Used to find optimal connections between users

## Dependencies
- Python 3.6 or newer
- Required Python libraries: `faker`, `tqdm`, `networkx`, `matplotlib`, `nltk`

## Contributors
- Yunus Hanifi Öztürk
- Eyüp Ensar Kara

---

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

