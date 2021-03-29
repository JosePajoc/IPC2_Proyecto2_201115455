from listaVertical import listaVertical

class nodoCabeceraColumna():                                #Nodo para identificar las columnas de la matriz
    def __init__(self, columna):
        self.columna = columna                              #único dato se da la posición a utilizar en las columnas cabeceras
        self.arriba = None
        self.abajo = None
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
        self.inicio.arriba = nuevoNodo
        nuevoNodo.abajo = self.inicio
        self.inicio = nuevoNodo
    
    def insertarFinal(self, nuevoNodo):
        self.fin.abajo = nuevoNodo
        nuevoNodo.arriba = self.fin
        self.fin = nuevoNodo
    
    def insertarMedio(self, nuevoNodo):
        temporal1 = self.inicio
        while temporal1.columna < nuevoNodo.columna:
            temporal1 = temporal1.abajo
        temporal2 = temporal1.arriba
        temporal2.abajo = nuevoNodo
        nuevoNodo.arriba = temporal2
        temporal1.arriba = nuevoNodo
        nuevoNodo.abajo = temporal1
    
    def mostrarListaCabeceraVertical(self):
        if self.verVacioListaCabeceraVertical() == False:
            temporal = self.inicio
            while temporal is not None:
                print('Columna: ', temporal.columna)
                temporal = temporal.abajo
    
    def buscarCabeceraVertical(self, columna):               #Buscando una columna entre las cabeceras
        if self.verVacioListaCabeceraVertical() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.columna == columna:
                    return temporal
                else:
                    temporal = temporal.abajo
        return None


'''
lista1 = listaCabeceraHorizontal()

lista1.insertar(3)
lista1.insertar(1)
lista1.insertar(5)
lista1.insertar(4)
lista1.insertar(2)
lista1.mostrarListaCabeceraHorizontal()

if lista1.buscarCabeceraHorizontal(4) == None:
    print('No existe')
else:
    tmp = lista1.buscarCabeceraHorizontal(4)
    print('Si existe la columna ', tmp.columna)
'''
