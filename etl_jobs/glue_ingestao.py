import pandas as pd
import os

def etl_glue():

    # Obtendo o diretório atual do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Caminho para o arquivo Excel
    caminho_arquivo_excel = os.path.join(diretorio_atual, "Fevereiro.xlsx")

    # Leitura do arquivo Excel
    df_excel = pd.read_excel(caminho_arquivo_excel)

    # Por exemplo, você pode renomear colunas, fazer conversões de tipos de dados, etc.
    # Aqui está um exemplo de renomear colunas
    df_excel = df_excel.rename(columns={"Nomes": "nom_cliet"})
    df_excel = df_excel.rename(columns={"Valores": "vlr_compr"})

    # Salvar os dados tratados em um arquivo CSV
    caminho_arquivo_csv = os.path.join(diretorio_atual, "Fevereiro.csv")
    df_excel.to_csv(caminho_arquivo_csv, index=False)
    return df_excel
