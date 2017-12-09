#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get
import bs4 

class Bimodule:
    
    def __init__(self,param):
        self.bim_base = 'http://www.bim.com.tr'
        self.aktuel_base = self.bim_base+'/Categories/100/aktuel-urunler.aspx'
        self.param = param
        
    def aktuel_date(self,date='this_week'):
        if date is 'after' or date is 'this_week':
            self.date = date
        else:
            raise Exception('Bimodule.aktuel()\'s date can take only 2 diffrent params. \n Param 1: this_week (or leave empty) \n Param 2: after ')
    def get_aktuel(self):
        raw_data = get(self.aktuel_base)
        soup = bs4.BeautifulSoup(raw_data.text, "lxml")
        afterdiv = soup('div', {"class": "anasayfaaktuelbaslik"})
        if self.date is 'this_week':
            self.url = self.bim_base + afterdiv[0].a['href']
        else:
            self.url = self.bim_base + afterdiv[1].a['href']
bim = Bimodule('nothing')
bim.aktuel_date()
bim.get_aktuel()
print(bim.url)


