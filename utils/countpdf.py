import glob
from pathlib import Path
import os

#p = Path('./Trabalho Completo-20240816T181335Z-001/Trabalho Completo/')
p = Path('./Comunicação Cientifica-20240816T181516Z-001/Comunicação Cientifica/')

subfolders = [ f.path for f in os.scandir(p) if f.is_dir() ]
print(subfolders)

count_pdf = 0
path_pdf = []
count_docx = 0
path_docx = []
count_tex = 0
path_tex = []
for folder in subfolders:
    files = [f.path for f in os.scandir(folder) if os.path.isfile(f)]
    if len(files) == 1 and len(glob.glob(os.path.join(folder,"*.pdf"))) == 1:
        count_pdf +=1
        path_pdf.append(folder)
    if len(files) == 1 and len(glob.glob(os.path.join(folder,"*.docx"))) == 1:
        count_docx += 1
        path_docx.append(folder)
    if len(files) > 1 and len(glob.glob(os.path.join(folder,"*.tex"))) > 0:
        count_tex += 1
        path_tex.append(folder)

print('Number of Pdf: ', count_pdf)
print('Number of Docx: ', count_docx)
print('Number of Tex: ', count_tex)
print('Number Total: ', count_pdf+count_docx+count_tex)

not_defineds = subfolders[:]
count = 0
for folder in subfolders:
    if folder in path_pdf or folder in path_docx or folder in path_tex:
    # if folder in path_pdf:
        count += 1
        not_defineds.remove(folder)

print(not_defineds)
print(len(not_defineds))
print(path_tex)
