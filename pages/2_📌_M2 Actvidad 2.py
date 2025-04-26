import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

# Cargar datos desde el archivo CSV
df = pd.read_csv("estudiantes_colombia.csv")

st.title("🎓 Aplicación de Análisis de Estudiantes - Colombia")


# Ver primeras y últimas 5 filas
with st.expander("🔍 Ver primeras y últimas 5 filas"):
    st.write("Primeras 5 filas:")
    st.dataframe(df.head())
    st.write("Últimas 5 filas:")
    st.dataframe(df.tail())

# Mostrar info() y describe()
with st.expander("📋 Resumen del dataset"):
    col1, col2 = st.columns(2)

    with col1:
        if st.checkbox("Mostrar info()"):
            buffer = io.StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())

    with col2:
        if st.checkbox("Mostrar describe()"):
            st.write(df.describe())

# Seleccionar columnas específicas
with st.expander("🧩 Seleccionar columnas"):
    columnas = st.multiselect("Selecciona columnas a mostrar:", df.columns.tolist())
    if columnas:
        st.dataframe(df[columnas])
    else:
        st.info("Selecciona una o más columnas para mostrar.")

# Filtrar por promedio con slider
with st.expander("🎯 Filtrar estudiantes por promedio"):
    valor_min = st.slider("Selecciona el promedio mínimo:", 0.0, 5.0, 4.0, step=0.1)
    filtrado = df[df["promedio"] >= valor_min]
    st.write(f"Estudiantes con promedio mayor o igual a {valor_min}:")
    st.dataframe(filtrado)

