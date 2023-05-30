import pandas as pd

pro = pd.read_excel('professores.xlsx')

linhas = len(pro)

pro.loc[linhas+1, 'siape'] = int(input("ID: "))
pro.loc[linhas+1, 'nome'] = str(input("nome: "))
pro.loc[linhas+1, 'formacao'] = str(input("formacao: "))

pro.to_excel('professores.xlsx', index=False)