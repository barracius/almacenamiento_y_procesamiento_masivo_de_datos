import MongoConection as mc
import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

class Application(ttk.Frame):
    run = False
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Entrega 2")
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.first_frame = ttk.Frame(self)
        self.first_frame.pack(side='top', fill='both', expand=True)
        self.combo1 = ttk.Combobox(self.first_frame, state="readonly")
        self.combo1["values"] = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.combo1.set('Año')
        self.combo1.pack(side='left')
        self.boton1 = ttk.Button(self.first_frame, text='Query 1', command=self.grafico_uno)
        self.boton1.pack(side='left')

        self.second_frame = ttk.Frame(self)
        self.second_frame.pack(side='top', fill='both', expand=True)
        self.combo2 = ttk.Combobox(self.second_frame, state="readonly")
        self.combo2["values"] = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.combo2.set('Año')
        self.combo2.pack(side='left')
        self.boton2 = ttk.Button(self.second_frame, text='Query 2', command=self.grafico_dos)
        self.boton2.pack(side='left')

    def grafico_uno(self):
        anno = self.combo1.get()
        listaUrbano, listaRural = mc.EscolaridadPorArea(anno)

        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        X = np.arange(12)
        #print(listaUrbano)
        #print('----------')
        #print(listaRural)
        plt.bar(X + 0.00, listaUrbano, color='b', width=0.33)
        plt.bar(X + 0.33, listaRural, color='r', width=0.33)
        plt.xticks(X, meses, fontsize=7, rotation=(45))
        colors = {'Área Urbana': 'blue', 'Área Rural': 'red'}
        labels = list(colors.keys())
        handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
        plt.legend(handles, labels, bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.title(f'Monto total subvencionado a establecimientos educacionales \n'
                  f'según área, del año {anno}')

        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.yticks(fontsize=6, rotation=(45))
        plt.xlabel('Mes')
        plt.ylabel('Chile Peso (CLP)')
        plt.tight_layout()
        plt.show()

    def grafico_dos(self):
        anno = self.combo2.get()
        listaUrbano, listaRural = mc.EscolaridadPromedioPorArea(anno)

        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        X = np.arange(12)
        # print(listaUrbano)
        # print('----------')
        # print(listaRural)
        plt.bar(X + 0.00, listaUrbano, color='b', width=0.33)
        plt.bar(X + 0.33, listaRural, color='r', width=0.33)
        plt.xticks(X, meses, fontsize=7, rotation=(45))
        colors = {'Área Urbana': 'blue', 'Área Rural': 'red'}
        labels = list(colors.keys())
        handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label]) for label in labels]
        plt.legend(handles, labels, bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.title(f'Monto promedio subvencionado a establecimientos educacionales \n'
                  f'según área, del año {anno}')

        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.yticks(fontsize=6, rotation=(45))
        plt.xlabel('Mes')
        plt.ylabel('Chile Peso (CLP)')
        plt.tight_layout()
        plt.show()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
