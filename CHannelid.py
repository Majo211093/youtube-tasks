# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:24:10 2021

@author: Albert
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:49:50 2021

@author: Albert
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from datetime import time
import sys
USvideos = pd.read_csv('D:/Auxiliar/Descargas/proyectosPy/USvideos.csv')
# TAREA NUMERO 2 
# tiempo_para_hacerse_viral = trending_date - publish_time
# print(tiempo_para_hacerse_viral)
#  days_lapse indica el número de días antes de que el video sea tendencia
def unique_channel_title(keep='last'):
    '''Removes duplicate videos to keep single record according to trending_date and keep argument.'''
    
    df = USvideos.copy()
    df.sort_values(by=['channel_title', 'trending_date'], axis=0, inplace=True)
    df.drop_duplicates(subset='channel_title', keep='last', inplace=True)
    
    return df

df = unique_channel_title(keep='first')

def publish_date(string):
    return string.split('T')[0]

df['publish_date'] = pd.to_datetime(df.publish_time.apply(func=lambda val:publish_date(val)),format='%Y-%m-%d')
df['trending_date'] = pd.to_datetime(df.trending_date,format = '%y.%d.%m')
df['days_lapse'] = df['trending_date'] - df['publish_date']

days_lapse=df['days_lapse']
days_lapse_count=days_lapse.value_counts().to_dict() #to dic: convertirlo  en dicc de python
# Dictionary[Key] = Value
# Key = Number of days
# Value = Number of rows matching
# Agrupa los elementos por orden.
# import pdb; pdb.set_trace()     #----- detener la ejecución del programa
days, count = zip(
  # Materializa el filtro en una lista (evalua el filtro)
  # adicionalmente: el * pasa CADA elemento como argumento para la funcion
  *sorted(
    # Materializa el filtro en una lista (evalua el filtro)
    list(
      # Filtra un iterable (esencialmente: una lista)
      # filter(lambda variable: exp
      # %DICT%.items(): Convierte el dict {k1: v1, k2: v2} en [(k1, v1), (k2, v2)]
        filter(
lambda each_tuple: each_tuple[0].days < 8, days_lapse_count.items())
    ),
    # key (del sorted) indica qué debe considerarse para ordenar la lista.
    key=lambda val: val[0]
  )
)


fig, grafica = plt.subplots(figsize=(19, 13), nrows=1, ncols=1)

cmap = plt.get_cmap('autumn')
colors = [cmap(i) for i in np.linspace(0, 1, len(days))]

# promedio = np.mean(days_lapse.value_counts())
# DE = np.std(days_lapse.value_counts()) 

grafica.bar(range(len(days)), np.log(count), align = 'center', width=0.6, color=colors)
grafica.set_xticks(range(len(days)))
label_days = ['{} days'.format(i.days) for i in days]
grafica.set_xticklabels(label_days, rotation=45)
grafica.set_ylabel('log of frequency count')
# frecuency count = número de veces que ocurre un suceso
grafica.set_xlabel('Número de dìas antes de ser tendencia')
grafica.set_title('Plot de la frecuencia discreta del número de días antes de ser tendencia')


