import pandas as pd


arquivo = pd.read_excel('professores.xlsx')
# profs = arquivo.loc[2,'cargo']
# print(profs)

tamanho = len(arquivo)
print(tamanho)
arquivo['idade'] = ""
for i in range(0, tamanho):
    j = arquivo.loc[i,'nome']
    k = int(input(f'Idade de {j}: '))
    arquivo.loc[i, 'idade'] = k


print(arquivo)
