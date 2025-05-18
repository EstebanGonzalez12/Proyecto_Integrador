import streamlit as st
import pandas as pd
import numpy as np
import random
from faker import Faker
import datetime

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


fake = Faker('es_CO')
np.random.seed(42)
random.seed(42)
fake.seed_instance(42)

n = 50
df = pd.DataFrame({
    'id': range(1, n+1),
    'nombre': [fake.name() for _ in range(n)],
    'edad': np.random.randint(18, 66, n),
    'ciudad': random.choices(['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'], k=n),
    'ingreso_mensual': np.random.randint(1000000, 10000001, n),
    'ocupacion': random.choices(['Estudiante', 'Ingeniero', 'Comerciante', 'Desempleado', 'Docente'], k=n),
    'fecha_nacimiento': [fake.date_of_birth(minimum_age=18, maximum_age=65) for _ in range(n)],
    'internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
})
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

st.sidebar.header("Filtros")

df_filtrado = df.copy()

# Filtro por edad
if st.sidebar.checkbox("Filtrar por edad"):
    edad_min, edad_max = st.sidebar.slider("Rango de edad", 18, 65, (25, 40))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(edad_min, edad_max)]

# Filtro por ciudad
if st.sidebar.checkbox("Filtrar por ciudad"):
    ciudades = st.sidebar.multiselect("Seleccione ciudad", df['ciudad'].unique())
    if ciudades:
        df_filtrado = df_filtrado[df_filtrado['ciudad'].isin(ciudades)]

# Filtro por ocupación
if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = st.sidebar.multiselect("Seleccione ocupación", df['ocupacion'].unique())
    if ocupaciones:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones)]

# Filtro por ingreso
if st.sidebar.checkbox("Filtrar por ingreso mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mínimo (COP)", 1000000, 10000000, 2000000, step=500000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] >= ingreso_min]

# Filtro por acceso a internet
if st.sidebar.checkbox("Solo con internet"):
    df_filtrado = df_filtrado[df_filtrado['internet'] == True]

# Mostrar resultados
st.subheader("🔎 Datos filtrados")
st.dataframe(df_filtrado)

st.write(f"Registros encontrados: **{df_filtrado.shape[0]}**")
