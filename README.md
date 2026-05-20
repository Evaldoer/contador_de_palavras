# Contador de Palavras

Aplicacao web simples para contar palavras, calcular operacoes basicas e visualizar estatisticas do arquivo `dados.csv`.

O projeto nasceu como scripts Python de estudo e agora tambem possui uma interface estatica pronta para deploy na Vercel, sem etapa de build e sem dependencias de servidor.

## Funcionalidades

- Contador de palavras com ranking das 10 palavras mais frequentes.
- Calculadora de operacoes basicas.
- Leitura do arquivo `dados.csv`.
- Calculo de media, mediana e desvio padrao.
- Grafico de dispersao em canvas.

## Estrutura

```text
contador_de_palavras/
|-- index.html
|-- styles.css
|-- app.js
|-- dados.csv
|-- api/index.py
|-- vercel.json
|-- calculator.py
|-- contador.py
|-- parse.py
|-- requirements.txt
`-- README.md
```

## Executar localmente

Como a aplicacao web e estatica, basta servir a pasta do projeto:

```bash
python -m http.server 8000
```

Depois acesse:

```text
http://localhost:8000
```

## Gerar build local

O build usado pela Vercel copia apenas os arquivos da aplicacao web para `dist`:

```bash
node scripts/build-static.js
```

## Deploy na Vercel

1. Envie o repositorio para o GitHub.
2. Na Vercel, importe o repositorio.
3. A configuracao do deploy ja esta no `vercel.json`:
   - Framework Preset: Other
   - Install Command: `echo No install needed`
   - Build Command: `node scripts/build-static.js`
   - Output Directory: `dist`
4. Clique em Deploy.

A configuracao `vercel.json` evita instalar dependencias Python, publica os arquivos estaticos gerados em `dist` e tambem possui rotas para funcionar caso a Vercel importe o projeto com preset Python.

## Scripts Python

Os scripts originais continuam disponiveis para estudo local:

```bash
pip install -r requirements-local.txt
python contador.py
python calculator.py
python parse.py
```

O `requirements.txt` principal fica minimo porque a Vercel le esse arquivo durante o deploy Python. As dependencias dos estudos locais ficam em `requirements-local.txt`.
