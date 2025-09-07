from pathlib import Path
ruta=Path("data")/"transacciones.txt"
resu= []
montos=[]
busqueda="2025-09-02"
with ruta.open("r",encoding="UTF-8") as a:
    for s in a:
        datos=s.strip().split(",")
        if datos[1]==busqueda:
            resu.append(datos)
            print(f"ID:{datos[0]} | Fecha:{datos[1]} | Tipo:{datos[2]} | Monto:{datos[3]}")
        con=int(datos[3])
        if con>8000:
            montos.append(datos)
            print(f"ID: {datos[0]} | Fecha: {datos[1]} | Tipo: {datos[2]} | Monto: {datos[3]}")

