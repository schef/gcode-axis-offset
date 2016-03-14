#!/usr/bin/env python
import re, sys

filename = sys.argv[1]
axis = sys.argv[2]
offset = float(sys.argv[3])

with open(filename) as f:
        lista_linija = f.read().splitlines() 


for line in lista_linija:
  for word in line.split(" "):
    if (re.search(axis + ".*", word)):
      print(axis + str(round(float(word[1:]) + offset,4)),end=" ")
    else:
      print(word, end=" ")
  print()
