# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:33:06 2022

@author: Sebastian
"""
#rt= tipo lectura, me supongo que read text
noticia = open("noticia.txt","rt",encoding="utf8")
datos_noticia = noticia.read()
print(datos_noticia)