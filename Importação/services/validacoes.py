def validar_estabelecimento(valor):
    return valor.isdigit() and len(valor) == 4


def validar_centro_custo(valor):
    return "." in valor and len(valor) >= 5
