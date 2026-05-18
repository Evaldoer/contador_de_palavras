import pandas as pd
import matplotlib.pyplot as plt

# Ler arquivo
df = pd.read_csv('dados.csv')

# Estatísticas
print("Média:")
print(df.mean())

print("\nMediana:")
print(df.median())

print("\nDesvio padrão:")
print(df.std())

# Gráfico
plt.scatter(df['col1'], df['col2'])
plt.xlabel('col1')
plt.ylabel('col2')
plt.title('Gráfico de Dispersão')
plt.show()