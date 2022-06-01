# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:45 2022

@author: Sebastian
"""
#at: agregar texto, me supongo que es add text
archivo = open("noticia.txt","at")
contenido="\nFuente: RPP"

archivo.write(contenido)
archivo.close()