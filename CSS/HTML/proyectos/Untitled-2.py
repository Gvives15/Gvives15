class nombre:
    def __init__(self):
        self.producto=["coca","fanta"]
        self.x=0
    def mostrar(self):
        producto_mostrar=input("ingrese producto para mostrar: ")
        try:
            self.x=self.producto.index(producto_mostrar)
        except:
            print("el producto no esta desea 1 intentar otra vez 2 ir menu")
            eleccion=int(input("ingrese eleccion:"))
            if eleccion==1:
                ger1.mostrar()
            
            elif eleccion==2:
                print("menu")
        print(self.x)
        if producto_mostrar == self.producto[self.x]:
            print (self.producto[self.x])
        


ger1=nombre()
ger1.mostrar()