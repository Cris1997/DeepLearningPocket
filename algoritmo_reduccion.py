#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:56:21 2019

@author: cristianrosales
"""

from PIL import Image
from os import listdir
from os.path import isfile, isdir

def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]
for i in range(1,34):
    files=ls1("/Users/cristianrosales/Desktop/TrabajoTerminal/DeepLearning3/VinosOriginales/"+str(i)+"/")
    print(len(files))
    files.sort
    
    listimg=[]
    for file in files:
            listimg.append(file)
            
    print(listimg[:10])
    
    for item in listimg:
        if 'JPG' in item:    
            try:
                imagen = Image.open('VinosOriginales/'+str(i)+'/'+item)
            except:
                continue
            rgb_im = imagen.convert('RGB')
            reducida = rgb_im.resize((400,300),Image.ANTIALIAS)
            rotar = reducida.rotate(270,0,1)
            rotar.save('VinosOriginales/'+str(i)+'/rotadas/'+ item,quality=100)


#
#
#imagen = Image.open('5180.JPG')
##print(imagen.histogram)
#reducida = imagen.resize((400,300))
##reducida.show()
##girada1 = reducida.rotate(270,0,1)
#reducida.save('nueva6.jpg')
##Restar las dos imagenes y ver com varian las imagenes
