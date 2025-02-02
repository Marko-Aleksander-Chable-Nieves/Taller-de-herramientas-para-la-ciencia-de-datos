import streamlit as st
import pandas as pd

# Función para calcular métricas estadísticas
def calcular_metricas(df):
    return {
        "Promedio": round(df["Life_exp"].mean(), 2),
        "Desviación Estándar": round(df["Life_exp"].std(), 2),
        "Mínimo": df["Life_exp"].min(),
        "Máximo": df["Life_exp"].max()
    }

# Función para mostrar métricas en tarjetas
def mostrar_metricas(metricas, titulo):
    with st.container():
        st.subheader(titulo)
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col1.metric("Promedio", metricas["Promedio"])
        col2.metric("Desviación Estándar", metricas["Desviación Estándar"])
        col3.metric("Mínimo", metricas["Mínimo"])
        col4.metric("Máximo", metricas["Máximo"])

# Cargar datos
df = pd.read_csv("OECD.csv", sep=",")

# Título
st.title("Análisis de Expectativa de Vida en la OECD")

#Información
st.markdown("Observaremos los datos de expectativa de vida en la OECD, previamente podremos identificar la recolección de información por género y miembros de la OECD, de igual manero los que no son miembros.")

# Selección de año
year = st.radio("Seleccione el año", options=range(2015, 2024), index=8)

# Filtros de agrupamiento
st.write("Opciones de filtrado:")
filter_oecd = st.checkbox("Diferenciar por membresía en la OCDE")
filter_gender = st.checkbox("Diferenciar por género")

# Filtrar datos por año
df_year = df[df["Year"] == year]

# Mostrar métricas según filtros seleccionados
if not filter_oecd and not filter_gender:
    metricas_total = calcular_metricas(df_year[df_year["Gender"] == "Total"])
    mostrar_metricas(metricas_total, "Métricas para todos los países")

if filter_oecd and not filter_gender:
    metricas_oecd = calcular_metricas(df_year[(df_year["Gender"] == "Total") & (df_year["OECD"] == True)])
    mostrar_metricas(metricas_oecd, "Métricas para países miembros de la OCDE")

    metricas_no_oecd = calcular_metricas(df_year[(df_year["Gender"] == "Total") & (df_year["OECD"] == False)])
    mostrar_metricas(metricas_no_oecd, "Métricas para países no miembros")

if not filter_oecd and filter_gender:
    metricas_hombres = calcular_metricas(df_year[df_year["Gender"] == "Male"])
    mostrar_metricas(metricas_hombres, "Métricas para Hombres")

    metricas_mujeres = calcular_metricas(df_year[df_year["Gender"] == "Female"])
    mostrar_metricas(metricas_mujeres, "Métricas para Mujeres")

if filter_oecd and filter_gender:
    st.subheader("Métricas por género y membresía en la OCDE")

    metricas_hombres_oecd = calcular_metricas(df_year[(df_year["Gender"] == "Male") & (df_year["OECD"] == True)])
    mostrar_metricas(metricas_hombres_oecd, "Hombres - OCDE")

    metricas_hombres_no_oecd = calcular_metricas(df_year[(df_year["Gender"] == "Male") & (df_year["OECD"] == False)])
    mostrar_metricas(metricas_hombres_no_oecd, "Hombres - No OCDE")

    metricas_mujeres_oecd = calcular_metricas(df_year[(df_year["Gender"] == "Female") & (df_year["OECD"] == True)])
    mostrar_metricas(metricas_mujeres_oecd, "Mujeres - OCDE")

    metricas_mujeres_no_oecd = calcular_metricas(df_year[(df_year["Gender"] == "Female") & (df_year["OECD"] == False)])
    mostrar_metricas(metricas_mujeres_no_oecd, "Mujeres - No OCDE")


st.page_link("Distribucion_de_la_OECD.py", label="Siguiente", icon="➡️")
