from matrizOrtogonal import matrizOrtogonal

class nodoMatriz():
    def __init__(self, posicion, nombre):
        self.posicion = posicion
        self.nombre = nombre
        self.siguiente = None
        self.matrizOrtogonal = matrizOrtogonal()
    
class listaMatrizOrtogonal():
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def verVacioListaMatrizOrtogonal(self):
        return self.inicio == None
    
    def insertarFinal(self, posicion, nombre):
        nuevoNodo = nodoMatriz(posicion, nombre)
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
                print('Posición: ', temporal.posicion, ' nombre: ', temporal.nombre)
                temporal = temporal.siguiente

    def buscarNombreMatriz(self, nombre):
        if self.verVacioListaMatrizOrtogonal() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.nombre == nombre:
                    return temporal
                else:
                    temporal = temporal.siguiente
            return None
    
    def buscarPosicionMatriz(self, posicion):
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
listaMatrix1.insertarFinal(0, 'mo0')
listaMatrix1.insertarFinal(1, 'mo1')
listaMatrix1.insertarFinal(2, 'mo2')
listaMatrix1.insertarFinal(3, 'mo3')
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