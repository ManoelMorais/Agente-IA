import streamlit as st

def add_to_history(role, text):
    st.session_state.history.append(
        {"role": role, "parts": [{"text": text}]}
    )

def init_history(system_prompt):
    if "history" not in st.session_state:
        st.session_state.history = [
            {"role": "system", "parts": [{"text": system_prompt}]}
        ]
