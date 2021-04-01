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
                self.insertar(cadena[indice], col, fil)
                indice = indice + 1
    
    def mostrarMatriz(self, columnas, filas):
        salida = ''
        for i in range(filas):
            temporal = self.filas.buscarCabeceraHorizontal(i).filaDatos
            temporal2 = temporal.inicio
            for j in range(columnas):
                salida = salida + str(temporal2.dato) + ' | '
                temporal2 = temporal2.derecha
            print(salida)
            salida = ''

    
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
        render('dot', 'png', nombreGrafo)                 #Renderizar el archivo DOT escrito

'''
matriz1 = matrizOrtogonal()
matriz1.llenado(5, 8, '------***--*-*--***-------*-*---*---*-*-')
matriz1.mostrarMatriz(5, 8)
#print(matriz1.filas.buscarCabeceraHorizontal(1).filaDatos.inicio.derecha.derecha.arriba.dato)
matriz1.crearGrafo('matriz de prueba', 5, 8)
print('')
print('')
matriz2 = matrizOrtogonal()
matriz2.llenado(12, 12, '-----------------**---------*--*-------*----*-----*--**--*---*--****--*--------------*-******-*--*--------*--*--------*--**********-------------')
matriz2.mostrarMatriz(12, 12)
matriz2.crearGrafo('matriz de prueba 2', 12, 12)
'''
