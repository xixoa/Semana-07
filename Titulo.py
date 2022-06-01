# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:36:47 2022

@author: Sebastian
"""
#Importamos la libreria
import camelcase
#Tenemos una cadena llamda nombre y se desea que se muestre
#en formato titulo
nombre = "sebastian timo Laura antezana"

print(nombre.upper())

print(nombre.title())

#Creamos un objeto llamado cam
cam= camelcase.CamelCase()
print("Con Camelcase....")

#Imprimos el nombre en formato título
#Utilizamos camelcase
print(cam.hump(nombre))

#Para resolver el problema
#Creamos otro objeto cam2
#Al definir el objeto incluimos los argumentos
#'sebastian' y 'leon'

cam2 = camelcase.CamelCase('sebastian','antezana')
print(cam2.hump(nombre))