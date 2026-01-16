import streamlit as st
from controller.progresso import mostrar_progresso, registrar_progresso

st.title("📊 Seu Progresso")
mostrar_progresso()
