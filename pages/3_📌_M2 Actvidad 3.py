import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

st.title("1. Operadores de comparación")

# 1. Ingreso mensual mayor a 5,000,000 COP
print(df_nuevo[df_nuevo['ingreso_mensual'] > 5000000].head())

# 2. Edad menor a 25 años
print(df_nuevo[df_nuevo['edad'] < 25].head())

# 3. Ocupación exactamente "Estudiante"
print(df_nuevo[df_nuevo['ocupacion'] == 'Estudiante'].head())

# 4. No vivan en vivienda "Propia"
print(df_nuevo[df_nuevo['tipo_vivienda'] != 'Propia'].head())

# 5. Edad mayor o igual a 60 años
print(df_nuevo[df_nuevo['edad'] >= 60].head())
