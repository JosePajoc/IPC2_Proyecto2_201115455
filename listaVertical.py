from nodo import nodo

class listaVertical():
    def __init__(self):
        self.inicio = None
        self.fin = None

    def verVacioVertical(self):
        return self.inicio == None
    
    def insertar(self, nuevoNodo):
        if self.verVacioVertical():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        elif nuevoNodo.fila < self.inicio.fila:
            self.insertarInicio(nuevoNodo)
        elif nuevoNodo.fila > self.fin.fila:
            self.insertarFinal(nuevoNodo)
        else:
            self.insertarMedio(nuevoNodo)

    def insertarInicio(self, nuevoNodo):
        self.inicio.arriba = nuevoNodo
        nuevoNodo.abajo = self.inicio
        inicio = nuevoNodo
        print('si I')
    
    def insertarFinal(self, nuevoNodo):
        self.fin.abajo = nuevoNodo
        nuevoNodo.arriba = self.fin
        fin = nuevoNodo
        print('si F')
    
    def insertarMedio(self, nuevoNodo):
        temporal1 = self.inicio
        while temporal1.fila < nuevoNodo.fila:
            temporal1 = temporal1.abajo
        temporal2 = temporal1.arriba
        temporal2.abajo = nuevoNodo
        nuevoNodo.arriba = temporal2
        temporal1.arriba = nuevoNodo
        nuevoNodo.abajo = temporal1
        print('si M')
    
    def mostrarListaVertical(self):
        if self.verVacioVertical() is not None:
            temporal = self.inicio
            while temporal is not None:
                print("Columna " , temporal.columna , " fila: " , temporal.fila , " dato: " , temporal.dato)
                temporal = temporal.abajo


lista1 = listaVertical()
lista1.insertar(nodo(10, 0, 1))
lista1.insertar(nodo(50, 0, 2))
lista1.insertar(nodo(70, 0, 3))
#lista1.insertar(nodo(30, 0, 4))
#lista1.insertar(nodo(15, 0, 5))

lista1.mostrarListaVertical()
