class Inventario :
    def __init__(self):
        self.producto=["coca","sprite","fanta"]
        self.precio=[2200,1900,1850]
        self.x=0
        self.cantidad=[503,374,345]
        self.producto_precio={
            "coca":2200,
            "sprite":1900,
            "fanta":1850 
                              }
    
    def agregar_producto(self):
        producto_agregado=input(f"PRODUCTO: ")
        precio_agregado=int(input(f"PRECIO: {producto_agregado}"))
        self.producto.append(producto_agregado)
        self.precio.append(precio_agregado)
        self.producto_precio[producto_agregado]=precio_agregado
        print(self.pr)
        print(f"AGREGADO:  {producto_agregado}-{precio_agregado}$")
        
        eleccion=int(input("""
                           1-Ir MENU 
                           2-Agregar otro producto
                           3-Sacar producto
                           """))
        if eleccion==1:
            inventario.menu()
        elif eleccion==2:
            inventario.agregar_producto()
        elif eleccion==3:
            inventario.sacar_producto()
        
        
    def sacar_producto(self):
        producto_sacar=input("PRODUCTO: ")
        if producto_sacar in self.producto:
            x=self.producto.index(producto_sacar)
            self.precio.pop(x)
            self.producto.remove(producto_sacar)
            print(f"""PRODUCTO: {producto_sacar} 
                       A SIDO DESALMACENADO
                       
                       1-Ir MENU
                       
                       2-Sacar otro Producto
                       
                       3-Agragar Producto
                       
                       """)
            elecicion=int(input("_"))
            if elecicion==1:
                inventario.menu()
            elif elecicion==2:
                inventario.sacar_producto()
            elif elecicion==3:
                inventario.agregar_producto()
            inventario.menu()
        else:
            print("el producto no se pudo remover por que no existe")
            inventario.menu()
    
    
    def mostrar_inventario(self):
        print("INVENTARIO")
        for producto,precio in self.producto_precio.items():
            print (f"PRODUCTO {producto}-{precio}$")
            
                
        
          
        inventario.menu()
   
    
    def cobrar (self):
        canasta_producto=[]
        canasta_precio=[]
        canasta_cantidad=[]
        contador=0
        
        while True:
            producto_cobrar=input("BUSCAR: ")
            try:
                self.x=self.producto.index(producto_cobrar)
            except:
                print("el producto no esta desea 1 intentar otra vez 2 ir menu")
                eleccion=int(input("ingrese eleccion:"))
                if eleccion==1:
                    inventario.cobrar()
            
                elif eleccion==2:
                    inventario.menu()
                    
            if producto_cobrar == self.producto[self.x]:
                print (self.producto[self.x])
                print (f"producto {self.producto[self.x]}-{self.precio[self.x]}$")
                cantidad_producto=int(input("Cantidad: "))
                    
                canasta_producto.append(self.producto[self.x])
                canasta_precio.append(self.precio[self.x])
                canasta_cantidad.append(cantidad_producto)
                
                total=self.precio[self.x] * cantidad_producto
                contador=contador+total
                
                
                    
                print("1-no desea mas nada 2-seguir 3-cuanto dinero va")
                eleccion=int(input("_"))
            
                if eleccion==1:
                        
                    print(f"""                   -----------------------------------------------
                                       DIA:  DD/MM/AA
                                       HORA:  3:56 HS
                                       PRODUCTOS {canasta_producto[:]}
                                       PRECIOS {canasta_precio[:]}
                                       CANTIDADES {canasta_cantidad[:]}
                                       
                                    -----------------------------------------------
                                       
                                       """)
                    print("para salir toque 1")
                    if eleccion==1:
                        inventario.menu()
                    else:
                        inventario.menu()
                        
                elif eleccion==3:
                        print(contador)
                    
                    
            else:
                    print("el producto no esta")
                    inventario.cobrar()
                    
    
            

    def menu (self):
        print ("""
--------------------------------------------------------------------------------------------------------------------------------------------    
    -      1- Cobrar
    -     
    -      2- Agregar producto
    -      
    -      3- Sacar producto
    -      
    -      4- Mostrar inventario
--------------------------------------------------------------------------------------------------------------------------------------------           
           """)   
        eleccion=int(input("_"))
        if eleccion==4:
            inventario.mostrar_inventario()
        elif eleccion==3:
            inventario.sacar_producto()
        elif eleccion==2:
            inventario.agregar_producto()
        elif eleccion==1:
            inventario.cobrar()
            
                
            




inventario=Inventario()
inventario.menu()