import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Actividad 4: Explorador interactivo de DataFrame con .loc y .iloc")

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


data = {
    "ID": [101, 102, 103, 104, 105],
    "Nombre": ["Ana", "Luis", "Carla", "David", "Eva"],
    "Edad": [28, 34, 29, 42, 25],
    "Departamento": ["Ventas", "TI", "Marketing", "TI", "Ventas"],
    "Salario": [50000, 65000, 48000, 72000, 51000]
}
df = pd.DataFrame(data).set_index("ID") 

st.subheader("DataFrame original")
st.dataframe(df)


st.subheader("Selección con .loc (por etiquetas)")

ids_seleccionados = st.multiselect("Selecciona IDs para filas (.loc)", options=df.index.tolist(), default=df.index.tolist())

cols_seleccionadas = st.multiselect("Selecciona columnas (.loc)", options=df.columns.tolist(), default=df.columns.tolist())

if ids_seleccionados and cols_seleccionadas:
    df_loc = df.loc[ids_seleccionados, cols_seleccionadas]
    st.write("DataFrame con .loc:")
    st.dataframe(df_loc)
else:
    st.write("Selecciona al menos una fila y columna para usar .loc")

st.subheader("Selección con .iloc (por posición)")

fila_min, fila_max = st.slider("Rango de filas para .iloc (por posición)", 0, len(df)-1, (0, len(df)-1))
col_min, col_max = st.slider("Rango de columnas para .iloc (por posición)", 0, len(df.columns)-1, (0, len(df.columns)-1))

df_iloc = df.iloc[fila_min:fila_max+1, col_min:col_max+1]
st.write("DataFrame con .iloc:")
st.dataframe(df_iloc)

st.subheader("Modificar datos usando .loc")

id_modificar = st.selectbox("Selecciona ID para modificar", options=df.index.tolist())
col_modificar = st.selectbox("Selecciona columna para modificar", options=df.columns.tolist())

nuevo_valor = st.text_input(f"Nuevo valor para {col_modificar} del ID {id_modificar}")

if st.button("Modificar valor"):
    try:
        if df[col_modificar].dtype in [np.int64, np.float64]:
            nuevo_valor_cast = float(nuevo_valor)
        else:
            nuevo_valor_cast = nuevo_valor
        
        df.loc[id_modificar, col_modificar] = nuevo_valor_cast
        st.success(f"Valor modificado correctamente: {id_modificar}, {col_modificar} = {nuevo_valor_cast}")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error al modificar el valor: {e}")

st.subheader("DataFrame final")
st.dataframe(df)


