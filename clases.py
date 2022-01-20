class Auto:
    def __init__(self, color = 'Negro', 
                        motor = "MOTOR1", 
                        chasis="AAA", 
                        cantidad_ruedas=4, 
                        direccion="MANUAL"):
        self.color = color
        self.motor = motor
        self.chasis = chasis
        self.cantidad_ruedas = cantidad_ruedas
        self.direccion = direccion
        self.kilometros = 0

    def acelerar(self, kilometros = 5):
        self.kilometros += kilometros
        return self
        
    def mostrarAuto(self):
        print(f"El auto {self.color} - Tiene: {self.kilometros} Kilometros")
        return self

    def tieneColoresIguales(self, otroAuto):
        return self.color == otroAuto.color

    def __str__(self):
        return f"EL AUTO {self.color} TIENE EL MOTOR {self.motor}"

auto1 = Auto(chasis="BBB")
auto1.acelerar().acelerar()
auto1.mostrarAuto()

auto_pancho = Auto(motor="V6",chasis="CCC", cantidad_ruedas=5)
auto_pancho.acelerar().acelerar().acelerar(50).acelerar()
auto_pancho.mostrarAuto()

print(auto1.tieneColoresIguales(auto_pancho))

auto_1 = Auto(motor="V6",chasis="CCC", cantidad_ruedas=5)
auto_1.mostrarAuto()