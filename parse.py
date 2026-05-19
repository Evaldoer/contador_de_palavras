import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os

# 📁 Caminho do CSV
caminho = os.path.join(os.path.dirname(__file__), 'dados.csv')

# 📊 Ler CSV
df = pd.read_csv(caminho)

# 🔎 Verificação de colunas
if 'col1' not in df.columns or 'col2' not in df.columns:
    print("❌ O CSV precisa conter col1 e col2")
    exit()

# 📈 Estatísticas apenas numéricas
numericos = df.select_dtypes(include='number')

media = numericos.mean()
mediana = numericos.median()
desvio = numericos.std()

print("📊 Média:")
print(media)

print("\n📊 Mediana:")
print(mediana)

print("\n📊 Desvio padrão:")
print(desvio)

# 💾 Banco de dados SQLite
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS resultados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    media_col1 REAL,
    mediana_col1 REAL,
    desvio_col1 REAL
)
''')

cursor.execute('''
INSERT INTO resultados (media_col1, mediana_col1, desvio_col1)
VALUES (?, ?, ?)
''', (
    df['col1'].mean(),
    df['col1'].median(),
    df['col1'].std()
))

conn.commit()
conn.close()

print("\n✅ Dados salvos no banco de dados (dados.db)")

# 📊 Gráfico
plt.scatter(df['col1'], df['col2'])
plt.xlabel('col1')
plt.ylabel('col2')
plt.title('Gráfico de Dispersão')
plt.grid(True)
plt.show()