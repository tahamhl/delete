# Delete Uygulaması

Bu uygulama, belirtilen klasördeki dosyaları silmek için kullanılan bir Python uygulamasıdır.

## Özellikler

- Klasör içindeki dosyaları listeleme
- Seçilen dosyaları silme
- Kullanıcı dostu arayüz

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repository-url]
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım

Uygulamayı çalıştırmak için:

```bash
python Delete.py
```

## Exe Oluşturma

Eğer uygulamayı exe olarak derlemek isterseniz:

1. PyInstaller'ı yükleyin:
```bash
pip install pyinstaller
```

2. Exe dosyasını oluşturun:
```bash
pyinstaller --onefile Delete.py
```

Oluşturulan exe dosyası `dist` klasöründe bulunacaktır.

