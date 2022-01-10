# La empresa que te ha contratado desea que, mediante POO en python, 
# crees la clase producto que permita automatizar la organizacion.

# la clase producto cuenta con los sgtes atributos y metodos:
# ATRIBUTOS:

# Codigo: corresponde al codigo del producto que comienza en 100 
# y llega hasta 15000

# Descripcion: corresponde al nombre del producto

# Categoria: Segun tabla se asigna con un metodo que contenga if

# Stock: Corresponde a la cantidad de unidades disponibles del producto

# Bodega: corresponde al numero de bodega donde se encuentran almacenados
# los productos.

# Metodos:

# Categoria: metodo que le asiga la categoria a la que corresponde cada
# uno de los productos, esta categoria se obtiene mediante la sgte 
# tabla.

# ATRIBUTOS O CAMPOS:

# Código Categoría
# Del 100 al 1500 Lácteos
# Del 1501 al 3000 Cereales
# Del 3001 al 6000 Masas
# Del 6001 al 9000 Legumbres
# Del 9001 al 12000 Vegetales
# Del 12001 al 15000 Congelados

# utilizando la setencia logica if debera imprimir el nombre de la 
# categoria del producto.

# Obtener precio:
# Obtener el precio del producto, el cual se obtiene multiplicando por 2 el valor del codigo del producto, tantas veces (for) como el largo del codigo del producto.
# utilizando la sentencia repetitiva for debera imprimir el precio del producto.
# ej codigo: 12000, entonces precio=2*12000*5, donde 5 es el largo de 12000
# (2*12000*1 + 2*12000*2 + 2*12000*3 + 2*12000*4 + 2*12000*5)

# ASIGNAR BODEGA:
# Obtener el numero de bodega asignado a cada uno de los productos, 
# el cual se obtiene contando la cantidad de veces que el numero del 
# codigo es divisible por 3 y 5 al mismo tiempo. este proceso debe 
# realizarse en un ciclo repetitivo disminuyendo en cada iteracion en 
# una cantidad mientras sea mayor que cero. se pide imprimir al termino
# del ciclo el numero de bodega asignado al producto.


class Product:
    
    def __init__(self, code, description, stock):
        self.code = code
        self.description = description
        self.category = self.category(code)
        self.stock = stock
        self.store = self.to_assing_store(code)
        
    def category(self, code):       
        if code >= 100 and code <= 1500:
            return 'dairy'
        elif code >= 1501 and code <= 3000:
            return 'cereals'
        elif code >= 3001 and code <= 6000:
            return 'masses'
        elif code >= 6001 and code <= 9000:
            return 'legumes'
        elif code >= 9001 and code <= 12000:
            return 'vegetables'
        elif code >= 12001 and code <= 15000:
            return 'frozen'
        
    def get_price(self, code):
        self.__price = 0
        
        for i in range(1, len(str(code))):
            self.__price += (2*int(code)*i)
            
        return self.__price 
    
    def to_assing_store(self, code):
        self.__store_number = 0
        self.__count = code
        
        while self.__count > 0:
            if self.__count % 3 == 0 and self.__count % 5 == 0:
                self.__store_number += 1 
            self.__count -= 1
        
        return self.__store_number
    
    
if __name__ == '__main__':
    milk = Product(100, 'leche', '50')
    
    print(milk.category)
    print(milk.get_price(100))
    print(milk.store)