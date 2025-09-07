from pathlib import Path

ruta = Path("data") / "transacciones.txt"

busqueda = "Retiro"
encontradas = []

with ruta.open("r", encoding="utf-8") as f:
    for linea in f:
        datos = linea.strip().split(",")
        if datos[2] == busqueda:
            encontradas.append(datos)

print("Transacciones encontradas:", encontradas)
