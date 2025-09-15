
# InstaGhost

**InstaGhost**, Instagram benzeri bir sosyal medya takip analiz uygulamasıdır. Bu CLI (Command-Line Interface) uygulaması, kullanıcıların takipçilerini ve takip ettiklerini yönetmelerine, gizli hayranları ve hayran olduklarını görüntülemelerine olanak sağlar. Python ve JSON tabanlı veri yönetimi kullanır.

## Proje Hakkında

InstaGhost, kullanıcıların takipçi ilişkilerini analiz edebileceği bir Python uygulamasıdır.  
Uygulama, JSON dosyaları aracılığıyla veri saklar ve kullanıcıya konsol üzerinden etkileşimli bir menü sunar.

Proje temel olarak üç modülden oluşur:

- `classes.py` → JSON tabanlı veri yönetimi ve takipçileri/following sınıfları.
- `func.py` → Menü, mesaj ve yardımcı fonksiyonlar.
- `main.py` → Uygulamanın ana çalıştırılabilir dosyası; kullanıcı etkileşimi ve uygulama mantığı burada.

## Özellikler

- Takipçileri listeleme.
- Takip edilenleri listeleme.
- Gizli hayranları görüntüleme.
- Hayran olduklarımı görüntüleme.
- Kolay JSON tabanlı veri yönetimi.
- Hata yönetimi ile kullanıcı dostu CLI deneyimi.

## Kurulum

1. Python 3.x sürümünü bilgisayarınıza kurun.
2. Projeyi bilgisayarınıza indirin veya klonlayın.
3. Gerekli klasör ve JSON dosyaları proje tarafından otomatik oluşturulacaktır.

Örnek komut ile çalıştırma:

```bash
python main.py
```

## Kullanım

Program çalıştırıldığında kullanıcı aşağıdaki menü ile karşılaşır:

```
======InstaGhost======
1 -> Takipçileri Listele
2 -> Takip Edilenleri Listele
3 -> Gizli Hayranları Listele
4 -> Hayranı Olduklarımı Listele
5 -> Çıkış
```

- **Seçenek 1:** Takipçileri listeler.
- **Seçenek 2:** Takip ettiklerinizi listeler.
- **Seçenek 3:** Gizli hayranları listeler.
- **Seçenek 4:** Hayran olduklarınızı listeler.
- **Seçenek 5:** Uygulamadan çıkış yapar.

### Örnek JSON Veri Yapısı

`followers_1.json` ve `following.json` dosyaları aşağıdaki formatta veri içerir:

```json
[
  {
    "string_list_data": [
      {"value": "kullanici_adi1"}
    ]
  },
  {
    "string_list_data": [
      {"value": "kullanici_adi2"}
    ]
  }
]
```

## Dosya Yapısı

```
InstaGhost/
│
├── main.py
├── classes.py
├── func.py
├── Takipçiler ve Takip Edilenler(JSON)/
│   ├── followers_1.json
│   └── following.json
└── README.md
```

## Bağımlılıklar

- Python 3.x
- Standart kütüphaneler: `json`, `os`

## Geliştirme ve İyileştirme Önerileri

- Çıkış işlemi `break` ile döngüden tam olarak çıkabilir.
- Menü ve mesaj metinleri ayrı bir konfigürasyon dosyasına taşınabilir.
- `get_usernames()` fonksiyonunda hata yönetimi geliştirilebilir.
- GUI veya web tabanlı arayüz ile daha kullanıcı dostu bir uygulama geliştirilebilir.
