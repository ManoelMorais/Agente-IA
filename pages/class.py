import streamlit as st
from controller.history import add_to_history, init_history
from controller.ai_client import gerar_resposta
from controller.progresso import mostrar_progresso, registrar_progresso
from config.prompt import system_prompt

st.title("💬 Aula com seu professor")
init_history(system_prompt())

for msg in st.session_state.history: 
  if msg["role"] == "user": 
      st.chat_message("user").write(msg["parts"][0]["text"])
  elif msg["role"] == "model":
    st.chat_message("assistant").write(msg["parts"][0]["text"])

user_input = st.chat_input("Digite sua mensagem...")

if user_input:
  st.chat_message("user").write(user_input)
  add_to_history("user", user_input)
  placeholder = st.chat_message("assistant").empty()
  placeholder.write("⏳ Pensando...")
  response = gerar_resposta(st.session_state.history)
  resposta_texto = response.text
  placeholder.write(resposta_texto)
  add_to_history("model", resposta_texto)
  registrar_progresso("Aula prática", 8.0, "Interação concluída com sucesso")
