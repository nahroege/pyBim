#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
import bs4 

class pyBim:
    def __init__(self):
        self.bim_base = 'http://www.bim.com.tr'
        self.aktuel_base = self.bim_base+'/Categories/100/aktuel-urunler.aspx'
        self.nothing = ''
    def aktuel_date(self,date='this_week'):
        if date is 'last_week' or date is 'this_week' or date is 'next_week':
            self.date = date
        else:
            raise Exception('Bimodule.aktuel()\'s date can take only 3 diffrent params. \n Param 1: this_week (or leave empty) \n Param 2: next_week \n Param 3: last_week')
            
    def get_aktuel(self):
        raw_data = get(self.aktuel_base)
        soup = bs4.BeautifulSoup(raw_data.text, "lxml")
        afterdiv = soup('div', {"class": "anasayfaaktuelbaslik"})
        if self.date is 'this_week':
            self.url = self.bim_base + afterdiv[0].a['href']
        elif self.date is 'next_week':
            self.url = self.bim_base + afterdiv[1].a['href']
        elif self.date is 'last_week':
            self.url = self.nothing
        else:
            raise Exception('Unknown Date Format.')

            
bim = pyBim()
bim.aktuel_date('last_week')
bim.get_aktuel()
print(bim.url)


