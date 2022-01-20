def for_bucles():
    
    my_dict = { "name": "Noelle", "language": "Python" }
    for k in my_dict:
        print(k)

    for key, val in my_dict.items():
        print(key, " = ", val)        

for_bucles()








def saludar():
    print("Hola mundo")

saludar()
saludar()
saludar()
saludar()
saludar()

def saludar_nombre(nombre):
    print(f"Hola {nombre}")

saludar_nombre("Francisco")
saludar_nombre("Pancho")
saludar_nombre("Javier")


def sumar(num1, num2):
    return num1 + num2

resultado = sumar(1,4)
print(resultado)
print(sumar(1,19))





def zapatos(color, tela):
    return f"el zapato es de color {color} y de tela {tela}"

zapato1 = zapatos("rojo", "algodon")
print(zapato1)

zapato2 = zapatos("negro", "plastico")
print(zapato2)



# valores predeterminados

def zapatos(color = "rosado", tela = "algodon"):
    return f"el zapato es de color {color} y de tela {tela}"

zapato1 = zapatos("rojo", "algodon")
print(zapato1)

zapato2 = zapatos("negro", "plastico")
print(zapato2)

zapato3 = zapatos("AZUL")
print(zapato3)

zapato4 = zapatos()
print(zapato4)

zapato5 = zapatos(tela = "gamuza")
print(zapato5)


stacks = 10
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')


resultado = 'Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!'
print(resultado)

resultado = 10 if stacks >= 3 else 20