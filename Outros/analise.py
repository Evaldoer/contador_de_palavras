from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PASTA = Path(__file__).resolve().parent
ARQUIVO_CSV = PASTA / 'vendas.csv'

# 1. Carregar dados
df = pd.read_csv(ARQUIVO_CSV, parse_dates=['data'])
df['receita'] = df['quantidade'] * df['preço']

# 2. Total de vendas por mês
df['mes'] = df['data'].dt.to_period('M')
vendas_por_mes = df.groupby('mes')['receita'].sum()
print('Vendas por mês:')
print(vendas_por_mes)

# 3. Produto mais vendido e maior receita
vendas_prod = df.groupby('produto').agg({'quantidade': 'sum', 'receita': 'sum'})
mais_vendido = vendas_prod['quantidade'].idxmax()
maior_receita = vendas_prod['receita'].idxmax()

print(f'\nProduto mais vendido: {mais_vendido} ({vendas_prod.loc[mais_vendido, "quantidade"]} unidades)')
print(f'Produto com maior receita: {maior_receita} (R$ {vendas_prod.loc[maior_receita, "receita"]:.2f})')

# 4. Gráfico de vendas por mês
vendas_por_mes_plot = vendas_por_mes.copy()
vendas_por_mes_plot.index = vendas_por_mes_plot.index.astype(str)
plt.figure(figsize=(6, 4))
vendas_por_mes_plot.plot(kind='bar', color='skyblue')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Receita (R$)')
plt.tight_layout()
plt.savefig(PASTA / 'vendas_por_mes.png')
plt.close()

# 5. Gráfico dos 5 principais produtos por receita
top5 = vendas_prod.nlargest(5, 'receita')
plt.figure(figsize=(6, 4))
plt.bar(top5.index, top5['receita'], color='orange')
plt.title('Top 5 Produtos por Receita')
plt.ylabel('Receita (R$)')
plt.xlabel('Produto')
plt.tight_layout()
plt.savefig(PASTA / 'top5_produtos.png')
plt.close()

print('\nGráficos salvos: vendas_por_mes.png e top5_produtos.png')

# 6. Gerar relatório HTML
html_conteudo = f"""
<html>
<head>
    <meta charset="UTF-8">
    <title>Relatório de Vendas</title>
</head>
<body>
    <h1>Relatório de Vendas Mensais</h1>
    <h2>Resumo</h2>
    <p><b>Produto mais vendido:</b> {mais_vendido} ({vendas_prod.loc[mais_vendido, "quantidade"]} unidades)</p>
    <p><b>Produto com maior receita:</b> {maior_receita} (R$ {vendas_prod.loc[maior_receita, "receita"]:.2f})</p>

    <h2>Vendas por mês</h2>
    {vendas_por_mes.to_frame().to_html()}

    <h2>Gráfico de Vendas por Mês</h2>
    <img src="vendas_por_mes.png" width="500">

    <h2>Top 5 Produtos por Receita</h2>
    <img src="top5_produtos.png" width="500">
</body>
</html>
"""

with open(PASTA / "relatorio.html", "w", encoding="utf-8") as f:
    f.write(html_conteudo)

print("\nRelatório HTML gerado: relatorio.html")
