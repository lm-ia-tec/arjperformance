import streamlit as st
from ui.sidebar import render_sidebar
from ui.telas import tela_upload_e_execucao, tela_resultado
from services.motor import MotorAutomacao

st.set_page_config(
    page_title="Automação Fortes Contábil",
    layout="wide"
)

st.title("Automação Fortes Contábil 🚀")

# Sidebar apenas informativa
render_sidebar()

# Tela principal
df, executar = tela_upload_e_execucao()

# Execução da automação
if executar and df is not None:
    with st.spinner("Executando automação..."):
        motor = MotorAutomacao()
        resultado = motor.executar(df)

    tela_resultado(resultado)

def rodape():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            font-size: 0.9em;
            color: gray;
            padding: 5px 0;
            background-color: #f0f2f6; /* cor de fundo leve */
        }
        </style>
        <div class="footer">
            Versão 1.0 | Desenvolvido por Lucas Marques
        </div>
        """,
        unsafe_allow_html=True
    )

# Chame no final do app
rodape()
