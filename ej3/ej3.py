try:
    with open("ej3//fake.txt","r",encoding="UTF-8") as ar:
        ar.read()
except Exception as e:
    print(f"El error es: {e}")
    with open("ej3//fake.txt","w",encoding="UTF-8") as artrue:
        artrue.write("Creando archivo que no existia")
with open("ej3//fake.txt","r",encoding="UTF-8") as ar:
        print(ar.read())