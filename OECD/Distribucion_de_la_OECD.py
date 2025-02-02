import streamlit as st
import pandas as pd
import altair as alt

# Función para generar un boxplot
def generar_boxplot(df, titulo, color="blue"):
    return alt.Chart(df).mark_boxplot().encode(
        y=alt.Y("Life_exp:Q", title="Esperanza de vida", scale=alt.Scale(zero=False)),
        color=alt.value(color)
    ).properties(
        width=300, height=400, title=titulo
    )

# Función para mostrar un único boxplot
def mostrar_boxplot(df, titulo):
    with st.container():
        st.subheader(titulo)
        st.altair_chart(generar_boxplot(df, titulo), use_container_width=True)

# Función para mostrar dos boxplots comparativos
def mostrar_doble_boxplot(df1, df2, titulo1, titulo2):
    min_val = min(df1["Life_exp"].min(), df2["Life_exp"].min())
    max_val = max(df1["Life_exp"].max(), df2["Life_exp"].max())

    box1 = generar_boxplot(df1, titulo1, "blue").encode(y=alt.Y("Life_exp:Q", scale=alt.Scale(domain=[min_val, max_val])))
    box2 = generar_boxplot(df2, titulo2, "red").encode(y=alt.Y("Life_exp:Q", scale=alt.Scale(domain=[min_val, max_val])))

    st.altair_chart(alt.hconcat(box1, box2), use_container_width=True)

# Cargar datos
df = pd.read_csv("OECD.csv", sep=",")

# Título
st.title("Distribución de la Esperanza de Vida")

#Información
st.markdown("Conoceremos la distribución de los datos reflejados en una caja y bigotes, de igual manera podemos seleccionar el año, miembros o no mieembros, género, etc.")

# Selección del año
year = st.radio("Seleccione el año", options=range(2015, 2024), index=8)

# Filtros de agrupamiento
st.write("Opciones de filtrado:")
filter_oecd = st.checkbox("Diferenciar por membresía en la OCDE")
filter_gender = st.checkbox("Diferenciar por género")

st.write("Nota: Para el año 2023 hay registros para menos países que en años anteriores.")

# Filtrar datos por año
df_year = df[df["Year"] == year]

# Mostrar gráficos según los filtros seleccionados
if not filter_oecd and not filter_gender:
    mostrar_boxplot(df_year[df_year["Gender"] == "Total"], "Todos los países")

elif filter_oecd and not filter_gender:
    mostrar_doble_boxplot(
        df_year[(df_year["Gender"] == "Total") & (df_year["OECD"] == True)],
        df_year[(df_year["Gender"] == "Total") & (df_year["OECD"] == False)],
        "Países miembros de la OCDE",
        "Países no miembros"
    )

elif not filter_oecd and filter_gender:
    mostrar_doble_boxplot(
        df_year[df_year["Gender"] == "Male"],
        df_year[df_year["Gender"] == "Female"],
        "Hombres de todos los países",
        "Mujeres de todos los países"
    )

elif filter_oecd and filter_gender:
    st.subheader("Hombres")
    mostrar_doble_boxplot(
        df_year[(df_year["Gender"] == "Male") & (df_year["OECD"] == True)],
        df_year[(df_year["Gender"] == "Male") & (df_year["OECD"] == False)],
        "Países miembros de la OCDE",
        "Países no miembros"
    )

    st.subheader("Mujeres")
    mostrar_doble_boxplot(
        df_year[(df_year["Gender"] == "Female") & (df_year["OECD"] == True)],
        df_year[(df_year["Gender"] == "Female") & (df_year["OECD"] == False)],
        "Países miembros de la OCDE",
        "Países no miembros"
    )

st.page_link("Introducción.py", label="Anterior", icon="⬅️")
st.page_link("Evolucion_de_la_OECD.py", label="Siguiente", icon="➡️")