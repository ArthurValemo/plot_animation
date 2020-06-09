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


class plotter : 

    def __init__(self,file_name) : 

        xlsx = pd.ExcelFile(file_name)
        self.__data_frame = pd.read_excel(xlsx,'Sheet1')
        self.initialise_donnees('CODE_F0')
        self.ordonner_donnees()
        self.initialise_figure()


    def initialise_donnees(self,group_key) : 
        list_group = [group_key,'DUREE_ARRET','ID','PERTES_ENERGIE_GLOBALES']
        agg_famille_dict = {"DUREE_ARRET":sum,"ID":len,"PERTES_ENERGIE_GLOBALES":sum}
        self.__group_key = group_key
        self.__group = self.__data_frame[list_group].groupby(group_key).agg(agg_famille_dict)
        


    def ordonner_donnees(self,data_name='ID'):
        #DUREE PAR FAMILLE
        self.__data_name = data_name
        #self.__group = self.__group.sort_values(by=data_name,ascending=False)
        self.__data_array = self.__group[data_name].values
        self.__list_index = self.__group.index.values
        if data_name == "ID" : 
            self.__data_label = "nombre arrêts cumulés"
        if data_name == "DUREE_ARRETS" : 
            self.__data_label = "temps d'arrêt cumulés"
        if data_name == "PERTES_ENERGIE_GLOBALES" : 
            self.__data_label = "pertes cumulées"
        
    
    def initialise_figure(self) : 

        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(111)
        self.__ax.pie(self.__data_array,labels=self.__list_index,autopct='%1.1f%%',startangle=90)
        self.__ax.set_title("Répartion : <"+self.__data_label+"> par <"+self.__group_key+">")
        self.__ax.grid(True)
        self.__ax.axis('equal')
        self.__fig.tight_layout()