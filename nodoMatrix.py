from matrizOrtogonal import matrizOrtogonal

class nodoMatriz():
    def __init__(self, posicion, nombre, columnas, filas):          #Datos de la matriz ortogonal
        self.posicion = posicion
        self.nombre = nombre
        self.columnas = columnas
        self.filas = filas
        self.siguiente = None
        self.matrizOrtogonal = matrizOrtogonal()
    
class listaMatrizOrtogonal():                                       #Lista simple enlazada
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def verVacioListaMatrizOrtogonal(self):
        return self.inicio == None
    
    def insertarFinal(self, posicion, nombre, columnas, filas):     #Agregar nodo al final
        nuevoNodo = nodoMatriz(posicion, nombre, columnas, filas)
        if self.verVacioListaMatrizOrtogonal():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        else:
            temporal = self.inicio
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevoNodo
    
    def mostrarListaMatrizOrtogonal(self):
        if self.verVacioListaMatrizOrtogonal() == False:
            temporal = self.inicio
            while temporal is not None:
                print('Posición: ', temporal.posicion, ' nombre: ', temporal.nombre, ' columnas: ', temporal.columnas,' filas:', temporal.filas)
                temporal = temporal.siguiente

    def buscarNombreMatriz(self, nombre):                           #Busqueda de nodo por nombre
        if self.verVacioListaMatrizOrtogonal() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.nombre == nombre:
                    return temporal
                else:
                    temporal = temporal.siguiente
            return None
    
    def buscarPosicionMatriz(self, posicion):                       #Bsqueda de nodo por posición
        if self.verVacioListaMatrizOrtogonal() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.posicion == posicion:
                    return temporal
                else:
                    temporal = temporal.siguiente
            return None

'''
listaMatrix1 = listaMatrizOrtogonal()
listaMatrix1.insertarFinal(0, 'mo0', 10, 10)
listaMatrix1.insertarFinal(1, 'mo1', 8, 5)
listaMatrix1.insertarFinal(2, 'mo2', 11,20)
listaMatrix1.insertarFinal(3, 'mo3', 3, 3)
listaMatrix1.mostrarListaMatrizOrtogonal()

if listaMatrix1.buscarNombreMatriz('mo2') is not None:
    tmp = listaMatrix1.buscarNombreMatriz('mo2')
    print('Si existe, esta en la posición', tmp.posicion)
else:
    print('No existe')

if listaMatrix1.buscarPosicionMatriz(2) is not None:
    tmp = listaMatrix1.buscarPosicionMatriz(2)
    print('Si existe, esta en la posición', tmp.posicion, ' y su nombre es ', tmp.nombre)
else:
    print('No existe')

listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.llenado(4, 4, 'Esto es una prue')
listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.mostrarMatriz(4, 4)
print('-----------------------------------------------------------------------')
listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.llenado(4, 4, 'matriz ortogonal')
listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.mostrarMatriz(4, 4)
'''
