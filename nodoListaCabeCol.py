from listaVertical import listaVertical

class nodoCabeceraColumna():                                #Nodo para identificar las columnas de la matriz
    def __init__(self, columna):
        self.columna = columna                              #único dato se da la posición a utilizar en las columnas cabeceras
        self.izquierda = None
        self.derecha = None
        self.columnaDatos = listaVertical()                 #Como atributo poseera una lista doble enlazada

class listaCabeceraVertical():                              #Creando lista para las cabeceras de las columnas
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def verVacioListaCabeceraVertical(self):
        return self.inicio == None
    
    def insertar(self, columna):
        nuevoNodo = nodoCabeceraColumna(columna)
        if self.verVacioListaCabeceraVertical():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        elif nuevoNodo.columna < self.inicio.columna:
            self.insertarInicio(nuevoNodo)
        elif nuevoNodo.columna > self.fin.columna:
            self.insertarFinal(nuevoNodo)
        else:
            self.insertarMedio(nuevoNodo)
    
    def insertarInicio(self, nuevoNodo):
        self.inicio.izquierda = nuevoNodo
        nuevoNodo.derecha = self.inicio
        self.inicio = nuevoNodo
    
    def insertarFinal(self, nuevoNodo):
        self.fin.derecha = nuevoNodo
        nuevoNodo.izquierda = self.fin
        self.fin = nuevoNodo
    
    def insertarMedio(self, nuevoNodo):
        temporal1 = self.inicio
        while temporal1.columna < nuevoNodo.columna:
            temporal1 = temporal1.derecha
        temporal2 = temporal1.izquierda
        temporal2.derecha = nuevoNodo
        nuevoNodo.izquierda = temporal2
        temporal1.izquierda = nuevoNodo
        nuevoNodo.derecha = temporal1
    
    def mostrarListaCabeceraVertical(self):
        if self.verVacioListaCabeceraVertical() == False:
            temporal = self.inicio
            while temporal is not None:
                print('Columna: ', temporal.columna)
                temporal = temporal.derecha
    
    def buscarCabeceraVertical(self, columna):               #Buscando una columna entre las cabeceras
        if self.verVacioListaCabeceraVertical() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.columna == columna:
                    return temporal
                else:
                    temporal = temporal.derecha
        return None


'''
lista1 = listaCabeceraVertical()

lista1.insertar(3)
lista1.insertar(1)
lista1.insertar(5)
lista1.insertar(4)
lista1.insertar(2)
lista1.mostrarListaCabeceraVertical()

if lista1.buscarCabeceraVertical(4) == None:
    print('No existe')
else:
    tmp = lista1.buscarCabeceraVertical(4)
    print('Si existe la columna ', tmp.columna)
'''
