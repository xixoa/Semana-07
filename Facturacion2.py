# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:52:43 2022

@author: Sebastian
"""

#Dado el total, calcular el IGV y el Subtotal

import financiero
total = 1000.49
print(f"Subtotal: {financiero.obtenerSubTotalconTotal(total): .2f}")
print(f"IGV: {financiero.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")