import streamlit as st
import pandas as pd
import sqlite3
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

# Título y descripción
st.title("Actividad 1 - Creación de DataFrames")
st.write("En esta actividad exploraremos distintas formas de crear y mostrar DataFrames usando Streamlit y Pandas.")

# 1. Diccionario
st.subheader("📚 DataFrame de Libros")
libros_dict = {
    "título": ["1984", "Cien años de soledad", "El principito", "Fahrenheit 451"],
    "autor": ["George Orwell", "Gabriel García Márquez", "Antoine de Saint-Exupéry", "Ray Bradbury"],
    "año de publicación": [1949, 1967, 1943, 1953],
    "género": ["Distopía", "Realismo mágico", "Fábula", "Ciencia ficción"]
}
df_libros = pd.DataFrame(libros_dict)
st.dataframe(df_libros)

# 2. Lista de diccionarios
st.subheader("🌆 Información de Ciudades")
ciudades = [
    {"nombre": "París", "población": 2148000, "país": "Francia"},
    {"nombre": "Lima", "población": 9675000, "país": "Perú"},
    {"nombre": "Tokio", "población": 13929000, "país": "Japón"},
    {"nombre": "Nairobi", "población": 4397000, "país": "Kenia"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# 3. Lista de listas
st.subheader("🏪 Productos en Inventario")
productos = [
    ["Lápiz", 0.5, 100],
    ["Cuaderno", 1.5, 200],
    ["Regla", 0.8, 150],
    ["Borrador", 0.3, 300]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# 4. Series
st.subheader("👥 Datos de Personas")
nombres = pd.Series(["Ana", "Luis", "María", "Carlos"])
edades = pd.Series([25, 30, 22, 28])
ciudades = pd.Series(["Madrid", "Bogotá", "Buenos Aires", "Santiago"])
df_personas = pd.DataFrame({"Nombre": nombres, "Edad": edades, "Ciudad": ciudades})
st.dataframe(df_personas)

# 5. Archivo CSV
st.subheader("📄 Datos desde CSV")
df_csv = pd.read_csv("data.csv")
st.dataframe(df_csv)

# 6. Archivo Excel
st.subheader("📊 Datos desde Excel")
df_excel = pd.read_excel("data.xlsx")
st.dataframe(df_excel)

# 7. Archivo JSON
st.subheader("📁 Datos de Usuarios desde JSON")
df_json = pd.read_json("data.json")
st.dataframe(df_json)

# 8. URL pública
st.subheader("🌐 Datos desde URL")
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
df_url = pd.read_csv(url)
st.dataframe(df_url)


# 9. Base de datos SQLite
st.subheader("🗃️ Datos desde SQLite")
conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        nombre TEXT,
        calificación INTEGER
    )
""")
cursor.execute("DELETE FROM estudiantes")
cursor.executemany("INSERT INTO estudiantes (nombre, calificación) VALUES (?, ?)", [
    ("María", 95),
    ("Juan", 88),
    ("Elena", 91)
])
conn.commit()
df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
st.dataframe(df_sqlite)
conn.close()

# 10. Array de NumPy
st.subheader("🔢 Datos desde NumPy")
array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
df_numpy = pd.DataFrame(array, columns=["Columna A", "Columna B", "Columna C"])
st.dataframe(df_numpy)


