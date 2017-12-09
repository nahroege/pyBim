#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import get

class Bimodule:
    
    def __init__(self,param):
        self.param = param
        
    def aktuel(self,date='this_week'):
        if date is 'after' or date is 'this_week':
            self.date = date
        else:
            raise Exception('Bimodule.aktuel()\'s date can take only 2 diffrent params. \n Param 1: this_week (or leave empty) \n Param 2: after ')

bim = Bimodule('nothing')

