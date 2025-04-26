#Clases Hechas por Diego

class Cliente:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")

class GestorClientes:
    def __init__(self):
        self.lista_clientes = []

    def agregar_cliente(self, cliente):
        self.lista_clientes.append(cliente)

    def modificar_cliente(self, email, nuevo_nombre=None, nuevo_apellido=None, nuevo_telefono=None):
        for cliente in self.lista_clientes:
            if cliente.email == email:
                if nuevo_nombre:
                    cliente.nombre = nuevo_nombre
                if nuevo_apellido:
                    cliente.apellido = nuevo_apellido
                if nuevo_telefono:
                    cliente.telefono = nuevo_telefono
                print("Cliente modificado correctamente.")
                return
        print("Cliente no encontrado.")

    def eliminar_cliente(self, email):
        for cliente in self.lista_clientes:
            if cliente.email == email:
                self.lista_clientes.remove(cliente)
                print("Cliente eliminado correctamente.")
                return
        print("Cliente no encontrado.")

    def mostrar_todos(self):
        for cliente in self.lista_clientes:
            cliente.mostrar_info()
            print("-" * 20)
