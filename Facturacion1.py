# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:47:10 2022

@author: Sebastian
"""

#Dado el subtotal, calcular el IGV y el Total

import financiero
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV:{financiero.obtenerIGVSubtotal(subtotal): .2f}")
print(f"Total: {financiero.obtenerTotalconSubtotal(subtotal): .2f}")