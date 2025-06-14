import streamlit as st

def render_interface(model, predict_fn):
    st.markdown("""
    <style>
    .sticky-title {
    position: sticky;
    top: 0;
    background-color: inherit;
    color: white;
    z-index: 100;
    padding: 0.5rem 0;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 600;
    border-bottom: 1px solid #ccc;
    }
    .positive-response {
    background-color: #d4edda;
    color: black;
    padding: 0.8rem 1rem;
    border-radius: 10px;
    display: inline-block;
    }
    .negative-response {
    background-color: #f8d7da;
    color: black;
    padding: 0.8rem 1rem;
    border-radius: 10px;
    display: inline-block;
    }
    </style>
    <div class="sticky-title">Chat de Análisis de Sentimientos</div>
    """, unsafe_allow_html=True)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar el historial con burbujas tipo mensajería
    for entry in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(entry["user"])

        with st.chat_message("assistant"):
            if entry["sentiment"] == "positive":
                st.markdown(
                    "<div class='positive-response'>✅ Sentimiento <strong>POSITIVO</strong></div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div class='negative-response'>❌ Sentimiento <strong>NEGATIVO</strong></div>",
                    unsafe_allow_html=True
                )

    # Entrada del usuario
    user_input = st.chat_input("Escribe tu mensaje para analizar el sentimiento...")

    if user_input:
        prediction = predict_fn(model, user_input)
        sentiment_label = "positive" if prediction == 1 else "negative"

        # Guardar en el historial
        st.session_state.chat_history.append({
            "user": user_input,
            "sentiment": sentiment_label
        })

        st.rerun()

    # Botón para limpiar conversación
    if st.button("🧹 Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()