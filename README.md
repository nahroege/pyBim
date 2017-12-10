# PyBim
![PyBim Logo](https://i.hizliresim.com/RO5WqZ.png)

*Bim Aktuel Module for Python*

## Usage

### Importing

Complete Import

```python
import pyBim
```

Import Base Functions

```python
from pyBim import aktuelUrunler_date, aktuelUrunler_get
```

### Init
Define header in this section (default):
```python
self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
```

Define Bim Website URL (default):
```python
self.bim_base = 'http://www.bim.com.tr'
```

Define Bim Website's Aktuel Section URL (default):
```python
self.aktuel_base = self.bim_base+'/Categories/100/aktuel-urunler.aspx'
```

Define Key Link (default):
```python
self.keylink = self.aktuel_base+'?Bim_AktuelTarihKey='
```

Define A Aktuel Product's specific page (default):
```python
self.aktuel_urun = self.bim_base+'/aktuel-urunler/'
```

Define Empty String as Nothing (default):
```python
self.nothing = ''
```

### Slugify

In search section we need slugify the keyword so we define a function for slugifying text.

Usage:
```python
bim = pyBim()
bim.slugify('Toptan fiyatına perâkende satış')
```

Result:
```shell
toptan-fiyatina-perakende-satis
```
### Date

In aktuelUrunler_date function we set date

#### Set Aktuel Date as Last Week
Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('last_week')
```

#### Set Aktuel Date as This Week
Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
```

#### Set Aktuel Date as Next Week
Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('next_week')
```

### Get Aktuel Products Page

In date function we define the Aktuel's date, now we get Aktuel's Page of spesific date

Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
url = bim.aktuelUrunler_get()
```

Result:
```shell
http://www.bim.com.tr/Categories/100/aktuel-urunler.aspx?Bim_AktuelTarihKey=292
```

### Get Aktuel Products Detail

In last function we generate aktuel page link for parsing products, now we can parse products in Aktuel Catalog

Defaults:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
```

#### Array's Object 0 - Total Product Amount
Usage:
```python
print(bim.aktuelUrunler_parse()[0])
```

Result:
```shell
12
```

#### Array's Object 1 - Slugified Product Names
Usage:
```python
print(bim.aktuelUrunler_parse()[1])
```

Result:
```shell
['toblerone-360-g', 'sutlu-findikli-cikolata-nestle-70-g', 'bademli-beyaz-cikolata-nestle-70-g', 'karisik-kurabiye-cesitleri-lambertz-235-g', 'tam-tahilli-kahvaltilik-biskuvi-hellema-253-g', 'oreo-228-g', 'hindistan-cevizli-sutlu-cikolata-kaplamali-biskuvi-hellema-175-g', 'sutlu-kakao-kremali-gofret-wafer-master-500-g', 'mini-kekler-kuchenmeister', 'elma-dolgulu-kurabiye-new-yorkers-200-g', 'findik-aromali-kakaolu-dolgulu-waffle-136-g', 'dolgulu-sert-seker-olips-3-lu-paket']
```

#### Array's Object 2 - Full Product URL's
Usage:
```python
print(bim.aktuelUrunler_parse()[2])
```

Result:
```shell
['http://www.bim.com.tr/aktuel-urunler/toblerone-360-g/kral.aspx', 'http://www.bim.com.tr/aktuel-urunler/sutlu-findikli-cikolata-nestle-70-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/bademli-beyaz-cikolata-nestle-70-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/karisik-kurabiye-cesitleri-lambertz-235-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/tam-tahilli-kahvaltilik-biskuvi-hellema-253-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/oreo-228-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/hindistan-cevizli-sutlu-cikolata-kaplamali-biskuvi-hellema-175-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/sutlu-kakao-kremali-gofret-wafer-master-500-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/mini-kekler-kuchenmeister/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/elma-dolgulu-kurabiye-new-yorkers-200-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/findik-aromali-kakaolu-dolgulu-waffle-136-g/aktuel.aspx', 'http://www.bim.com.tr/aktuel-urunler/dolgulu-sert-seker-olips-3-lu-paket/aktuel.aspx']
```

### Parsing Specific Product with All Info  from URL
In aktuelUrun_parse function we must send a url for parsing product data 

Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
bim.aktuelUrun_parse(bim.aktuelUrunler_parse()[2][1]) #Send Full URL of product
```

Result:
```shell
{'price': '3,50', 'name': 'Sütlü Fındıklı  Çikolata  Nestle 70 g', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_NESTLE FINDIK.png', 'desc': '\xa0%25 fındıklı\n'}
```

### Random Bim Product from Aktuel
