# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 09:21:37 2021

@author: Albert
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from datetime import time


plt.figure(figsize=(19, 13))
USvideos = pd.read_csv('D:/Auxiliar/Descargas/proyectosPy/USvideos.csv')

vistas_por_fechas_Child = USvideos[USvideos['video_id'] == 'VYOjWnS4cMY'].groupby(['trending_date'])
vistas_por_fechas_Child['views'].sum().sort_values().plot(logy=True, color='y', label= 'Views')

likes_por_fechas_Child = USvideos[USvideos['video_id'] == 'VYOjWnS4cMY'].groupby(['trending_date'])
likes_por_fechas_Child['likes'].sum(axis=1).sort_values().plot.bar(color='b', label= 'Likes')
#plt.semilogy()

dislikes_por_fechas_Child = USvideos[USvideos['video_id'] == 'VYOjWnS4cMY'].groupby(['trending_date'])
dislikes_por_fechas_Child['dislikes'].sum(axis=1).sort_values().plot.bar(color='r', label = 'Dislikes')
plt.xlabel('Trending Date')

plt.title('Childish Gambino - This is America (Official Video)')  
plt.legend()

#normalizar los tres valores o aplicar suma acumulativa
   

