class Fecha:
    def __init__(self):
        self._dia = 0
        self._mes = 0
        self._año = 0

    def _comprobar_dia(self, dia):
        if dia >= 1 and dia <= 31:
            return True
        else:
            raise ValueError("El número del día debe estar entre 1 y 31")

    def _comprobar_mes(self, mes):
        if mes >= 1 and mes <= 12:
            return True
        else:
            raise ValueError("El número del mes debe estar entre 1 y 12")

    def _comprobar_fecha(self, dia, mes):
        Fecha._comprobar_dia(self, dia)
        Fecha._comprobar_mes(self, mes)

    def modificar_dia(self, dia):
        self._dia = dia
    
    def modificar_mes(self, mes):
        self._mes = mes

    def modificar_año(self, año):
        self._año = año

    def modificar_fecha(self, dia, mes, año):
        Fecha._comprobar_fecha(self, dia, mes)
        self.modificar_dia(dia)
        self.modificar_mes(mes)
        self.modificar_año(año)

    def devolver_dia(self):
        return self._dia
    
    def devolver_mes(self):
        return self._mes
    
    def devolver_año(self):
        return self._año
    
    def __str__(self) -> str:
        return f"{self.devolver_dia()}/{self.devolver_mes()}/{self.devolver_año()}"

fechas = Fecha()
dia = int(input("Dime un dia: "))
mes = int(input("Dime un mes: "))
año = int(input("Dime un año: "))
fechas.modificar_fecha(dia, mes, año)
print(fechas)   