#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
new_path = os.path.abspath('../')
sys.path.append(new_path)

from gmes import *
#Se define el tamaño del espacio y la resoloción
space = Cartesian(size=(16,8,0), resolution=10)

'''Se Define una lista de geometrías en el espacio, con un medio dieléctrico predeterminado,
   un bloque dieléctrico con constante dieléctrica 12 y
   una capa de Perfectamente Adaptado al Aire (CPML) .'''
geom_list = [DefaultMedium(material=Dielectric()),
             Block(material=Dielectric(12),
                   size=(inf, 1, inf)),
             Shell(material=Cpml())]

#Se generan los puntos para la grafica        
points = [(-7,-2,0),(-7,2,0)]       

#Define una lista de fuentes de onda, en este caso, una fuente puntual que oscila con una frecuencia de 0.15 Hz
src_list = [PointSource(src_time=Continuous(freq=0.15),
                        component=Ez,
                        center=point) for point in points]

#Crea una instancia del simulador FDTD para el modo TMz
my_fdtd = TMzFDTD(space, geom_list, src_list)

#Inicializa el simulador
my_fdtd.init()

#Muestra el campo Ez en el plano Z=0
my_fdtd.show_field(Ez, Z, 0)

#Ejecuta la simulación durante 200 segundos
my_fdtd.step_until_t(200)