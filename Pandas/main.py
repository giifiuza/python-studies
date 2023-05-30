import pandas as pd

data = {
    'nome': ['João', 'Paulo', 'Bruna'],
    'idade': [20, 25, 19],
    'altura':[1.90, 1.85, 1.72]
}

df = pd.DataFrame(data)
df.to_excel('C:/Users/37076111837/Desktop/Pandas/pessoas.xlsx')
df.to_csv('C:/Users/37076111837/Desktop/Pandas/pessoas.csv', sep=' ')


