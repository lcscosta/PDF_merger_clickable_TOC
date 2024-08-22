#!/usr/bin bash

foldernumber=$1
foldername="PPT-eposter-trab-aceito-000${foldernumber}"
filename="$2"
cd $foldername
pdflatex "./$filename" --interaction=nonstopmode
bibtex "./$filename"
pdflatex "./$filename" --interaction=nonstopmode
pdflatex "./$filename" --interaction=nonstopmode
