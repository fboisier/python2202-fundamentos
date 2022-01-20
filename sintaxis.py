x = 1
if  x == 1:
    print("X es igual a 1")
    if x == 2:
        pass
    else:
        print("X no es igual a 2")
else:
    print("X no es igual a 1")
print("fuera del if")


add10 = lambda x: x + 10 # almacene la expresión lambda en una variable
add10(2)  # retorna 12
add10(98) # re