import streamlit as st

def render_sidebar():
    st.sidebar.title("⚙️ Configurações")

    estabelecimento = st.sidebar.text_input(
        "Estabelecimento (9999)",
        value="0001",
        max_chars=4
    )

    centro_custo = st.sidebar.text_input(
        "Centro de Custo (999.99)",
        value="999.99"
    )

    executar = st.sidebar.button("🚀 Executar Automação")

    return estabelecimento, centro_custo, executar
