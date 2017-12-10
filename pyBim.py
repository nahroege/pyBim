#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
import re
import bs4 

class pyBim:
    def __init__(self):
        self.bim_base = 'http://www.bim.com.tr'
        self.aktuel_base = self.bim_base+'/Categories/100/aktuel-urunler.aspx'
        self.keylink = self.aktuel_base+'?Bim_AktuelTarihKey='
        self.nothing = ''
        
    def aktuel_date(self,date='this_week'):
        if date is 'last_week' or date is 'this_week' or date is 'next_week':
            self.date = date
        else:
            raise Exception('Bimodule.aktuel()\'s date can take only 3 diffrent params. \n Param 1: this_week (or leave empty) \n Param 2: next_week \n Param 3: last_week')
            
    def get_aktuel(self):
        keys = []
        hrefs = []
        urls = {}
        raw_data = get(self.aktuel_base)
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

bim = pyBim()
bim.aktuel_date('next_week')
bim.get_aktuel()
print(bim.url)

