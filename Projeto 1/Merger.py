# Projeto para juntar pdfs em determinada ordem

import PyPDF2
import os

merger = PyPDF2.PdfMerger()

archive_list = os.listdir("Projeto 1/pdf")
archive_list.sort() #Colocar em ordem

for archive in archive_list: # Para cada arquivo (elemento dentro da lista)
    if ".pdf" in archive: # Verificar se existe o que foi deteriminado está presente no elemento
        merger.append(f"Projeto 1/pdf/{archive}")

merger.write("Complete Workout.pdf")