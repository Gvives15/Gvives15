class Producto:
    def __init__(self, nombre, marca, tipo, precio, vencimiento, stock, agregado):
        self.nombre = nombre
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.vencimiento = vencimiento
        self.stock = stock
        self.agregado = agregado


def chicle_todos ():
    chicle = Producto("Chicle de menta", "Beldent", "Dulce", 200, "01/01/2023", 300, False)
    chicle_frutilla = Producto("Chicle de menta", "Beldent", "Dulce", 200, "01/01/2023", 300 ,"Frutilla")
    chicle_sandia = Producto("Chicle de menta", "Beldent", "Dulce", 200, "01/01/2023", 300,"Sandia")
    
def mantecol_todos ():
    manteco_grande = Producto("Mantecol", "Arcor", "Dulce", 160, "01/01/2023", 150, True, False)
    manteco_relleno = Producto("Mantecol", "Arcor", "Dulce", 160, "01/01/2023", 111, True,"Dulce De Leche")
    manteco_de_nueces = Producto("Mantecol", "Arcor", "Dulce", 160, "01/01/2023", 13, True,"Nueces")
    
def alfajor_todos ():
    alfajor_relleno = Producto("Alfajor de chocolate", "Havanna", "Dulce", 250, "01/01/2025", 100,"Duelce De Leche")
    alfajor_chocolate = Producto("Alfajor de chocolate", "Havanna", "Dulce", 250, "01/01/2025", 100,"Chocolate")
    alfajor_bon_o_bom = Producto("Alfajor de chocolate", "Havanna", "Dulce", 250, "01/01/2025", 100,"Bon O Bom")

def caarmelo_todos ():
    caramelo_frutilla = Producto("Caramelo de menta", "Arcor", "Dulce", 50, "01/01/2023", 200,"Frutilla")
    caramelo_banana = Producto("Caramelo de menta", "Arcor", "Dulce", 50, "01/01/2023", 230,"Banana")
    caramelo_manzana = Producto("Caramelo de menta", "Arcor", "Dulce", 50, "01/01/2023", 212,"Manzana")
     
def turron_todos():
      turrón = Producto("Turrón de Jijona", "1880", "Dulce", 300, "01/01/2024", 50 , False)
      turrón_de_nueces = Producto("Turrón de Jijona", "1880", "Dulce", 320, "01/01/2024", 23 ,"Nueces")
      turron_de_azucar= Producto("Turrón de Jijona", "1880", "Dulce", 320, "01/01/2024", 21 ,"azucar")

def agregar_producto_todos():
    pass
      

      