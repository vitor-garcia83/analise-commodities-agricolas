# src/utils.py
def limpar_valor_ibge(df, coluna):
    """
    Remove traços e pontos de milhar de uma coluna do IBGE e converte para float.
    """
    df[coluna] = df[coluna].replace('-', '0')
    df[coluna] = df[coluna].str.replace('.', '', regex=False).astype(float)
    return df