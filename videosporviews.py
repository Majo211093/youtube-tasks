# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:49:50 2021

@author: Albert
"""
import pandas as pd
import matplotlib as plt
import numpy as np

# nueva funcion que el ...me enseño. Una función es una manera de hacer código que se a a repetir todo el tiempo. JoséDaniel2021)
# Tener cuidado con los niveles de indentación
def top_10_vistas_por_columna(dataset, nombre_columna):
    agrupados_ds = dataset.groupby([nombre_columna]) #la diferencia son los []
    # solo se puede agrupar por un campo 
    suma_por_vista = agrupados_ds['views'].sum().sort_values()
    return suma_por_vista.tail(10)   

def top_10_vistas_por_columnas(dataset, columnas):
    agrupados_ds = dataset.groupby(columnas)
    suma_por_vista = agrupados_ds['views'].sum().sort_values()
    return suma_por_vista.tail(10) 
  
def top_10_sum(dataset, columnas_sum=[], columnas_group_by=[]):
    agrupados_ds = dataset.groupby(columnas_group_by)
    suma_por_vista = agrupados_ds[columnas_sum].sum()
    return suma_por_vista.tail(10) 

USvideos = pd.read_csv('D:/Auxiliar/Descargas/proyectosPy/USvideos.csv')
# display(USvideos)

print("=== Views by trending Date ===")
print(top_10_vistas_por_columna(USvideos, 'trending_date'))
print('------------')

print("=== Views by title ===")
print(top_10_vistas_por_columna(USvideos, 'title')) 
print('------------')

print("=== Views by channel title ===")
print(top_10_vistas_por_columna(USvideos, 'channel_title'))
print("-----------")

print("=== Views by category id  ===")
print(top_10_vistas_por_columna(USvideos, 'category_id'))
print("-----------")

print("=== Views by category id  ===")
print(top_10_vistas_por_columna(USvideos, 'publish_time'))
print("-----------")

print("=== Views by category id  ===")
print(top_10_vistas_por_columnas(USvideos, ['category_id', 'channel_title']))
print("-----------")

print("=== Views by category id and channel title  ===")
print(top_10_sum(
    USvideos,
    columnas_sum=['category_id', 'channel_title'],
    columnas_group_by=['views']
    )
) 
print("-----------")
