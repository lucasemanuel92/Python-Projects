# Projeto para organizar uma determinada pasta de acordo com suas extensões

import os
from tkinter.filedialog import askdirectory # Escolhemos um pacote e importamos uma função dela

path = askdirectory(title="Selecione uma pasta") # Mostra o caminho onde está a pasta que quero executar

archive_list = os.listdir(path) # Criar uma lista de arquivos com o caminho selecionado anteriormente

local = {
    "Imagens" : [".png", ".jpeg"], # Nome da Pasta : [.extensões que eu quero nessa pasta]
    "Planilhas" : [".xlsx"],
    "PDFs" : [".pdf", ".rtf"],
    "csv" : [".csv"]
}

for archive in archive_list:
    # Vai até o arquivo e quebra o texto em nome e extensão
    name, extension = os.path.splitext(f"{path}/{archive}")
    # Ir em cada pasta e verificar as extensões
    for folder in local:
        # Verificar se as extensões estão em cada pasta
        if extension in local[folder]:
            # Verificar se já existem pastas desse tipo
            if not os.path.exists(f"{path}/{folder}"):
                # Se não existir, criar essa pasta
                os.mkdir(f"{path}/{folder}")
            # Mudar o caminho para chegar até o arquivo
            os.rename(f"{path}/{archive}", f"{path}/{folder}/{archive}") 