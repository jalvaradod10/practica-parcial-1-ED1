with open("ej2//demo.txt","r",encoding="UTF-8") as ar:#esto tirara error
    ar.write("Hola\n")
    ar.write("Mi nombre es Juan")

with open("ej2//demo.txt","r",encoding="UTF-8") as ar:
    print(ar.read())