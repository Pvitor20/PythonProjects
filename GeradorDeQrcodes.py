import qrcode
import os

# Solicita o link ou conteúdo que será transformado em QR code
data = input("Cole o link ou conteúdo que deseja transformar em QR code: ")

# Solicita o caminho onde o QR code será salvo
path = input("Cole o caminho onde deseja salvar o QR code: ")

# Verifica se o diretório existe, caso contrário, cria
if not os.path.exists(path):
    try:
        os.makedirs(path)
    except OSError as e:
        print(f"Erro ao criar o diretório: {e}")
        exit()

# Solicita o nome do arquivo e garante a extensão .png
file_name = input("Digite o nome do arquivo (sem extensão): ")
if not file_name.endswith('.png'):
    file_name += '.png'

# Caminho completo para salvar o QR code
img_path = os.path.join(path, file_name)

# Gera o QR code e salva o arquivo
try:
    img = qrcode.make(data)
    img.save(img_path)
    print(f"QR code gerado com sucesso e salvo em: {img_path}")
except Exception as e:
    print(f"Erro ao salvar o QR code: {e}")