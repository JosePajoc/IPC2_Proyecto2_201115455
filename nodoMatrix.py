from matrizOrtogonal import matrizOrtogonal                         #Módulo para hacer uso de las matrices ortogonales
from io import open                                                 #Módulo para abrir el archivo

class nodoMatriz():
    def __init__(self, posicion, nombre, columnas, filas, fechaCreacion):          #Datos de la matriz ortogonal
        self.posicion = posicion
        self.nombre = nombre
        self.columnas = columnas
        self.filas = filas
        self.fechaCreacion = fechaCreacion
        self.siguiente = None
        self.matrizOrtogonal = matrizOrtogonal()
    
class listaMatrizOrtogonal():                                       #Lista simple enlazada
    def __init__(self):
        self.inicio = None
        self.fin = None
    
    def verVacioListaMatrizOrtogonal(self):
        return self.inicio == None
    
    def insertarFinal(self, posicion, nombre, columnas, filas, fechaCreacion):     #Agregar nodo al final
        nuevoNodo = nodoMatriz(posicion, nombre, columnas, filas, fechaCreacion)
        if self.verVacioListaMatrizOrtogonal():
            self.inicio = nuevoNodo
            self.fin = nuevoNodo
        else:
            temporal = self.inicio
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevoNodo
    
    def mostrarListaMatrizOrtogonal(self):                          #Temporal para ver datos en consola de la lista enlazada
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

    def crearReporte(self):
        archivoCSS = open("grafos/estilo.css", "w")
        contenidoCSS = """html {   font-size: 20px; font-family: 'Open Sans', sans-serif; } \n
                    h1 { font-size: 60px; text-align: center; } \n
                    h2 { font-size: 40px; text-align: center; } \n
                    p, li {   font-size: 16px;   line-height: 2;   letter-spacing: 1px; }\n
                    html { background-color: #00539F; }
                    body { width: 1100px; margin: 0 auto; background-color: #FF9500; padding: 0 20px 20px 20px; border: 5px solid black; }
                    h1 { margin: 0; padding: 20px 0; color: #00539F; text-shadow: 3px 3px 1px black; }"""
        archivoCSS.write(contenidoCSS)
        archivoCSS.close()

        archivoHTML = open("grafos/index.html", "w")
        archivoHTML.write("<!Doctype html>\n")
        archivoHTML.write("<head>\n")
        archivoHTML.write("<title>Proyecto 2 - IPC2</title>\n")
        archivoHTML.write('<link href="estilo.css" rel="stylesheet" type="text/css">\n')
        archivoHTML.write("</head>\n")
        archivoHTML.write("<body>\n")
        archivoHTML.write("<h1>Matrices cargadas</h1>\n")
        archivoHTML.write("<br>\n")
        if self.buscarPosicionMatriz(0) is not None:                                #Mostrar matriz 1 cargada
            columnas = self.buscarPosicionMatriz(0).columnas
            filas = self.buscarPosicionMatriz(0).filas
            totalVacias = 0
            totalLlenas = 0
            for col in range(columnas):
                for fil in range(filas):
                    if self.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '-':
                        totalVacias = totalVacias + 1
                    else:
                        totalLlenas = totalLlenas + 1
            archivoHTML.write(self.buscarPosicionMatriz(0).fechaCreacion + ', nombre de la matriz: ' + self.buscarPosicionMatriz(0).nombre + ', espacios llenos: ' + str(totalLlenas) + ', espacios vacíos: ' + str(totalVacias))
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarPosicionMatriz(0).nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        
        
        if self.buscarPosicionMatriz(1) is not None:                                #Mostrar matriz 2 cargada
            columnas = self.buscarPosicionMatriz(1).columnas
            filas = self.buscarPosicionMatriz(1).filas
            totalVacias = 0
            totalLlenas = 0
            for col in range(columnas):
                for fil in range(filas):
                    if self.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil) == '-':
                        totalVacias = totalVacias + 1
                    else:
                        totalLlenas = totalLlenas + 1
            archivoHTML.write(self.buscarPosicionMatriz(1).fechaCreacion + ', nombre de la matriz: ' + self.buscarPosicionMatriz(1).nombre + ', espacios llenos: ' + str(totalLlenas) + ', espacios vacíos: ' + str(totalVacias))
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarPosicionMatriz(1).nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        
        archivoHTML.write('<h2>Operaciones sobre una matriz</h2>\n')
        #Mostrar matriz rotación horizontal
        if self.buscarNombreMatriz('Matriz_Rotacion_Horizontal') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_Rotacion_Horizontal').fechaCreacion + ', nombre de la matriz: ' + self.buscarNombreMatriz('Matriz_Rotacion_Horizontal').nombre + ', Tipo de operación: rotación horizontal')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_Rotacion_Horizontal').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar matriz rotación vertical
        if self.buscarNombreMatriz('Matriz_Rotacion_Vertical') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_Rotacion_Vertical').fechaCreacion + ', nombre de la matriz: ' + self.buscarNombreMatriz('Matriz_Rotacion_Vertical').nombre + ', Tipo de operación: rotación vertical')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_Rotacion_Vertical').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar matriz transpuesta
        if self.buscarNombreMatriz('Matriz_Transpuesta') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_Transpuesta').fechaCreacion + ', nombre de la matriz: ' + self.buscarNombreMatriz('Matriz_Transpuesta').nombre + ', Tipo de operación: transpuesta')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_Transpuesta').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar matriz limpia
        if self.buscarNombreMatriz('Matriz_imagen_limpia') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_imagen_limpia').fechaCreacion + ', nombre de la matriz: ' + self.buscarNombreMatriz('Matriz_imagen_limpia').nombre + ', Tipo de operación: limpiar zona')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_imagen_limpia').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar agregar línea horizontal
        if self.buscarNombreMatriz('Matriz_linea_horizontal') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_linea_horizontal').fechaCreacion + ', nombre de la matriz: ' + self.buscarNombreMatriz('Matriz_linea_horizontal').nombre + ', Tipo de operación: agregar línea horizontal')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_linea_horizontal').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar agregar línea vertical
        if self.buscarNombreMatriz('Matriz_linea_vertical') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_linea_vertical').fechaCreacion + ', nombre de la matriz: Matriz_linea_vertical Tipo de operación: agregar línea vertical')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_linea_vertical').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar agregar rectángulo
        if self.buscarNombreMatriz('Matriz_con_rectangulo') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_con_rectangulo').fechaCreacion + ', nombre de la matriz: Matriz_con_rectangulo Tipo de operación: agregar rectángulo')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_con_rectangulo').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar agregar triángulo rectángulo
        if self.buscarNombreMatriz('Matriz_con_triangulo_rectangulo') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').fechaCreacion + ', nombre de la matriz: Matriz_con_triangulo_rectangulo Tipo de operación: agregar triángulo rectángulo')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        
        archivoHTML.write('<h2>Operaciones sobre dos matrices</h2>\n')
        #Mostrar unión
        if self.buscarNombreMatriz('Matriz_union') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_union').fechaCreacion + ', nombre de la matriz: Matriz_union Tipo de operación: unión de matrices')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz 1 original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('Matriz 2 original utilizada: ' + self.buscarPosicionMatriz(1).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_union').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar intersección
        if self.buscarNombreMatriz('Matriz_interseccion') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_interseccion').fechaCreacion + ', nombre de la matriz: Matriz_interseccion Tipo de operación: intersección de matrices')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz 1 original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('Matriz 2 original utilizada: ' + self.buscarPosicionMatriz(1).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_interseccion').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar diferencia simétrica
        if self.buscarNombreMatriz('Matriz_diferencia') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_diferencia').fechaCreacion + ', nombre de la matriz: Matriz_diferencia Tipo de operación: diferencia de matrices')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz 1 original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('Matriz 2 original utilizada: ' + self.buscarPosicionMatriz(1).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_diferencia').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        #Mostrar diferencia simétrica
        if self.buscarNombreMatriz('Matriz_diferencia_simetrica') is not None:
            archivoHTML.write(self.buscarNombreMatriz('Matriz_diferencia_simetrica').fechaCreacion + ', nombre de la matriz: Matriz_diferencia_simetrica Tipo de operación: diferencia simétrica de matrices')
            archivoHTML.write('<br>\n')
            archivoHTML.write('Matriz 1 original utilizada: ' + self.buscarPosicionMatriz(0).nombre)
            archivoHTML.write('Matriz 2 original utilizada: ' + self.buscarPosicionMatriz(1).nombre)
            archivoHTML.write('\n<br>\n')
            archivoHTML.write('<img src="' + self.buscarNombreMatriz('Matriz_diferencia_simetrica').nombre + '.dot.png" ' + 'width=250 height=250  border="1">\n')
            archivoHTML.write('<br>\n')
        
        archivoHTML.write("</body>\n")
        archivoHTML.write("</html>")
        archivoHTML.close()


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
