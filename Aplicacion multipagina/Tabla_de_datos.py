import streamlit as st
import pandas as pd


st.subheader("Tabla de datos")
st.write("Los datos que exploraremos están disponibles en la siguiente tabla:")

df = pd.read_csv("Datos/quality_life_2020.csv", sep=";")
st.dataframe(df)

st.page_link("Indicadores_de_calidad_de_vida.py", label="Anterior", icon="⬅️")
st.page_link("Grafica_de_barras.py", label="Siguiente", icon="➡️")