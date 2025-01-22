import streamlit as st
import pandas as pd
import altair as alt


pg = st.navigation([st.Page("Indicadores_de_calidad_de_vida.py"), st.Page("Tabla_de_datos.py"),st.Page("Grafica_de_barras.py"),
                    st.Page("Histograma.py"), st.Page("Grafica_de_caja.py"), st.Page("Grafica_de_dispersion.py")])
pg.run()
