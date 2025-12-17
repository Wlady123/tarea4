"""
CASO 2: TIENDA VIRTUAL (MUNDO REAL)

Este programa simula una tienda virtual básica
utilizando Programación Orientada a Objetos (POO).
"""
# Clase Producto: representa un producto de la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        # Muestra la información del producto
        return f"Producto: {self.nombre} - Precio: ${self.precio}"

# Clase Cliente: representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_producto(self, producto):
        # Agrega un producto al carrito del cliente
        self.carrito.append(producto)

        

