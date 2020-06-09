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

color_cycler = cycler(color=[orange_intense,blue,green,brown,greensea,orange,purple,greenbrown,yellow,cyan,brown_dark])
plt.rc('axes', prop_cycle=color_cycler)


class plotter : 

    def __init__(self,file_name) : 

        xlsx = pd.ExcelFile(file_name)
        self.__data_frame = pd.read_excel(xlsx,'Sheet1')
        filtre = np.ones(len(self.__data_frame),dtype=bool)
        self.initialise_donnees('CODE_F0',filtre)
        self.ordonner_donnees()
        self.initialise_figure()
        self.__selection = ''


    def initialise_donnees(self,group_key,filtre) : 
        list_group = [group_key,'DUREE_ARRET','ID','PERTES_ENERGIE_GLOBALES']
        agg_famille_dict = {"DUREE_ARRET":sum,"ID":len,"PERTES_ENERGIE_GLOBALES":sum}
        self.__group_key = group_key
        self.__group = self.__data_frame[filtre][list_group].groupby(group_key).agg(agg_famille_dict)
        


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

        self.__fig = plt.figure(figsize=(8,5))
        self.__ax = self.__fig.add_subplot(111)
        self.__wedges,texts,autotexts = self.__ax.pie(self.__data_array,autopct='%1.1f%%',startangle=90,textprops=dict(color="w"))
        self.__ax.set_title("Répartion : <"+self.__data_label+"> par <"+self.__group_key+">")
        self.__ax.grid(True)
        self.__ax.axis('equal')
        self.__ax.legend(self.__wedges, self.__list_index,
                        title=self.__group_key,
                        loc="center left",
                        bbox_to_anchor=(1, 0, 0.5, 1))
        self.__fig.tight_layout()

    def rafraichir_figure(self) :

        self.__fig.clf()
        self.__ax = self.__fig.add_subplot(111)
        self.__wedges,texts,autotexts = self.__ax.pie(self.__data_array,autopct='%1.1f%%',startangle=90,textprops=dict(color="w"))
        self.__ax.set_title("Répartion : <"+self.__data_label+"> par <"+self.__group_key+">")
        self.__ax.grid(True)
        self.__ax.axis('equal')
        self.__ax.legend(self.__wedges, self.__list_index,
                        title=self.__group_key,
                        loc="center left",
                        bbox_to_anchor=(1, 0, 0.5, 1))
        self.__fig.tight_layout()





    def click_figure(self,event) : 

        xclick, yclick = event.xdata, event.ydata 
        selection_mask = self.__find_selection(xclick,yclick)
        selection = self.__list_index[selection_mask]
        if len(selection)>0 :
            self.__selection =  selection[0]
        else : 
            self.__selection = ''


    @property
    def figure(self) : 
        return self.__fig

    @property
    def selection(self) : 
        return self.__selection

    def __find_selection(self,xclick,yclick) :
        selection_mask = []
        for wedge in self.__wedges : 
            selection_mask.append(wedge.get_path().contains_point([xclick,yclick]))
        return selection_mask

    def detail_selection(self) : 
        detail_flag = True
        if self.__group_key == 'CODE_F0' : 
            group_key = 'CODE_F1' 
        elif self.__group_key == 'CODE_F1' : 
            group_key = 'FAMILLE_STATUS' 
        else : detail_flag = False

        print(self.__group_key)
        if self.__selection != '' and detail_flag : 

            filtre = self.__data_frame[self.__group_key]==self.__selection
            self.initialise_donnees(group_key,filtre)
            self.ordonner_donnees(self.__data_name)
            self.rafraichir_figure()
            

    def clear_figure(self) : 
        filtre = np.ones(len(self.__data_frame),dtype=bool)
        self.initialise_donnees('CODE_F0',filtre)
        self.ordonner_donnees(self.__data_name)
        self.rafraichir_figure()

    def change_data_name(self,data_name) : 

            self.ordonner_donnees(data_name)
            self.rafraichir_figure()

