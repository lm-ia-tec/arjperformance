import streamlit as st
from config import APP_NAME, APP_VERSION
from ui.sidebar import render_sidebar
from ui.telas import tela_upload, tela_resultado
from services.motor import MotorAutomacao
from services.transformacoes import ajustar_layout_fortes

# Configuração da página
st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)

st.title(f"{APP_NAME} 🚀")
st.caption(f"Versão {APP_VERSION}")

# Sidebar
estabelecimento, centro_custo, executar = render_sidebar()

# Upload
df = tela_upload()

# Execução
if executar and df is not None:
    st.info("Executando automação...")

    # Ajustes de layout
    df_ajustado = ajustar_layout_fortes(
        df,
        estabelecimento_padrao=estabelecimento,
        centro_padrao=centro_custo
    )

    # Motor
    motor = MotorAutomacao(config={
        "estabelecimento": estabelecimento,
        "centro_custo": centro_custo
    })

    resultado = motor.executar(df_ajustado)

    tela_resultado(resultado)
