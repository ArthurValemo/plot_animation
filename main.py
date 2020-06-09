# -*- coding: utf-8 -*-

from plotter_data import plotter
from GUI_graphe import runAppGui

##################################################
#                                                #
#            /!\ CHEMIN DU FICHIER /!\           #
chemin_fichier = "../data/Liste_arrets_v2.xlsx"
#                                                #
##################################################


#Execution
figure_plotter = plotter(chemin_fichier)
runAppGui(figure_plotter)