import streamlit as st

def render_sidebar():
    st.sidebar.title("🔹ARJ Contabilidade🔹")
    st.sidebar.markdown(
        """
        **Plataforma de Automação**

        - Preparação de Layouts
        - Validação de dados
        - Automação contábil
        """
    )

    st.sidebar.markdown(
    "<div style='text-align: center; font-size: 0.9em;'>"
    "<b>Versão:</b> 1.0<br>"
    "<b>Desenvolvido por:</b> Lucas Marques"
    "</div>",
    unsafe_allow_html=True
)




