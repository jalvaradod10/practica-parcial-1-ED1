from pathlib import Path
ruta=Path("data")/"ejemplo.txt"
with ruta.open("r",encoding="UTF-8")as b:
    print(b.read())

with ruta.open("a", encoding="utf-8") as f:
    f.write("Línea agregada al final\n")

print("Se agregó una línea en:", ruta)

