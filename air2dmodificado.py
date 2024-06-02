#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
new_path = os.path.abspath('../')
sys.path.append(new_path)

from gmes import *

SIZE = (10,10,0)

space = Cartesian(size=SIZE, resolution=20)
geom_list = [DefaultMedium(material=Dielectric()),
             Shell(material=Cpml())]
points = [(0,-2,0),(0,2,0)]                         #Para 2 puntos 
#points = [(-2,-2,0),(-2,2,0),(2,-2,0),(2,2,0)]     #Para 4 puntos
src_list = [PointSource(src_time=Continuous(freq=0.8),
                        center=point,
                        component=Ez) for point in points]

my_fdtd = TMzFDTD(space, geom_list, src_list)

my_fdtd.init()

my_fdtd.show_field(Ez, Z, 0)
my_fdtd.show_field(Hx, Z, 0)
my_fdtd.show_field(Hy, Z, 0)
my_fdtd.step_until_t(10)
my_fdtd.write_field(Ez, (-5,-5,0), (5,5,0))