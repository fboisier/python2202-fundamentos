lista_animales = [["gato","10"], ["perro","20"], ["elefante","30"]]
lista_animales.append(["tigre","40"])

for animal in lista_animales:
    print(animal)
    for caracteristica in animal:
        print("VALOR DENTRO", caracteristica)
