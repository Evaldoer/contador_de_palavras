import argparse
from pathlib import Path

# Definir categorias
categorias = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
}

# Criar mapa extensão -> categoria
extensao_para_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extensao_para_categoria[ext.lower()] = categoria

# Configurar argparse
parser = argparse.ArgumentParser(description="Organizador de Arquivos")
parser.add_argument("--pasta", type=str, required=True, help="Caminho da pasta a organizar")
args = parser.parse_args()

pasta_alvo = Path(args.pasta)

# Listar arquivos
arquivos = [f for f in pasta_alvo.iterdir() if f.is_file()]

for arquivo in arquivos:
    ext = arquivo.suffix.lower()
    categoria = extensao_para_categoria.get(ext, "Outros")
    destino = pasta_alvo / categoria
    destino.mkdir(exist_ok=True)
    arquivo.rename(destino / arquivo.name)
    print(f"Movido {arquivo.name} para {categoria}/")
