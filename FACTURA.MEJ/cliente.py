class Cliente:
    def __init__(self, nombre, apellido, telefono, gmail, barrio, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.gmail = gmail
        self.barrio = barrio
        self.direccion = direccion

# Crear una lista de 10 clientes ficticios
clientes_ficticios = [
    
        Cliente("María", "López", "3512345678", "marialopez@gmail.com", "Nueva Córdoba", "Av. Libertad 456"),
        Cliente("Juan", "Vives", "3513053541", "juanvives@gmail.com", "Centro", "Calle 123"),
        Cliente("Pedro", "González", "3518765432", "pedrogonzalez@gmail.com", "Alberdi", "Av. San Martín 789"),
        Cliente("Ana", "Martínez", "3519876543", "anamartinez@gmail.com", "General Paz", "Calle 456"),
        Cliente("Luis", "Sánchez", "3511112222", "luissanchez@gmail.com", "Güemes", "Av. Colón 1234"),
        Cliente("Laura", "Díaz", "3512223333", "lauradiaz@gmail.com", "Observatorio", "Av. Vélez Sársfield 567"),
        Cliente("Carlos", "Romero", "3513334444", "carlosromero@gmail.com", "Alta Córdoba", "Calle 789"),
        Cliente("Mariano", "Pérez", "3514445555", "marianoperez@gmail.com", "Cerro de las Rosas", "Av. Rafael Núñez 1010"),
        Cliente("Lucía", "Hernández", "3515556666", "luciahernandez@gmail.com", "Villa Belgrano", "Calle 101"),
        Cliente("Julián", "Fernández", "3516667777", "julianfernandez@gmail.com", "Argüello", "Av. Gauss 123")
]


def mostrar_clientes():
    cliente_a_mostar=("Nombre Cliente: ")
    if cliente_a_mostar in clientes_ficticios:
        print
def mostrar_todos_clientes():
    for i, cliente in enumerate(clientes_ficticios):
        print(f"Cliente {i}:")
        print("Nombre:", cliente.nombre)
        print("Apellido:", cliente.apellido)
        print("Teléfono:", cliente.telefono)
        print("Correo electrónico:", cliente.gmail)
        print("Barrio:", cliente.barrio)
        print("Dirección:", cliente.direccion)
        print()