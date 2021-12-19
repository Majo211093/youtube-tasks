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


plt.figure()
USvideos = pd.read_csv('D:/Auxiliar/Descargas/proyectosPy/USvideos.csv')
likes_por_fechas_Child = USvideos[USvideos['video_id'] == 'VYOjWnS4cMY'].groupby(['trending_date'])
likes_por_fechas_Child['likes'].sum().plot(color='b', label= 'Likes')
plt.semilogy()

vistas_por_fechas_Child = USvideos[USvideos['video_id'] == 'VYOjWnS4cMY'].groupby(['trending_date'])
vistas_por_fechas_Child['views'].sum().plot(color='y', label= 'Views')

dislikes_por_fechas_Child = USvideos[USvideos['video_id'] == 'VYOjWnS4cMY'].groupby(['trending_date'])
dislikes_por_fechas_Child['dislikes'].sum().plot(color='r', label = 'Dislikes')
plt.xlabel('Trending Date')

plt.title('Childish Gambino - This is America (Official Video)')  
plt.legend()

   

