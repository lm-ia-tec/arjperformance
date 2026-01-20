def ajustar_layout_fortes(df, estabelecimento_padrao, centro_padrao):
    df["Estabelecimento"] = df.get("Estabelecimento", estabelecimento_padrao)
    df["CentroCusto"] = df.get("CentroCusto", centro_padrao)

    return df
