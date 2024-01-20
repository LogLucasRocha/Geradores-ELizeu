import pandas as pd

caminho_arquivo_csv = 'data.csv'

dados_csv = pd.read_csv(caminho_arquivo_csv, sep=',')

caminho_saida_excel = 'saida_excel.xlsx'

dados_csv.to_excel(caminho_saida_excel, index=False)