# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:44 2022

@author: Sebastian
"""
#wt: leer archivo, me supongo que read text
archivo=open("archivo_de_prueba.txt","wt")
contenido="Linea1 Hola amigos ¿Cómo estan?\nLinea2 Bienvenidos a la untels"
archivo.write(contenido)
archivo.close()