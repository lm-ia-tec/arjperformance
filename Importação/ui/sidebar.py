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

    st.sidebar.markdown("---")

    # Rodapé
    st.sidebar.markdown(
        """
        **Versão:** 1.0  
        **Desenvolvido por:** Lucas Marques
        """
    )


