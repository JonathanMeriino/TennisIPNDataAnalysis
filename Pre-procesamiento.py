#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 19:13:15 2025

@author: jonathan
"""

import pandas as pd
import numpy as np

# Cargar el archivo
file_path = "TenisIPNForm.xlsx"
xls = pd.ExcelFile(file_path)

# Leer la hoja "Respuestas"
df_original = pd.read_excel(xls, sheet_name="Respuestas")

#Eliminar columnas inecesarias
df_col = df_original.drop(columns=['Marca temporal', 
                                   'Nombre completo ( empezando por apellidos )',
                                   'Boleta','Correo institucional',
                                   'Teléfono personal','Teléfono de emergencia',
                                   'Link de tu carpeta de google drive con tu documentación ( Asegúrate de que se permita el acceso) '])

#Estandarizar datos
df_col['Escuela de procedencia'] = df_col['Escuela de procedencia'].str.strip().str.lower().str.capitalize()


print(df_col['Escuela de procedencia'].value_counts())


reemplazos_escuelas= {
    'Esiquie': 'Esiqie',
    'Escuela superior de ingeniería química e industrias extractivas': 'Esiqie',
    'Esime': 'Esime zacatenco',
    'Esime zac': 'Esime zacatenco',
    'Esime zacatenco.': 'Esime zacatenco',
    'Escuela nacional de biblioteconomía y archivonomía': 'Enba',
    'Upibi ipn': 'Upibi',
    'Esia': 'Esia zacatenco',
    'Esia z': 'Esia zacatenco',
    'Esia zac': 'Esia zacatenco',
    'Esia u.zac': 'Esia zacatenco',
    'Esia - escuela superior de ingeniería y arquitectura unidad zacatenco': 'Esia zacatenco',
    'Escuela superior de ingeniería y arquitectura': 'Esia zacatenco',
    'Esia ticoman': 'Esia ticomán',
    'Escuela superior de computp': 'Escom',
    'Esca sto.': 'Esca ust',
    'Escuela superior de ingeniería textil (esit)': 'Esit'
    }

df_col['Escuela de procedencia'] = df_col['Escuela de procedencia'].replace(reemplazos_escuelas)

print(df_col['Escuela de procedencia'].value_counts())


df_col.to_excel('TenisIPNProcessed.xlsx')