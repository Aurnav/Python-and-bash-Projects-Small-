#!/bin/bash
Sjunk=("temp","tmp","log","cache",".temp",".tmp","log",".bak",".old",".part",".cache")
Wjunk=("history","thumbnail","thumbs","crash","dump","lock","pid")
Impo=(".pdf",".docx",".xlsx",".odt",".txt",".jpg",".jpeg",".png",".gif",".mp4",".zip",".tar")

echo "Enter Which Directory you would Like to search in "
read Directory
a=$(find $Directory -type d -name "temp")
b=$(find $Directory -type d -name "Temp")
c=$(find $Directory -type d -name "Cache")
d=$(find $Directory -type d -name "cache")
output_a=$( ls  $a)
if
