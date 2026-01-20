import streamlit as st
import pandas as pd

def tela_upload_e_execucao():
    st.header("📥 Conversão de Planilha")

    arquivo = st.file_uploader(
        "Selecione o arquivo (Excel ou CSV)",
        type=["xlsx", "csv"]
    )

    if arquivo:
        if arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo, sep=";")
        else:
            df = pd.read_excel(arquivo)

        st.success("Arquivo carregado com sucesso")
        st.dataframe(df, use_container_width=True)

        st.markdown("---")

        executar = st.button(
            "⚙️ Executar automação",
            type="primary"
        )

        return df, executar

    return None, False


def tela_resultado(resultado):
    st.header("📊 Resultado")

    st.write("**Status:**", resultado["status"])
    st.write("**Linhas processadas:**", resultado["linhas_processadas"])

    if resultado["erros"]:
        st.error("Erros encontrados")
        st.write(resultado["erros"])
    else:
        st.success("Processamento concluído com sucesso")

