from listaHorizontal import listaHorizontal

class nodoCabeceraFila():                                   #Nodo para identificar las columnas de la matriz
    def __init__(self, fila):
        self.fila = fila                                    #único dato se da la posición a utilizar en las columnas cabeceras
        self.anterior = None
        self.siguiente = None
        self.filaDatos = listaHorizontal()                 #Como atributo poseera una lista doble enlazada

class listaCabeceraHorizontal():                           #Creando lista para las cabeceras de las columnas
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def verVacioListaCabeceraHorizontal(self):
        return self.inicio == None
    
    def insertar(self, fila):
        nuevoNodo = nodoCabeceraFila(fila)
        if self.verVacioListaCabeceraHorizontal():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        elif nuevoNodo.fila < self.inicio.fila:
            self.insertarInicio(nuevoNodo)
        elif nuevoNodo.fila > self.fin.fila:
            self.insertarFinal(nuevoNodo)
        else:
            self.insertarMedio(nuevoNodo)
    
    def insertarInicio(self, nuevoNodo):
        self.inicio.anterior = nuevoNodo
        nuevoNodo.siguiente = self.inicio
        self.inicio = nuevoNodo
    
    def insertarFinal(self, nuevoNodo):
        self.fin.siguiente = nuevoNodo
        nuevoNodo.anterior = self.fin
        self.fin = nuevoNodo
    
    def insertarMedio(self, nuevoNodo):
        temporal1 = self.inicio
        while temporal1.fila < nuevoNodo.fila:
            temporal1 = temporal1.siguiente
        temporal2 = temporal1.anterior
        temporal2.siguiente = nuevoNodo
        nuevoNodo.anterior = temporal2
        temporal1.anterior = nuevoNodo
        nuevoNodo.siguiente = temporal1
    
    def mostrarListaCabeceraHorizontal(self):
        if self.verVacioListaCabeceraHorizontal() == False:
            temporal = self.inicio
            while temporal is not None:
                print('Fila: ', temporal.fila)
                temporal = temporal.siguiente
    
    def buscarCabeceraHorizontal(self, fila):               #Buscando una columna entre las cabeceras
        if self.verVacioListaCabeceraHorizontal() == False:
            temporal = self.inicio
            while temporal is not None:
                if temporal.fila == fila:
                    return temporal
                else:
                    temporal = temporal.siguiente
        return None

'''
lista1 = listaCabeceraVertical()

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
    print('Si existe la fila ', tmp.fila)
'''
