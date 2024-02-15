import pandas as pd
from bs4 import BeautifulSoup

# Ler os dados HTML do arquivo file.txtgo 
with open('file.txt', 'r', encoding='utf-8') as file:
    html_data = file.read()

# Analisar o HTML
soup = BeautifulSoup(html_data, 'html.parser')

# Extrair dados da tabela
table_rows = soup.select('.table_row')
data = []

# Extrair o cabeçalho da tabela
header_row = table_rows[0]
header_cols = header_row.find_all(['div', 'span'])
selected_positions = [0, 1, 2, 3, 4, 6]
header_cols = [header_cols[i].text.strip() for i in selected_positions]

# Posições específicas para extrair da tabela, Visits, Registrations, FTDs, QFTDs e RevShare
positions_if_consistent = [0, 1, 2, 3, 4, 6]
positions_if_not_consistent = [0, 1, 4, 7, 10, 19]

# Iterar sobre as linhas da tabela, começando da 4 linha (3 linhas iniciais são de totais)
for row in table_rows[4:]:
    cols = row.find_all(['div', 'span'])
    cols = [col.text.strip() for col in cols]

    # Verificar se o número de colunas no cabeçalho é igual ao número de colunas nos dados
    if len(header_cols) == len(cols):
        # Extrair apenas as posições específicas
        selected_cols = [cols[i] for i in positions_if_consistent]
        # Adicionar o filtro Visits > 0 ou terminar em an-
        if selected_cols[1].isdigit() and int(selected_cols[1]) > 0 or selected_cols[0].endswith('an-'):
            data.append(selected_cols)
    else:
        # Extrair apenas as posições específicas das demais linhas
        selected_cols = [cols[i] for i in positions_if_not_consistent]
        # Adicionar o filtro Visits > 0 ou terminar em an-
        if selected_cols[1].isdigit() and int(selected_cols[1]) > 0 or selected_cols[0].endswith('an-'):
            data.append(selected_cols)

# Imprimir dados
for i, row in enumerate(data):
    print(f"Row {i + 1}: {row}")

# Criar um DataFrame pandas
df = pd.DataFrame(data, columns=header_cols)

# Escrever para um arquivo Excel
df.to_excel('output.xlsx', index=False)

import random as rd

