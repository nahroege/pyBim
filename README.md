![PyBim Logo](https://media.discordapp.net/attachments/326420797721673729/399580454228983808/68747470733a2f2f692e68697a6c69726573696d2e636f6d2f34474e477a512e706e67.png)

# pyBim
*Bim Aktuel Module for Python*

## Docs / Examples

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

Define A Aktuel Product's specific page URL(default):
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

Result:
```shell
last_week
```

#### Set Aktuel Date as This Week
Usage 1 (Leave Empty):
```python
bim = pyBim()
bim.aktuelUrunler_date()
```

or

Usage 2:
```python
bim = pyBim()
bim.aktuelUrunler_date()
```

Result:
```shell
this_week
```

#### Set Aktuel Date as Next Week
Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('next_week')
```

Result:
```shell
next_week
```
#### Exception: Set Aktuel Date as Something other than these
Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('somethinglolololololo')
```

Result:

```python
Traceback (most recent call last):
  File "pyBim.py", line 125, in <module>
    bim.aktuelUrunler_date('somethinglolololololo')
  File "pyBim.py", line 28, in aktuelUrunler_date
    raise Exception('Bimodule.aktuel()\'s date can take only 3 diffrent params. \n Param 1: this_week (or leave empty) \n Param 2: next_week \n Param 3: last_week')
Exception: Bimodule.aktuel()'s date can take only 3 diffrent params. 
 Param 1: this_week (or leave empty) 
 Param 2: next_week 
 Param 3: last_week
```

### Get Aktuel Products Page

In date function we define the Aktuel's date, now we get Aktuel's Page of spesific date

Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
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
**Note: Random function doesnt give same product twice!**
#### Usage 1 (Leave Empty):
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
bim.aktuelUrunler_parse(),
bim.aktuelUrun_random()
```

Result:
```shell
{'price': '4,95', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_OREO.png', 'desc': '', 'name': 'Oreo 228 g'}
```

#### Usage 2 (Give Amount):
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
bim.aktuelUrunler_parse(),
bim.aktuelUrun_random(5)
```

Result:
```shell
[{'price': '3,50', 'desc': '\xa0%25 fındıklı\n', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_NESTLE FINDIK.png', 'name': 'Sütlü Fındıklı  Çikolata  Nestle 70 g'}, {'price': '5,45', 'desc': 'Fındık aromalı krema dolgulu\nYoğurt krema dolgulu\n', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_SUN BEST.png', 'name': 'Tam Tahıllı Kahvaltılık Bisküvi  Hellema 253 g'}, {'price': '4,95', 'desc': '', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_OREO.png', 'name': 'Oreo 228 g'}, {'price': '7,95', 'desc': 'Bitter çikolata parçacıklı 225 g\nBitter çikolatalı ve kakao 225 g\nMozaik 255 g\n', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_MUFFIN.png', 'name': 'Mini Kekler\xa0 Kuchenmeister'}, {'price': '3,95', 'desc': '\xa0%23 bademli\n', 'img': 'http://www.bim.com.tr/Uploads/aktuel-urunler/292_buyuk_330x280_NESTLE BADEM.png', 'name': 'Bademli  Beyaz  Çikolata  Nestle  70 g'}]
```

#### Exception: Give Amount bigger than total products
**Note: You can get total amount of products with (self.total_item)**

Exception Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
bim.aktuelUrunler_parse()
bim.aktuelUrun_random(15)
```

Result:
```python
Traceback (most recent call last):
  File "pyBim.py", line 128, in <module>
    bim.aktuelUrun_random(15)
  File "pyBim.py", line 106, in aktuelUrun_random
    raise Exception('Amount can not bigger than total amount of aktuel items.')
Exception: Amount can not bigger than total amount of aktuel items.
```

### Search in Aktuel
Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
bim.aktuelUrunler_parse()
print(bim.aktuelUrun_search('Toblerone 360'))
```

Result:
```shell
['toblerone-360-g']
```

### Download Specific Product Image

Usage:
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
bim.aktuelUrunler_get()
bim.aktuelUrunler_parse()
bim.aktuelUrun_dl(bim.aktuelUrun_random(),'../img/')
```

Result:
```shell
../img/Sütlü Fındıklı  Çikolata  Nestle 70 g.png
```
