#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
from random import randint
import re
import bs4 

class pyBim:
    def __init__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        self.bim_base = 'http://www.bim.com.tr'
        self.aktuel_base = self.bim_base+'/Categories/100/aktuel-urunler.aspx'
        self.keylink = self.aktuel_base+'?Bim_AktuelTarihKey='
        self.aktuel_urun = self.bim_base+'/aktuel-urunler/'
        self.nothing = ''
        
    def aktuelUrunler_date(self,date='this_week'):
        if date is 'last_week' or date is 'this_week' or date is 'next_week':
            self.date = date
            return True
        else:
            raise Exception('Bimodule.aktuel()\'s date can take only 3 diffrent params. \n Param 1: this_week (or leave empty) \n Param 2: next_week \n Param 3: last_week')
            
    def aktuelUrunler_get(self):
        keys = []
        hrefs = []
        urls = {}
        raw_data = get(self.aktuel_base, headers=self.headers)
        soup = bs4.BeautifulSoup(raw_data.text, "lxml")
        afterdiv = soup('div', {"class": "anasayfaaktuelbaslik"})
        hrefs.append(self.bim_base + afterdiv[0].a['href'])
        hrefs.append(self.bim_base + afterdiv[1].a['href'])
        regex = r"=(\d{3})"
        for i in hrefs:
            match = re.search(regex, i)
            keys.append(match.group(1))
        keys.append(str(int(min(keys))-1))
        keys.sort()
        urls['last_week'] = keys[0]
        urls['this_week'] = keys[1]
        urls['next_week'] = keys[2]
        if self.date is 'last_week':
            self.url = self.keylink+urls['last_week']
        elif self.date is 'this_week':
            self.url = self.keylink+urls['this_week']
        elif self.date is 'next_week':
            self.url = self.keylink+urls['next_week']
        else:
            raise Exception('Unknown Date Format.')
        return self.url
        
    def aktuelUrunler_parse(self):
        fullitem = []
        slugitem = []
        raw_data = get(self.url, headers=self.headers)
        regex = r"\"\/aktuel-urunler\/(.*?)\/(.*?)\"><"
        matches = re.finditer(regex, raw_data.text)
        for matchNum, match in enumerate(matches):
            slugitem.append(match.group(1))
            fullitem.append(self.aktuel_urun+match.group(1)+'/'+match.group(2))
            matchNum = matchNum + 1
        self.total_item = matchNum
        self.slugitem = slugitem
        self.fullitem = fullitem
        return matchNum,slugitem,fullitem
        
    def aktuelUrun_parse(self,full):
        item = {}
        raw_data = get(full, headers=self.headers)
        soup = bs4.BeautifulSoup(raw_data.text, "lxml")
        item['img'] = self.bim_base+soup('img', {"class": "img-responsive"})[0].get('src')
        item['name'] = soup('h3')[0].text.strip()
        item['price'] = soup('button', {"class": "btn btn-danger"})[0].text.strip()
        item['desc'] = ""
        rawdesc = soup('div', {"class": "slide-frame-detail"})[0]
        for i in rawdesc.select('li'):
            item['desc'] += i.text + '\n'
        return item
        
    def aktuelUrun_random(self,amount=1):
        if amount is 1:
            rand = randint(0,len(self.fullitem))
            return self.aktuelUrun_parse(self.fullitem[rand])
        elif amount <= len(self.fullitem):
            items = []
            x = 0
            while x < amount:
                rand = randint(0,len(self.fullitem))
                if pyBim.aktuelUrun_parse(self,self.fullitem[rand]) in items:
                    continue
                else:
                    items.append(pyBim.aktuelUrun_parse(self,self.fullitem[rand]))
                    x += 1
            return items
        else:
            raise Exception('Amount can not bigger than total amount of aktuel items.')
            
