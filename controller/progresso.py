import streamlit as st
import pandas as pd
from datetime import datetime

def init_progresso():
    if "progresso" not in st.session_state:
        st.session_state.progresso = []

def registrar_progresso(topico, nota, observacao):
    st.session_state.progresso.append({
        "Data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Tópico": topico,
        "Nota": nota,
        "Observações": observacao
    })

def mostrar_progresso():
    init_progresso()
    if st.session_state.progresso:
        df = pd.DataFrame(st.session_state.progresso)
        st.dataframe(df, use_container_width=True)
        st.line_chart(df.set_index("Data")["Nota"])
    else:
        st.info("Nenhum progresso registrado ainda. Faça uma aula para começar!")
