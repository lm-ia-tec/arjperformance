import streamlit as st
import pandas as pd

def tela_upload():
    st.header("📂 Importação de Planilha")

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
        st.dataframe(df)

        return df

    return None


def tela_resultado(resultado):
    st.header("📊 Resultado da Automação")

    st.write("Status:", resultado["status"])
    st.write("Linhas processadas:", resultado["linhas_processadas"])

    if resultado["erros"]:
        st.error("Erros encontrados")
        st.write(resultado["erros"])
    else:
        st.success("Processamento concluído sem erros")
