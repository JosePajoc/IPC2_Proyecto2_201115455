from nodo import nodo

class listaHorizontal():
    def __init__(self):                                     #Crear lista con apuntadores a nulo
        self.inicio = None
        self.fin = None

    def verVacioHorizontal(self):                           #Verificar si existen elementos en la lista
        return self.inicio == None
    
    def insertar(self, nuevoNodo):                          #Insertar nodos según la posición de la fila en los métodos
        if self.verVacioHorizontal():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        elif nuevoNodo.columna < self.inicio.columna:
            self.insertarInicio(nuevoNodo)
        elif nuevoNodo.columna > self.fin.columna:
            self.insertarFinal(nuevoNodo)
        else:
            self.insertarMedio(nuevoNodo)

    def insertarInicio(self, nuevoNodo):                    #Insertar nodo al inicio de la lista y cambiar apuntador
        self.inicio.izquierda = nuevoNodo
        nuevoNodo.derecha = self.inicio
        self.inicio = nuevoNodo
    
    def insertarFinal(self, nuevoNodo):                     #Insertar nodo al final de la lista y cambiar apuntador
        self.fin.derecha = nuevoNodo
        nuevoNodo.izquierda = self.fin
        self.fin = nuevoNodo
    
    def insertarMedio(self, nuevoNodo):                     #Insertar nodo en medio de la lista y cambiar apuntadores
        temporal1 = self.inicio
        while temporal1.columna < nuevoNodo.columna:
            temporal1 = temporal1.derecha
        temporal2 = temporal1.izquierda                     #Para obtener el nodo anterior al deseado y así cambiar sus apuntadores
        temporal2.derecha = nuevoNodo
        nuevoNodo.izquierda = temporal2
        temporal1.izquierda = nuevoNodo
        nuevoNodo.derecha = temporal1
    
    def mostrarListaHorizontal(self):
        if self.verVacioHorizontal() == False:
            temporal = self.inicio
            while temporal is not None:
                print("Columna " , temporal.columna , " fila: " , temporal.fila , " dato: " , temporal.dato)
                temporal = temporal.derecha

    def buscarColumna(self, columna):                       #Buscando una columna
        if self.verVacioHorizontal() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.columna == columna:
                    return temporal
                else:
                    temporal = temporal.derecha
        return None

'''
lista1 = listaHorizontal()
lista1.insertar(nodo(10, 1, 0))
lista1.insertar(nodo(50, 3, 0))
lista1.insertar(nodo(70, 2, 0))
lista1.insertar(nodo(30, 5, 0))
lista1.insertar(nodo(15, 4, 0))

lista1.mostrarListaHorizontal()

if lista1.buscarColumna(2) == None:
    print('No existe la columna')
else:
    print('Si existe la columna')
    print(lista1.buscarColumna(2).dato)
'''