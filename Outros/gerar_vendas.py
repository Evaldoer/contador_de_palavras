"""Gera o arquivo vendas.csv com dados de exemplo."""
import numpy as np
import pandas as pd

np.random.seed(42)
datas = pd.date_range('2025-01-01', '2025-06-30', freq='D')
produtos = ['A', 'B', 'C', 'D', 'E']
dados = {
    'data': np.random.choice(datas, 100),
    'produto': np.random.choice(produtos, 100),
    'quantidade': np.random.randint(1, 10, 100),
    'preço': np.random.uniform(5.0, 50.0, 100),
}

df = pd.DataFrame(dados)
df.to_csv('vendas.csv', index=False)
print('Arquivo vendas.csv criado com sucesso!')
