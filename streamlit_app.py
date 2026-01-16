import streamlit as st

pages = {
  "Início": [
    st.Page("app.py", title="Página Inícal")
  ],
  "Aula": [
    st.Page("pages/class.py", title="Aulas"),
    st.Page("pages/questions.py", title="Questões")
  ],
  "Recursos": [
    st.Page("pages/timeline.py", title="Cronograma"),
    st.Page("pages/progress.py", title="Progresso"),
    st.Page("pages/audio.py", title="Áudio")
  ],
  "Referência": [
    st.Page("pages/reference.py", title="Referência")
  ]
}

pg = st.navigation(pages, position="top")
pg.run()
