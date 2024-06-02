#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
new_path = os.path.abspath('../')
sys.path.append(new_path)

from gmes import *

SIZE = (10,10,0)

#Se define el tamaño del espacio y la resoloción
space = Cartesian(size=SIZE, resolution=20) 

'''Se Define una lista de geometrías en el espacio, con un medio dieléctrico predeterminado y
 una capa de Perfectamente Adaptado al Aire (CPML) .'''
geom_list = [DefaultMedium(material=Dielectric()),
             Shell(material=Cpml())] 
             
#Se generan los puntos para la grafica
points = [(0,-2,0),(0,2,0)]                         #Para 2 puntos 
#points = [(-2,-2,0),(-2,2,0),(2,-2,0),(2,2,0)]     #Para 4 puntos

#Define una lista de fuentes de onda, en este caso, una fuente puntual que oscila con una frecuencia de 0.8 Hz
src_list = [PointSource(src_time=Continuous(freq=0.8),
                        center=point,
                        component=Ez) for point in points]

#Crea una instancia del simulador FDTD para el modo TMz
my_fdtd = TMzFDTD(space, geom_list, src_list)

#Inicializa el simulador
my_fdtd.init()

#Muestra el campo Ez Hx Hy en el plano Z=0
my_fdtd.show_field(Ez, Z, 0)
my_fdtd.show_field(Hx, Z, 0)
my_fdtd.show_field(Hy, Z, 0)

#Ejecuta la simulación durante 10 segundos
my_fdtd.step_until_t(10)

#Guarda los valores del campo Ez en el rango de coordenadas
my_fdtd.write_field(Ez, (-5,-5,0), (5,5,0))