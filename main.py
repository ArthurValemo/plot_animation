# -*- coding: utf-8 -*-


##Couleurs valorem
yellow = (255/255,215/255,31/255)
orange = (242/255,148/255,0/255)
orange_intense = (234/255,100/255,31/255)
brown = (177/255,78/255,29/255)
brown_dark = (126/255,46/255,24/255)
purple = (149/255,88/255,155/255)
cyan_light = (133/255,194/255,186/255)
cyan = (0/255,152/255,151/255)
blue = (71/255,98/255,120/255)
green = (132/255,184/255,25/255)
greensea = (0/255,101/255,100/255)
greenbrown = (82/255,95/255,47/255)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler

from plotter_data import plotter
from GUI_graphe import runAppGui

color_cycler = cycler(color=[orange_intense,blue,green,brown,greensea,orange,purple,greenbrown,yellow,cyan,brown_dark])
plt.rc('axes', prop_cycle=color_cycler)




figure_plotter = plotter("../data/Liste_arrets_v2.xlsx")
runAppGui(figure_plotter)

