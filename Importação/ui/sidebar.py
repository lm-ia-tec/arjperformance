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

    # Rodapé da barra lateral
    st.sidebar.markdown(
        """
        <div style="
            position: absolute;
            bottom: 10px;
            width: 90%;
            text-align: center;
            font-size: 0.9em;
            color: gray;
        ">
            Versão 1.0<br>
            Desenvolvido por Lucas Marques
        </div>
        """,
        unsafe_allow_html=True
    )




