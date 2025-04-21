import os
from PIL import Image

def converter_para_webp(caminho_imagem, qualidade=90):
    if not os.path.isfile(caminho_imagem):
        print(f"Arquivo não encontrado: {caminho_imagem}")
        return

    with Image.open(caminho_imagem) as img:
        nome_arquivo, _ = os.path.splitext(caminho_imagem)
        novo_caminho = f"{nome_arquivo}.webp"

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(novo_caminho, "WEBP", quality=qualidade, method=6)
        print(f"[✓] Imagem convertida: {novo_caminho}")

def converter_pasta(pasta, qualidade=100):
    formatos = ('.png', '.jpg', '.jpeg')

    if not os.path.isdir(pasta):
        print(f"Pasta não encontrada: {pasta}")
        return

    arquivos_convertidos = 0
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(formatos):
            caminho_completo = os.path.join(pasta, arquivo)
            converter_para_webp(caminho_completo, qualidade)
            arquivos_convertidos += 1

    if arquivos_convertidos == 0:
        print("Nenhuma imagem compatível encontrada na pasta.")
    else:
        print(f"[✓] {arquivos_convertidos} imagem(ns) convertida(s).")

def menu():
    print("====== Conversor de Imagens para WebP ======")
    print("1. Converter imagem individual")
    print("2. Converter todas as imagens de uma pasta")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        caminho = input("Digite o caminho da imagem: ").strip('"')
        converter_para_webp(caminho)
    elif opcao == "2":
        pasta = input("Digite o caminho da pasta: ").strip('"')
        converter_pasta(pasta)
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
