from nodo import nodo
from nodoListaCabeCol import nodoCabeceraColumna
from nodoListaCabeCol import listaCabeceraVertical
from nodoListaCabeFila import nodoCabeceraFila
from nodoListaCabeFila import listaCabeceraHorizontal
from io import open                          #Importando módulo para crear archivo plano
from graphviz import render                  #Importando módulo para renderizar desde python, agregar con pip graphviz

class matrizOrtogonal():
    def __init__(self):
        self.columnas = listaCabeceraVertical()
        self.filas = listaCabeceraHorizontal()
    
    def insertar(self, dato, columna, fila):
        nodoNuevo = nodo(dato, columna, fila)
        if self.columnas.buscarCabeceraVertical(columna) == None:       #Se crean los índices si estos no existen
            self.columnas.insertar(columna)
        if self.filas.buscarCabeceraHorizontal(fila) == None:
            self.filas.insertar(fila)
        temporalColumna = self.columnas.buscarCabeceraVertical(columna) #Buscando y obteniendo los índices de la matriz
        temporalFila = self.filas.buscarCabeceraHorizontal(fila)
        temporalColumna.columnaDatos.insertar(nodoNuevo)
        temporalFila.filaDatos.insertar(nodoNuevo)
        #print('Dato: ', nodoNuevo.dato, ' Columna: ', nodoNuevo.columna, ' Fila: ', nodoNuevo.fila)
    
    def llenado(self, columnas, filas, cadena):
        indice = 0
        for fil in range(filas):
            for col in range(columnas):
                self.insertar(cadena[indice], col, fil)                 #dato, columna, fila
                indice = indice + 1
    
    def mostrarMatriz(self, columnas, filas):                           #Mostrar en consola
        salida = ''
        for i in range(filas):
            temporal = self.filas.buscarCabeceraHorizontal(i).filaDatos
            temporal2 = temporal.inicio
            for j in range(columnas):
                salida = salida + str(temporal2.dato) + ' | '
                temporal2 = temporal2.derecha
            print(salida)
            salida = ''

    def llenadoRotacionHorizontal(self, columnas, filas, cadena):
        indice = 0
        filas = filas - 1
        while filas > -1:
            for col in range(columnas):
                self.insertar(cadena[indice], col, filas)
                #print('columna: ', col, ' fila: ', filas)              #Visualizar coordenadas en consola
                indice = indice + 1
            filas = filas - 1

    def llenadoRotacionVertical(self, columnas, filas, cadena):
        indice = 0
        columnas = columnas - 1
        for fil in range(filas):
            col = columnas
            while col > -1:
                self.insertar(cadena[indice], col, fil)
                #print('columna: ', col, ' fila: ', fil, ' dato: ', cadena[indice]) #Visualizar en consola
                indice = indice + 1
                col = col - 1

    def transpuesta(self, columnas, filas, cadena):
        indice = 0
        for fil in range(filas):
            for col in range(columnas):
                self.insertar(cadena[indice], fil, col)                 #dato, columna, fila
                indice = indice + 1

    def devolvercadena(self, columnas, filas):             #Retornar los datos de la matriz ortogonal en una sola línea
        salida = ''
        for i in range(filas):
            temporal = self.filas.buscarCabeceraHorizontal(i).filaDatos
            temporal2 = temporal.inicio
            for j in range(columnas):
                salida = salida + str(temporal2.dato)
                temporal2 = temporal2.derecha
        return salida
    
    def crearGrafo(self, nombre, columnas, filas):
        nombreGrafo = 'grafos/' + nombre + '.dot'
        salidaImagen = open(nombreGrafo, 'w')
        salidaImagen.write('digraph G { \n')
        salidaImagen.write('node [shape=plaintext] \n')
        salidaImagen.write('a [label=<<table border="0" cellborder="1" cellspacing="0"> \n')
        
        for i in range(filas):
            temporal = self.filas.buscarCabeceraHorizontal(i).filaDatos
            temporal2 = temporal.inicio
            salidaImagen.write('<tr> \n')

            for j in range(columnas):
                if temporal2.dato == '-':
                    salidaImagen.write('\t <td>  </td> \n')
                else:
                    salidaImagen.write('\t <td>' + temporal2.dato + '</td> \n') 
                temporal2 = temporal2.derecha
            
            salidaImagen.write('</tr> \n')
        
        salidaImagen.write('</table>>]; \n')
        salidaImagen.write('}')
        salidaImagen.close()
        render('dot', 'png', nombreGrafo)                         #Renderizar el archivo DOT escrito

    def buscarNodo(self, columna, fila):                          #Busca un nodo por sus coordenadas y muestra su dato
        temporal = self.filas.buscarCabeceraHorizontal(fila).filaDatos
        temporal2 = temporal.buscarColumna(columna)
        temporalDatoNodo = temporal2.dato
        return temporalDatoNodo
    
    def buscarNodoSustituirDato(self, columna, fila, nuevoDato):  #Busca un nodo por sus coordenadas y actualiza su dato
        temporal = self.filas.buscarCabeceraHorizontal(fila).filaDatos
        temporal2 = temporal.buscarColumna(columna)
        temporal2.dato = nuevoDato
        

'''
matriz1 = matrizOrtogonal()
matriz1.llenado(5, 8, '------***--*-*--***-------*-*---*---*-*-')
matriz1.mostrarMatriz(5, 8)
#print(matriz1.filas.buscarCabeceraHorizontal(1).filaDatos.inicio.derecha.derecha.arriba.dato)
#matriz1.crearGrafo('matriz de prueba', 5, 8)
#print(matriz1.buscarNodo(1,5) , matriz1.buscarNodo(2,5),matriz1.buscarNodo(3,5))
#print(matriz1.buscarNodo(1,6) , matriz1.buscarNodo(2,6),matriz1.buscarNodo(3,6))
matriz1.buscarNodoSustituirDato(1,5, '#')
matriz1.buscarNodoSustituirDato(2,5, '#')
matriz1.buscarNodoSustituirDato(3,5, '#')
print('')
matriz1.mostrarMatriz(5,8)

matriz1_1 = matrizOrtogonal()
matriz1_1.llenadoRotacionVertical(10, 10, '-----------***-***----*--***----*--*-----***-*---------------***-***---*-----*---***-***------------')
matriz1_1.mostrarMatriz(10, 10)
matriz1_1.crearGrafo('matriz de prueba 1_1 rotacion horizontal', 10, 10)
'''
