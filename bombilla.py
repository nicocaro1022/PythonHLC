class Bombilla:
    def __init__(self):
        self.encendido = False
        self.contador = 0
        self.fundido = False

    def encender(self):
        if self.fundido:
            print("La bombilla esta fundida.")
        elif self.encendido:
            print("La bombilla ya estaba encendida.")
        else:
            self.contador += 1
            self.encendido = True
            if self.contador == 1000:
                self.fundido = True
                print("La bombilla se ha fundido.")
        
    def apagar(self):
        if self.fundido:
            print("La bombilla esta fundida.")
        elif not self.encendido:
            print("La bombilla ya estaba apagada.")
        else:
            self.encendido = False

    def __str__(self) -> str:
        return f"{self.contador}"
    
b = Bombilla()
for i in range(1000):
    b.encender()
    b.apagar()
print(b)