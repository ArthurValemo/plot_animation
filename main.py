# -*- coding: utf-8 -*-

from plotter_data import plotter
from GUI_graphe import runAppGui

##################################################
#                                                #
#            /!\ CHEMIN DU FICHIER /!\           #
chemin_fichier = "../data/GRANDVILLE_new.xlsx"
#                                                #
##################################################


#Execution
figure_plotter = plotter(chemin_fichier)
runAppGui(figure_plotter)