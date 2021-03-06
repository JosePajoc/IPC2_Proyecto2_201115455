from nodo import nodo

class listaVertical():
    def __init__(self):                                     #Crear lista con apuntadores a nulo
        self.inicio = None
        self.fin = None

    def verVacioVertical(self):                             #Verificar si existen elementos en la lista
        return self.inicio == None
    
    def insertar(self, nuevoNodo):                          #Insertar nodos según la posición de la fila en los métodos
        if self.verVacioVertical():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        elif nuevoNodo.fila < self.inicio.fila:
            self.insertarInicio(nuevoNodo)
        elif nuevoNodo.fila > self.fin.fila:
            self.insertarFinal(nuevoNodo)
        else:
            self.insertarMedio(nuevoNodo)

    def insertarInicio(self, nuevoNodo):                    #Insertar nodo al inicio de la lista y cambiar apuntador
        self.inicio.arriba = nuevoNodo
        nuevoNodo.abajo = self.inicio
        self.inicio = nuevoNodo
    
    def insertarFinal(self, nuevoNodo):                     #Insertar nodo al final de la lista y cambiar apuntador
        self.fin.abajo = nuevoNodo
        nuevoNodo.arriba = self.fin
        self.fin = nuevoNodo
    
    def insertarMedio(self, nuevoNodo):                     #Insertar nodo en medio de la lista y cambiar apuntadores
        temporal1 = self.inicio
        while temporal1.fila < nuevoNodo.fila:
            temporal1 = temporal1.abajo
        temporal2 = temporal1.arriba                        #Para obtener el nodo anterior al deseado y así cambiar sus apuntadores
        temporal2.abajo = nuevoNodo
        nuevoNodo.arriba = temporal2
        temporal1.arriba = nuevoNodo
        nuevoNodo.abajo = temporal1
    
    def mostrarListaVertical(self):
        if self.verVacioVertical() == False:
            temporal = self.inicio
            while temporal is not None:
                print("Columna " , temporal.columna , " fila: " , temporal.fila , " dato: " , temporal.dato)
                temporal = temporal.abajo

'''
lista1 = listaVertical()
lista1.insertar(nodo(10, 0, 1))
lista1.insertar(nodo(50, 0, 3))
lista1.insertar(nodo(70, 0, 2))
lista1.insertar(nodo(30, 0, 5))
lista1.insertar(nodo(15, 0, 4))

lista1.mostrarListaVertical()
'''