"""
Sistema de Reservas de Hotel
Descripción del caso del mundo real:
Este programa simula un sistema básico de reservas de un hotel
usando Programación Orientada a Objetos (POO).
"""
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.habitacion.disponible = False

    def calcular_total(self):
        return self.dias * self.habitacion.precio
cliente1 = Cliente("Daniel Cañar", "0102030405")
habitacion1 = Habitacion(101, "Matrimonial", 50)

reserva1 = Reserva(cliente1, habitacion1, 3)
print(reserva1.calcular_total())
