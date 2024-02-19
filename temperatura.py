class Temperatura:
    def __init__(self, fecha, tempmin, tempmax):
        self.fecha = fecha
        self.tempmin = tempmin
        self.tempmax = tempmax
    
    def modificar_temp(self, min_nueva, max_nueva):
        self.tempmin = min_nueva
        self.tempmax = max_nueva
    
    def devolver_max(self):
        return self.tempmax
    
    def devolver_min(self):
        return self.tempmin
    
    def devolver_temp_media(self):
        return ((self.tempmax + self.tempmin)/2)
    
    def __str__(self) -> str:
        return f"Fecha: {self.fecha}. Temperatura Máxima: {self.devolver_max()}ºC. Temperatura Mínima: {self.devolver_min()}ºC. Temperatura Media: {self.devolver_temp_media()}ºC."
    
tempmax = 25
tempmin = 10
fecha = "12/10/2024"
t1 = Temperatura(fecha, tempmin, tempmax)
print(t1)