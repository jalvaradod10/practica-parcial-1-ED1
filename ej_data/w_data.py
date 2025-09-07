from pathlib import Path
ruta_relativa = Path("data") / "nuevo.txt"
print("Ruta relativa:", ruta_relativa)
print("Ruta absoluta:", ruta_relativa.resolve())
with ruta_relativa.open("w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

print("Archivo creado en:", ruta_relativa)
