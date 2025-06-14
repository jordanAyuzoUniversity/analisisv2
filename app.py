import streamlit as st
from backend import load_model, predict_sentiment
from frontend import render_interface

# Esta línea debe ir al inicio, antes de cualquier otro comando de Streamlit
st.set_page_config(page_title="Chat de Sentimientos", page_icon="💬")

model = load_model()
render_interface(model, predict_sentiment)

