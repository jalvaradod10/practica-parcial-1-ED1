from pathlib import Path
transacciones= []
ruta= Path("data")/"transacciones.txt"
with ruta.open("r",encoding="UTF-8")as r:
    for linea in r:
        lol= linea.strip().split()
        transacciones.append(lol)
print(transacciones)