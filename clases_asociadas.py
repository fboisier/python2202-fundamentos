class Perfil:
    def __init__(self, sobrenombre, rol, imagen):
        self.sobrenombre = sobrenombre
        self.rol = rol
        self.imagen = imagen


perfil_pancho = Perfil("Pancho","Usuario","https://algunaimagen.com/perfil1.png")
print(perfil_pancho.rol)


class Persona:
    def __init__(self, nombre, apellido, genero, sobrenombre, rol, imagen):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.perfil =  Perfil(sobrenombre,rol,imagen)


francisco = Persona("Francisco",
                    "Boisier",
                    "Masculino",
                    "Pancho",
                    "Usuario",
                    "perfil.png")

print(francisco.nombre)
print(francisco.perfil.imagen)