# -*- coding: utf-8 -*-
"""
Spyder Editor

Los módulos te permitiran crear librerias funcionales 
que puedas utilizar o reutilizar en cualquier momento
"""

igv = 0.18

def obtenerIGVSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    #subtotal + igv*subtotal
    #subtotal*(1+0.18)
    return subtotal*(1+igv)

def obtenerSubTotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubTotalconTotal(total)