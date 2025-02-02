import streamlit as st

pg = st.navigation([
                    st.Page("Introducción.py"), st.Page("Distribucion_de_la_OECD.py"),
                    st.Page("Evolucion_de_la_OECD.py")
                    ])
pg.run()
