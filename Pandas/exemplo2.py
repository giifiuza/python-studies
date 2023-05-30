import pandas as pd

## Primeiro jeito
'''arquivo = pd.ExcelFile('professores.xlsx')
dframe = pd.read_excel(arquivo, "Sheet1")'''

##Segundo jeito
arquivo = pd.read_excel('professores.xlsx')
prof = arquivo.loc[arquivo['cargo'] == 'PROFESSOR DO MAGISTERIO SUPERIOR']
pro = prof[['nome', 'formacao']]
print(pro)

# nomes = dframe[['nome', 'formacao']]

# print(dframe.loc[2])
# print(nomes.loc[10])


# print(dframe.head())
# print(dframe.head(3))
# print(dframe.shape)
