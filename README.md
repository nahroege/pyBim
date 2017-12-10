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

```python
bim = pyBim()
bim.slugify('slug me pls')
```

### Date

In aktuelUrunler_date function we set date

#### Set Aktuel Date as Last Week
```python
bim = pyBim()
bim.aktuelUrunler_date('last_week')
```

#### Set Aktuel Date as This Week
```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
```

#### Set Aktuel Date as Next Week
```python
bim = pyBim()
bim.aktuelUrunler_date('next_week')
```

### Get Aktuel Products Page

In date function we define the Aktuel's date, now we get Aktuel's Page of spesific date

```python
bim = pyBim()
bim.aktuelUrunler_date('this_week')
url = bim.aktuelUrunler_get()
```

Result:
```shell
http://www.bim.com.tr/Categories/100/aktuel-urunler.aspx?Bim_AktuelTarihKey=292
```


