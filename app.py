import streamlit as st
from controller.history import add_to_history, init_history
from controller.ai_client import gerar_resposta
from controller.progresso import mostrar_progresso, registrar_progresso
from config.prompt import system_prompt

# 🌐 Configuração da página
st.set_page_config(layout="wide", page_title="Professor de Idiomas")

col1, col2 = st.columns([1,4])
with col1:
     st.image("assets/StudyWords.png", width=300)
with col2:
    st.title("📚 Bem-vindo ao seu professor particular de idioma.")
st.markdown("""
    Olá! 👋 Este é seu espaço para aprender idiomas de forma natural e personalizada.

    - Converse com seu professor particular  
    - Aprenda com temas que você gosta  
    - Evolua no seu ritmo  

    Clique no menu superior para começar sua aula!
""")
