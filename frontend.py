import streamlit as st

def render_interface(model, predict_fn):
    st.set_page_config(page_title="Chat de Sentimientos", page_icon="💬")
    st.title("Chat de Análisis de Sentimientos")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar historial
    for entry in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(entry["user"])
        with st.chat_message("assistant"):
            st.markdown(entry["bot"], unsafe_allow_html=True)

    user_input = st.chat_input("Escribe tu mensaje...")

    if user_input:
        # Mostrar mensaje del usuario
        st.chat_message("user").markdown(user_input)

        # Comando especial /info
        if user_input.strip().lower() == "/info":
            info_msg = (
                "📘 **Información del modelo:**  \n"
                "Este modelo fue desarrollado usando la técnica de *stacking* como parte de un proyecto "
                "para la materia **Reconocimiento de Patrones** en la **Universidad Tecnológica de la Mixteca**.  \n\n"
                "🔤 Está diseñado para analizar opiniones escritas en **inglés**."
            )
            bot_response = info_msg
        else:
            prediction = predict_fn(model, user_input)
            sentiment = "Positivo" if prediction == 1 else "Negativo"
            icon = "✅" if prediction == 1 else "❌"
            bot_response = f"{icon} Sentimiento **{sentiment.upper()}**"

        # Mostrar respuesta del bot
        st.chat_message("assistant").markdown(bot_response, unsafe_allow_html=True)

        # Guardar en historial
        st.session_state.chat_history.append({
            "user": user_input,
            "bot": bot_response
        })

    # Botón para limpiar conversación
    if st.button("🧹 Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()
