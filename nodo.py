class nodo():
    def __init__(self, dato, columna, fila):            #Nodo ortogonal que poseera el dato, sus índices y apuntadores
        self.dato = dato
        self.columna = columna
        self.fila = fila
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None