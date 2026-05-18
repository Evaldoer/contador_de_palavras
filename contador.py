# Programa para contar palavras em um arquivo de texto

# 1. Pedir o caminho do arquivo
# 2. Ler o conteúdo
# 3. Separar palavras
# 4. Contar total
# 5. Mostrar palavras mais frequentes

import re
from collections import Counter

STOPWORDS = {"de", "a", "o", "e", "do", "da", "é"}

def contar_palavras(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()

        palavras = re.findall(r'\b\w+\b', texto.lower())

        palavras = [p for p in palavras if p not in STOPWORDS]

        total = len(palavras)

        contador = Counter(palavras)
        mais_comuns = contador.most_common(10)

        print(f"\nTotal de palavras: {total}")
        print("\nPalavras mais frequentes:")
        for palavra, qtd in mais_comuns:
            print(f"{palavra}: {qtd}")

    except FileNotFoundError:
        print("Arquivo não encontrado!")


# 👇 FORA da função
def main():
    caminho = input("Digite o caminho do arquivo: ")
    contar_palavras(caminho)


if __name__ == "__main__":
    main()