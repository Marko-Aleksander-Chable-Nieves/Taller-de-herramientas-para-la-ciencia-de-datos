import pandas as pd
import streamlit as st
import altair as alt

# Cargar datos
df = pd.read_csv("OECD.csv")

# Título principal
st.title("Análisis de Esperanza de Vida")

#Información
st.markdown("Identificaremos la evolución de estos datos apartir de la siguiente gráfica, en esta parte es mas especifico, seleccionamos el país que queremos visualizar y puede ser dividido por hombres y mujeres.")

# Sidebar para opciones de filtrado
st.sidebar.header("Filtros")

# Selección de países
paises_disponibles = df["Country"].unique()
paises_seleccionados = st.sidebar.multiselect(
    "Selecciona países",
    options=paises_disponibles,
    default=paises_disponibles[0]  # Selecciona un país por defecto
)

# Opción para diferenciar por género
filtro_genero = st.sidebar.checkbox("Distinguir por género")

# Filtrar datos según la selección
df_filtrado = df[df["Country"].isin(paises_seleccionados)]

if filtro_genero:
    df_visualizacion = df_filtrado[df_filtrado["Gender"] != "Total"]
else:
    df_visualizacion = df_filtrado[df_filtrado["Gender"] == "Total"]

# Verificar que haya datos seleccionados
if not df_visualizacion.empty:
    titulo_grafico = f"Evolución de la Esperanza de Vida en {', '.join(paises_seleccionados)}"
    
    # Crear gráfico con Altair
    grafico = alt.Chart(df_visualizacion).mark_line().encode(
        x=alt.X("Year:O", title="Año"),
        y=alt.Y("Life_exp:Q", title="Esperanza de vida"),
        color=alt.Color("Country:N", legend=alt.Legend(title="País")),
        strokeDash=alt.StrokeDash("Gender:N", legend=alt.Legend(title="Género"))
    ).properties(
        width=800,
        height=400,
        title=titulo_grafico
    )
    
    # Mostrar gráfico en Streamlit
    with st.container():
        st.altair_chart(grafico, use_container_width=True)
else:
    st.warning("No hay datos disponibles para la selección realizada.")

st.page_link("Distribucion_de_la_OECD.py", label="Anterior", icon="⬅️")
