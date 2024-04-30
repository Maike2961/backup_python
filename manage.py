from tkinter.filedialog import askdirectory
import shutil
import os 
from datetime import datetime

#listar arquivos e pasta do diretorio selecionado
caminho_arquivo_selecionado = askdirectory()
nomes_arquivos = os.listdir(caminho_arquivo_selecionado)

#fazer backup dos arquivos que estao nessa pasta
nome_pasta_backup = 'backup'
caminho_pasta_backup = f'{caminho_arquivo_selecionado}/{nome_pasta_backup}'

if not os.path.exists(caminho_pasta_backup):
    os.mkdir(caminho_pasta_backup)

data_atual = datetime.now().strftime("%Y-%m-%d, %H-%M-%S")


for arq in nomes_arquivos:
    print(arq)
    caminho_arquivo_completo = f'{caminho_arquivo_selecionado}/{arq}'
    caminho_final_backup = f'{caminho_pasta_backup}/{data_atual}/{arq}'
    
    if not os.path.exists(f"{caminho_pasta_backup}/{data_atual}"):
        os.mkdir(f"{caminho_pasta_backup}/{data_atual}")
    
    if "." in arq:
        shutil.copy2(caminho_arquivo_completo, caminho_final_backup)
    elif "backup" != arq:
        shutil.copytree(caminho_arquivo_completo, caminho_final_backup)
