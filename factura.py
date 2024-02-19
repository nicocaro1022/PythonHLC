class Factura:
    def __init__(self, codigo_producto, descripcion_producto, precio_producto, 
                 nombre_cliente, apellidos_cliente, direccion_cliente, dni_cliente, unidades):
        self.codigo_producto = codigo_producto
        self.descripcion_producto = descripcion_producto
        self.precio_producto = precio_producto
        self.nombre_cliente = nombre_cliente
        self.apellidos_cliente = apellidos_cliente
        self.direccion_cliente = direccion_cliente
        self.dni_cliente = dni_cliente
        self.unidades = unidades

    def calcular_importe_total(self, iva=0.21):
        subtotal = self.precio_producto * self.unidades
        impuesto = subtotal * iva
        total = subtotal + impuesto
        return total

    def generar_informe(self):
        informe = f"Factura:\n" \
                   f"Código producto: {self.codigo_producto}\n" \
                   f"Descripción producto: {self.descripcion_producto}\n" \
                   f"Precio unitario: {self.precio_producto}€\n" \
                   f"Nombre cliente: {self.nombre_cliente}\n" \
                   f"Apellidos cliente: {self.apellidos_cliente}\n" \
                   f"Dirección cliente: {self.direccion_cliente}\n" \
                   f"DNI cliente: {self.dni_cliente}\n" \
                   f"Número de unidades: {self.unidades}\n" \
                   f"Importe total: {self.calcular_importe_total()}\n"
        return informe

# Ejemplo de uso
factura = Factura("001", "Camiseta", 20, "Juan", "Perez", "Calle 123", "12345678A", 2)
print(factura.generar_informe())