# -*- coding: utf-8 -*-

#Imports
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from numpy import cos,sin,linspace,pi
import matplotlib.patches as patches
from matplotlib.backends.backend_qt5agg  import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import sys


class plotGUI(QWidget):


    #Style des Labels
    fontsize = 12
    font = "Cambria"
    Police = QFont(font,fontsize)
    Police2 = QFont(font,10)
    SheetStyle = "background-color: rgb(217,221,230) ; color : rgb(8,60,110)"
    SheetStyle2 = " color : rgb(110,60,8)"

    #-----------------------------------------------------------------#
    #                       Init                                      #
    #-----------------------------------------------------------------#
    def __init__(self,figure_plotter):

        self.__figure_plotter = figure_plotter
        self.__figure = figure_plotter.figure
        
        super().__init__()
        self.__InitUI()

        
    
    def __InitFig(self) :
        """Permet de générer le graphique et de le réinitialiser."""
        
        self.__figureCanvas = FigureCanvas(self.__figure)
        self.__figureCanvas.draw()
        self.__figureCanvas.mpl_connect('button_press_event', self.click_figure)
        
        self.__FigToolbar = NavigationToolbar(self.__figureCanvas, self)
        self.__FigToolbar.setMinimumWidth(450)

    def __InitUI(self):
        
        #self.resize(1200,900)
        self.setWindowTitle('Graphiques')
        self.setWindowIcon(QIcon("icons/plot.png"))
        self.__InitFig()

        #Génération des Layouts
        self.__HBoxMain = QHBoxLayout(self)
        self.__VBox1 = QVBoxLayout()
        self.__VBox2 = QVBoxLayout()


        #Intégration des widgets aux layouts
        self.Widget1A = self.__Widget1A()
        self.Widget1B = self.__Widget1B()
        
        self.__VBox1.addWidget(self.Widget1A)
        self.__VBox2.addWidget(self.Widget1B)

        #Intégration Layouts
        self.__HBoxMain.addLayout(self.__VBox1)
        self.__HBoxMain.addLayout(self.__VBox2)

    def __Widget1B(self):

        #Bouton
        self.__ClearBtn = QPushButton(QIcon('icons/clear.png'),"Clear")
        self.__DetailsBtn = QPushButton(QIcon('icons/detail.png'),"Details")

        self.__ClearBtn.clicked.connect(self.clear_figure)
        self.__DetailsBtn.clicked.connect(self.detail_selection)

        #QLineEdit
        self.__QLselection = QLineEdit()
        self.__QLselection.setReadOnly(True) 
        self.__cb = QComboBox()
        self.__cb.addItems(["Nombre arrets","Durees arrets","Pertes energie"])
        self.__cb.currentIndexChanged.connect(self.change_data_name)


        #Widget
        widget = QWidget()
        widget.setMaximumWidth(550)
        
        #BoxLayout
        VBoxMain = QVBoxLayout(widget)
        self.__VBox1B = QVBoxLayout()

        #Intégration
        VBoxMain.addStretch()
        VBoxMain.addWidget(self.__cb)
        VBoxMain.addWidget(self.__ClearBtn)
        VBoxMain.addWidget(self.__QLselection)
        VBoxMain.addWidget(self.__DetailsBtn)
        VBoxMain.addStretch()

        

        return widget

    #-----------------------------------------------------------------#
    #                       Widget 2A : Graphics                                 #
    #-----------------------------------------------------------------#
    

    def __Widget1A(self):
        #Widget
        widget = QWidget()

       
        #BoxLayout
        VBoxMain = QVBoxLayout(widget)
        

        #Intégration
        VBoxMain.addStretch()
        VBoxMain.addWidget(self.__figureCanvas)
        VBoxMain.addWidget(self.__FigToolbar)
        VBoxMain.addStretch()
          

        return widget




    def clear_figure(self) :
        self.__figure_plotter.clear_figure()
        self.__figureCanvas.draw()

    def detail_selection(self) :
        self.__figure_plotter.detail_selection()
        self.__figureCanvas.draw()

    def click_figure(self,event):
        self.__figure_plotter.click_figure(event)
        selection = self.__figure_plotter.selection
        self.__QLselection.setText(selection)
        

    def change_data_name(self) : 
        cb_text = self.__cb.currentText()
        if cb_text == "Nombre arrets" : 
            data_name = "ID"
        if cb_text == "Durees arrets" : 
            data_name = "DUREE_ARRET"
        if cb_text == "Pertes energie" : 
            data_name = "PERTES_ENERGIE_GLOBALES"
        self.__figure_plotter.change_data_name(data_name)
        self.__figureCanvas.draw()


def runAppGui(figure_plotter) : 
    
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    mainWindow = plotGUI(figure_plotter)
    mainWindow.show()
    sys.exit(app.exec_())