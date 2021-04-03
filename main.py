from tkinter import filedialog                      #Módulo para abrir ventana de selección
from tkinter import messagebox                      #Módulo para cuadros de mensaje
from tkinter import *                               #Módulo para entorno gráfico
from nodoMatrix import listaMatrizOrtogonal         #Módulo para crear lista enlazada simplde de matrices ortogonales
from tkinter.simpledialog import *                  #Dialogos de entrada, debe ir antes del PIL caso contrario da error
from PIL import Image, ImageTk                      #Instalar módulo, pip install Pillow, para usar imagenes con más opciones

import xml.etree.ElementTree as ET                  #importando libreria para manipular XML


#-------------------------------------------Ventana inicial-----------------------------------------------------------
ventanaInicial = Tk()                                           #Objeto de tipo ventana
ventanaInicial.title('Proyecto 2 - IPC2')
ventanaInicial.resizable(False, False)                          #No permitir cambios al ancho y alto de la ventana

marcoInicial = Frame(ventanaInicial, width="850", height="500")
marcoInicial.pack()                                             #Marco agregado a la ventana


#--------------------------------------------Manejo del XML-----------------------------------------------------------
documentoXML = None                                             #Variable para el archivo XML
matricesRaiz = None                                             #Variable para la etiqueta matrices y así poder iterar
listaMatrix1 = listaMatrizOrtogonal()                           #Creación de lista simple enlazada para las matrices ortogonales
indice = 0                                                      #Indice global para saber cuantas matrices ortogonales existen
marcoOperaciones = None

def cargarXML(ruta):
    global documentoXML
    global matricesRaiz
    global listaMatrix1
    #try:
    documentoXML = ET.parse(ruta)                               #Conviritendo a legible
    matricesRaiz = documentoXML.getroot()                       #Obteniendo la raíz del XML
    messagebox.showinfo("información", "Se cargo con éxtio...\n\nEl archivo se encuentra en:\n" + ruta)
    procesarXML()
    #except:
    #messagebox.showinfo("información", "No se pudo cargar el archivo...")

def procesarXML():
    global documentoXML
    global matricesRaiz
    global indice
    global listaMatrix1
    nombreM1 = ''
    nombreM2 = ''

    for matriz in matricesRaiz:                                 #Todas las etiquetas de cada matriz son asignadas al elemento
        filas = int(matriz[1].text)                             #Valor de la etiqueta filas del XML
        columnas = int(matriz[2].text)                          #Valor de la etiqueta columnas del XML
        
        imagenEntrada =  matriz[3].text                         #obteniendo los caracteres de la imagen
        
        while '\n' in imagenEntrada or '			' in imagenEntrada or '    ' in imagenEntrada:
            imagenEntrada = imagenEntrada.replace('			','')
            imagenEntrada = imagenEntrada.replace('\n','')
            imagenEntrada = imagenEntrada.replace('    ','')


        listaMatrix1.insertarFinal(indice, matriz[0].text, columnas, filas)      #Se crea el nodo con posición y NOMBRE
        if indice == 0:
            nombreM1 = matriz[0].text
        elif indice == 1:
            nombreM2 = matriz[0].text

        #Se busca el nodo creado, se llama al atributo tipo matriz ortogonal, se llena la matriz con la info de la imagen del XML
        listaMatrix1.buscarPosicionMatriz(indice).matrizOrtogonal.llenado(columnas, filas, imagenEntrada)
        #Crear imagenes a partir de la matriz ortogonal
        listaMatrix1.buscarPosicionMatriz(indice).matrizOrtogonal.crearGrafo(matriz[0].text, columnas, filas)
        
        indice = indice + 1                             #Indice de la lista simple enlazada para las matrices ortogonales 
    cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", state=DISABLED)  #Deshabilitar botón principal
    cargarArchivobtn.place(x=50, y=20)
    mostrarImagenes(indice, nombreM1, nombreM2)
    
    if indice == 1:
        operacionesbtn = Button(marcoInicial, text="Operaciones para una matriz", command=mostrarOperaciones1)
        operacionesbtn.place(x=200, y=20)
        operaciones2btn = Button(marcoInicial, text="Operaciones para dos matriz", state=DISABLED)
        operaciones2btn.place(x=400, y=20)
    else:
        operacionesbtn = Button(marcoInicial, text="Operaciones para una matriz", command=mostrarOperaciones1)
        operacionesbtn.place(x=200, y=20)
        operaciones2btn = Button(marcoInicial, text="Operaciones para dos matriz", command=mostrarOperaciones2)
        operaciones2btn.place(x=400, y=20)

#-----------------------------------------Mostrar imagenes en los visores--------------------------------------------    
def mostrarImagenes(indice, nombreM1, nombreM2):
    if indice == 1:
        imagen1 = Image.open('grafos/' + nombreM1 + '.dot.png')
        tamanoImagen1 = imagen1.resize((250, 250))
        renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
        imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
        imagenlbl.image = renderizadoImagen1
        imagenlbl.place(x=40, y=90)
    else:
        imagen1 = Image.open('grafos/' + nombreM1 + '.dot.png')
        tamanoImagen1 = imagen1.resize((250, 250))
        renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
        imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
        imagenlbl.image = renderizadoImagen1
        imagenlbl.place(x=40, y=90)

        imagen2 = Image.open('grafos/' + nombreM2 + '.dot.png')
        tamanoImagen2 = imagen2.resize((250, 250))
        renderizadoImagen2 = ImageTk.PhotoImage(tamanoImagen2)
        imagen2lbl = Label(marcoInicial, image=renderizadoImagen2)
        imagen2lbl.image = renderizadoImagen2
        imagen2lbl.place(x=300, y=90)

#-------------------------------Proceso rotación horizontal de una matriz--------------------------------------------
def rotacionHorizontalMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_Rotacion_Horizontal', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    #print(cadenaMatrizOrtogonal0)
    listaMatrix1.buscarNombreMatriz('Matriz_Rotacion_Horizontal').matrizOrtogonal.llenadoRotacionHorizontal(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    listaMatrix1.buscarNombreMatriz('Matriz_Rotacion_Horizontal').matrizOrtogonal.crearGrafo('Matriz_Rotacion_Horizontal', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_Rotacion_Horizontal.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    rotacionHorizontal = Button(marcoOperaciones, text='Rotación horizontal', state=DISABLED)   #Deshabilitar botón secundario
    rotacionHorizontal.place(x=10, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#-------------------------------Proceso rotación vertical de una matriz---------------------------------------------
def rotacionVerticalMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_Rotacion_Vertical', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_Rotacion_Vertical').matrizOrtogonal.llenadoRotacionVertical(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    listaMatrix1.buscarNombreMatriz('Matriz_Rotacion_Vertical').matrizOrtogonal.crearGrafo('Matriz_Rotacion_Vertical', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_Rotacion_Vertical.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    rotacionVertical = Button(marcoOperaciones, text='Rotación vertical', state=DISABLED)   #Deshabilitar botón secundario
    rotacionVertical.place(x=160, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#-------------------------------Proceso transpuesta de una matriz----------------------------------------------------
def transpuestaMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición, NOMBRE y cambio de COLUMNAS por FILAS
    listaMatrix1.insertarFinal(indice, 'Matriz_Transpuesta', filNuevaOrtogonal, colNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_Transpuesta').matrizOrtogonal.transpuesta(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    #Se cambia COLUMNAS por FILAS
    listaMatrix1.buscarNombreMatriz('Matriz_Transpuesta').matrizOrtogonal.crearGrafo('Matriz_Transpuesta', filNuevaOrtogonal, colNuevaOrtogonal)
    
    noImagen3 = Image.open('grafos/Matriz_Transpuesta.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    transpuesta = Button(marcoOperaciones, text='Transpuesta', state=DISABLED)   #Deshabilitar botón secundario
    transpuesta.place(x=310, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#-------------------------------Proceso limpiar zona de una imagen----------------------------------------------------
def limpiarZonaImagen():
    global listaMatrix1
    global indice
    global marcoOperaciones
    colInicial = askinteger('titulo', 'ingrese la columna inicial') - 1         #Dialogos de entrada
    filInicial = askinteger('titulo', 'ingrese la fila inicial') - 1
    colFinal = askinteger('titulo', 'ingrese la columna final')
    filFinal = askinteger('titulo', 'ingrese la fila final')

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_imagen_limpia', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_imagen_limpia').matrizOrtogonal.llenado(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    for i in range(colInicial, colFinal):
        for j in range(filInicial, filFinal):
            listaMatrix1.buscarNombreMatriz('Matriz_imagen_limpia').matrizOrtogonal.buscarNodoSustituirDato(i, j, '-')
    
    listaMatrix1.buscarNombreMatriz('Matriz_imagen_limpia').matrizOrtogonal.crearGrafo('Matriz_imagen_limpia', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_imagen_limpia.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    limpiarZona = Button(marcoOperaciones, text='Limpiar Zona', state=DISABLED)   #Deshabilitar botón secundario
    limpiarZona.place(x=420, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#-------------------------------------Proceso agregar línea horizontal------------------------------------------------
def agregarLineaHorizontalMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones
    colInicial = askinteger('titulo', 'ingrese la columna inicial') - 1         #Dialogos de entrada
    filInicial = askinteger('titulo', 'ingrese la fila inicial') - 1
    cantidadElementos = askinteger('titulo', 'Ingrese el número de elementos para la línea')
    colFin = colInicial + cantidadElementos

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_linea_horizontal', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_linea_horizontal').matrizOrtogonal.llenado(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    for i in range(colInicial, colFin):
        listaMatrix1.buscarNombreMatriz('Matriz_linea_horizontal').matrizOrtogonal.buscarNodoSustituirDato(i, filInicial, '*')
    
    listaMatrix1.buscarNombreMatriz('Matriz_linea_horizontal').matrizOrtogonal.crearGrafo('Matriz_linea_horizontal', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_linea_horizontal.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    agregarLineaHorizontal = Button(marcoOperaciones, text='Agregar línea horizontal', state=DISABLED)   #Deshabilitar botón secundario
    agregarLineaHorizontal.place(x=10, y=60)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#--------------------------------------Proceso agregar línea vertical-------------------------------------------------
def agregarLineaVerticallMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones
    colInicial = askinteger('titulo', 'ingrese la columna inicial') - 1         #Dialogos de entrada
    filInicial = askinteger('titulo', 'ingrese la fila inicial') - 1
    cantidadElementos = askinteger('titulo', 'Ingrese el número de elementos para la línea')
    filFin = filInicial + cantidadElementos

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_linea_vertical', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_linea_vertical').matrizOrtogonal.llenado(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    for i in range(filInicial, filFin):
        listaMatrix1.buscarNombreMatriz('Matriz_linea_vertical').matrizOrtogonal.buscarNodoSustituirDato(colInicial, i, '*')
    
    listaMatrix1.buscarNombreMatriz('Matriz_linea_vertical').matrizOrtogonal.crearGrafo('Matriz_linea_vertical', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_linea_vertical.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    agregarLineaVertical = Button(marcoOperaciones, text='Agregar línea vertical', state=DISABLED)   #Deshabilitar botón secundario
    agregarLineaVertical.place(x=160, y=60)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#-----------------------------------------Proceso agregar rectángulo--------------------------------------------------
def agregarRectanguloMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones
    colInicial = askinteger('titulo', 'ingrese la columna inicial') - 1         #Dialogos de entrada
    filInicial = askinteger('titulo', 'ingrese la fila inicial') - 1
    cantidadElemeCol = askinteger('titulo', 'Ingrese la cantidad de elementos para las columnas')
    cantidadElemeFil = askinteger('titulo', 'Ingrese la cantidad de elementos para las filas')
    colFin = colInicial + cantidadElemeCol
    filFin = filInicial + cantidadElemeFil

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_con_rectangulo', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_con_rectangulo').matrizOrtogonal.llenado(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    #Línea superior, aumento en columnas
    for i in range(colInicial, colFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(i, filInicial, '*')
    #Línea inferior, aumento en columnas, se resta a la fila 1 por iniciar en cero los índices
    for i in range(colInicial, colFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(i, filFin - 1, '*')
    
    #Línea izquierda, aumento en filas
    for i in range(filInicial, filFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(colInicial, i, '*')
    #Línea derecha, aumento en filas, se resta a la columna 1 por iniciar en cero los índices
    for i in range(filInicial, filFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(colFin - 1, i, '*')
    
    listaMatrix1.buscarNombreMatriz('Matriz_con_rectangulo').matrizOrtogonal.crearGrafo('Matriz_con_rectangulo', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_con_rectangulo.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    agregarRectangulo = Button(marcoOperaciones, text='Agregar ractángulo', state=DISABLED)   #Deshabilitar botón secundario
    agregarRectangulo.place(x=290, y=60)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales

#---------------------------------------Proceso agregar Triángulo rectángulo------------------------------------------
def agregarTrianRecMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones
    colInicial = askinteger('titulo', 'ingrese la columna inicial') - 1         #Dialogos de entrada
    filInicial = askinteger('titulo', 'ingrese la fila inicial') - 1
    cantidadElemeCol = cantidadElemeFil = askinteger('titulo', 'Ingrese la cantidad de elementos')
    #cantidadElemeFil = askinteger('titulo', 'Ingrese la cantidad de elementos para la fila')
    colFin = colInicial + cantidadElemeCol
    filFin = filInicial + cantidadElemeFil

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    #Se crea el nodo con posición y NOMBRE
    listaMatrix1.insertarFinal(indice, 'Matriz_con_triangulo_rectangulo', colNuevaOrtogonal, filNuevaOrtogonal) 
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    
    listaMatrix1.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').matrizOrtogonal.llenado(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    #Fila de la figura
    for i in range(colInicial, colFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(i, filFin - 1, '*')
    
    #Columna de la figura
    for i in range(filInicial, filFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(colInicial, i, '*')
    
    #Línea inclinada de la figura
    col = colInicial
    for fil in range(filInicial, filFin):
        listaMatrix1.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
        col = col + 1
    
    listaMatrix1.buscarNombreMatriz('Matriz_con_triangulo_rectangulo').matrizOrtogonal.crearGrafo('Matriz_con_triangulo_rectangulo', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_con_triangulo_rectangulo.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    agregarTrianguloRectangulo = Button(marcoOperaciones, text='Agregar triángulo rectángulo', state=DISABLED)   #Deshabilitar botón secundario
    agregarTrianguloRectangulo.place(x=410, y=60)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#--------------------------------------Proceso unión de dos matrices---------------------------------------------------
def unionMatrices():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colOrto1 = listaMatrix1.buscarPosicionMatriz(0).columnas
    filOrto1 = listaMatrix1.buscarPosicionMatriz(0).filas
    
    colOrto2 = listaMatrix1.buscarPosicionMatriz(1).columnas
    filOrto2 = listaMatrix1.buscarPosicionMatriz(1).filas
    
    if (colOrto1 * filOrto1) > (colOrto2 * filOrto2):
        #Se crea el nodo con posición y NOMBRE
        listaMatrix1.insertarFinal(indice, 'Matriz_union', colOrto1, filOrto1)
        cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colOrto1, filOrto1)
        listaMatrix1.buscarNombreMatriz('Matriz_union').matrizOrtogonal.llenado(colOrto1, filOrto1, cadenaMatrizOrtogonal0)
        for col in range(colOrto2):
            for fil in range(filOrto2):
                if listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_union').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
        listaMatrix1.buscarNombreMatriz('Matriz_union').matrizOrtogonal.crearGrafo('Matriz_union', colOrto1, filOrto1)
    else:
        listaMatrix1.insertarFinal(indice, 'Matriz_union', colOrto2, filOrto2)
        cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.devolvercadena(colOrto2, filOrto2)
        listaMatrix1.buscarNombreMatriz('Matriz_union').matrizOrtogonal.llenado(colOrto2, filOrto2, cadenaMatrizOrtogonal0)
        for col in range(colOrto1):
            for fil in range(filOrto1):
                if listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_union').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
        listaMatrix1.buscarNombreMatriz('Matriz_union').matrizOrtogonal.crearGrafo('Matriz_union', colOrto2, filOrto2)
    
    noImagen3 = Image.open('grafos/Matriz_union.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    unionbtn = Button(marcoOperaciones, text='Unión', state=DISABLED)   #Deshabilitar botón secundario
    unionbtn.place(x=10, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#-----------------------------------Proceso intersección de dos matrices-----------------------------------------------
def interseccionMatrices():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colOrto1 = listaMatrix1.buscarPosicionMatriz(0).columnas
    filOrto1 = listaMatrix1.buscarPosicionMatriz(0).filas
    
    colOrto2 = listaMatrix1.buscarPosicionMatriz(1).columnas
    filOrto2 = listaMatrix1.buscarPosicionMatriz(1).filas
    
    if (colOrto1 * filOrto1) > (colOrto2 * filOrto2):
    
        listaMatrix1.insertarFinal(indice, 'Matriz_interseccion', colOrto1, filOrto1)
        listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.llenadoVacio(colOrto1, filOrto1)
        for col in range(colOrto2):
            for fil in range(filOrto2):
                if listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')

        for col in range(colOrto1):
            for fil in range(filOrto1):
                if (listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodo(col, fil) == '*') and (listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*'):
                    listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
                else:
                    listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '-')
        listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.crearGrafo('Matriz_interseccion', colOrto1, filOrto1)
    else:
        
        listaMatrix1.insertarFinal(indice, 'Matriz_interseccion', colOrto2, filOrto2)
        listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.llenadoVacio(colOrto2, filOrto2)
        for col in range(colOrto1):
            for fil in range(filOrto1):
                if listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')

        for col in range(colOrto2):
            for fil in range(filOrto2):
                if (listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodo(col, fil) == '*') and (listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil) == '*'):
                    listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
                else:
                    listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '-')
        listaMatrix1.buscarNombreMatriz('Matriz_interseccion').matrizOrtogonal.crearGrafo('Matriz_interseccion', colOrto2, filOrto2)
    
    noImagen3 = Image.open('grafos/Matriz_interseccion.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    interseccionbtn = Button(marcoOperaciones, text='Intersección', state=DISABLED)   #Deshabilitar botón secundario
    interseccionbtn.place(x=140, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#---------------------------------Proceso diferencia simétrica entre de dos matrices-----------------------------------
def diferenciaSimetricaMatrices():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colOrto1 = listaMatrix1.buscarPosicionMatriz(0).columnas
    filOrto1 = listaMatrix1.buscarPosicionMatriz(0).filas
    
    colOrto2 = listaMatrix1.buscarPosicionMatriz(1).columnas
    filOrto2 = listaMatrix1.buscarPosicionMatriz(1).filas
    
    if (colOrto1 * filOrto1) > (colOrto2 * filOrto2):
        #Se crea el nodo con posición y NOMBRE
        listaMatrix1.insertarFinal(indice, 'Matriz_diferencia_simetrica', colOrto1, filOrto1)
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.llenadoVacio(colOrto1, filOrto1)
        for col in range(colOrto1):
            for fil in range(filOrto1):
                if listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')

        for col in range(colOrto2):
            for fil in range(filOrto2):
                if listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodo(col, fil) == listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil):
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '-')
                else:
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.crearGrafo('Matriz_diferencia_simetrica', colOrto1, filOrto1)
    else:
        
        listaMatrix1.insertarFinal(indice, 'Matriz_diferencia_simetrica', colOrto2, filOrto2)
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.llenadoVacio(colOrto2, filOrto2)
        for col in range(colOrto1):
            for fil in range(filOrto1):
                if listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')

        for col in range(colOrto2):
            for fil in range(filOrto2):
                if listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodo(col, fil) == listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil):
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '-')
                else:
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia_simetrica').matrizOrtogonal.crearGrafo('Matriz_diferencia_simetrica', colOrto2, filOrto2)
    
    noImagen3 = Image.open('grafos/Matriz_diferencia_simetrica.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    diferenciaSimetricabtn = Button(marcoOperaciones, text='Diferencia simétrica', state=DISABLED)   #Deshabilitar botón secundario
    diferenciaSimetricabtn.place(x=400, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#------------------------------------Proceso diferencia entre de dos matrices-----------------------------------------
def diferenciaMatrices():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colOrto1 = listaMatrix1.buscarPosicionMatriz(0).columnas
    filOrto1 = listaMatrix1.buscarPosicionMatriz(0).filas
    
    colOrto2 = listaMatrix1.buscarPosicionMatriz(1).columnas
    filOrto2 = listaMatrix1.buscarPosicionMatriz(1).filas
    
    if (colOrto1 * filOrto1) > (colOrto2 * filOrto2):
        #Se crea el nodo con posición y NOMBRE
        listaMatrix1.insertarFinal(indice, 'Matriz_diferencia', colOrto1, filOrto1)
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.llenadoVacio(colOrto1, filOrto1)
        for col in range(colOrto1):
            for fil in range(filOrto1):
                if listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')

        for col in range(colOrto2):
            for fil in range(filOrto2):
                if (listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.buscarNodo(col, fil) == '*') and (listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil) == '*'):
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '-')
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.crearGrafo('Matriz_diferencia', colOrto1, filOrto1)
    else:
        
        listaMatrix1.insertarFinal(indice, 'Matriz_diferencia', colOrto2, filOrto2)
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.llenadoVacio(colOrto2, filOrto2)
        for col in range(colOrto1):
            for fil in range(filOrto1):
                if listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.buscarNodo(col, fil) == '*':
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '*')

        for col in range(colOrto2):
            for fil in range(filOrto2):
                if (listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.buscarNodo(col, fil) == '*') and  (listaMatrix1.buscarPosicionMatriz(1).matrizOrtogonal.buscarNodo(col, fil) == '*'):
                    listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.buscarNodoSustituirDato(col, fil, '-')
        listaMatrix1.buscarNombreMatriz('Matriz_diferencia').matrizOrtogonal.crearGrafo('Matriz_diferencia', colOrto2, filOrto2)
    
    noImagen3 = Image.open('grafos/Matriz_diferencia.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=570, y=90)
    
    diferenciabtn = Button(marcoOperaciones, text='Diferencia', state=DISABLED)   #Deshabilitar botón secundario
    diferenciabtn.place(x=290, y=10)

    indice = indice + 1                                 #Indice de la lista simple enlazada para las matrices ortogonales


#------------------------------------------Operaciones para una matriz-----------------------------------------------

def mostrarOperaciones1():
    global marcoOperaciones
    messagebox.showinfo('Información', 'Las operaciones se aplicaran sobre la matriz cargada en el visor 1')

    marcoOperaciones = LabelFrame(marcoInicial, text="La operaciones para una matriz son:", height=120, width=600)
    marcoOperaciones.place(x=40, y= 350)
    rotacionHorizontal = Button(marcoOperaciones, text='Rotación horizontal', command=rotacionHorizontalMatriz)
    rotacionHorizontal.place(x=10, y=10)
    rotacionVertical = Button(marcoOperaciones, text='Rotación vertical', command=rotacionVerticalMatriz)
    rotacionVertical.place(x=160, y=10)
    transpuesta = Button(marcoOperaciones, text='Transpuesta', command=transpuestaMatriz)
    transpuesta.place(x=310, y=10)
    limpiarZona = Button(marcoOperaciones, text='Limpiar zona', command=limpiarZonaImagen)
    limpiarZona.place(x=420, y=10)
    agregarLineaHorizontal = Button(marcoOperaciones, text='Agregar línea horizontal', command=agregarLineaHorizontalMatriz)
    agregarLineaHorizontal.place(x=10, y=60)
    agregarLineaVertical = Button(marcoOperaciones, text='Agregar línea vertical', command=agregarLineaVerticallMatriz)
    agregarLineaVertical.place(x=160, y=60)
    agregarRectangulo = Button(marcoOperaciones, text='Agregar ractángulo', command=agregarRectanguloMatriz)
    agregarRectangulo.place(x=290, y=60)
    agregarTrianguloRectangulo = Button(marcoOperaciones, text='Agregar triángulo rectángulo', command=agregarTrianRecMatriz)
    agregarTrianguloRectangulo.place(x=410, y=60)
    
    operacionesbtn = Button(marcoInicial, text="Operaciones para una matriz", state=DISABLED)       #Deshabilitar botón principal
    operacionesbtn.place(x=200, y=20)


#-----------------------------------------Operaciones para dos matrices------------------------------------------------

def mostrarOperaciones2():
    global marcoOperaciones
    marcoOperaciones = LabelFrame(marcoInicial, text="La operaciones para dos matriz son:", height=120, width=600)
    marcoOperaciones.place(x=40, y= 350)
    unionbtn = Button(marcoOperaciones, text='Unión', command=unionMatrices)
    unionbtn.place(x=10, y=10)
    interseccionbtn = Button(marcoOperaciones, text='Intersección', command=interseccionMatrices)
    interseccionbtn.place(x=140, y=10)
    diferenciabtn = Button(marcoOperaciones, text='Diferencia', command=diferenciaMatrices)
    diferenciabtn.place(x=290, y=10)
    diferenciaSimetricabtn = Button(marcoOperaciones, text='Diferencia simétrica', command=diferenciaSimetricaMatrices)
    diferenciaSimetricabtn.place(x=400, y=10)

    operaciones2btn = Button(marcoInicial, text="Operaciones para dos matriz", state=DISABLED)       #Deshabilitar botón principal
    operaciones2btn.place(x=400, y=20)
    

#-----------------------------------------Reporte de procesos realizados------------------------------------------------

def reporteMatrices():
    global indice
    if indice > 1:
        asd
    else:
        messagebox.showinfo('No se puede realizar un roperte porque no se ha echo ninguna operación...')

#-------------------------------------Abrir cuadro de dialogo para buscar--------------------------------------------
def buscarXML():
    #Cuadro de dialogo para buscar y luego asignarlo a la variable texto
    rutaXML = filedialog.askopenfilename(title = "Seleccionar archivo XML")
    cargarXML(rutaXML)                                          #Método para abrir el archivo XML
       
    
#------------------------------------------#Widgets------------------------------------------------------------------
cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", command=buscarXML)
cargarArchivobtn.place(x=50, y=20)
operacionesbtn = Button(marcoInicial, text="Operaciones para una matriz", state=DISABLED)
operacionesbtn.place(x=200, y=20)
operaciones2btn = Button(marcoInicial, text="Operaciones para dos matriz", state=DISABLED)
operaciones2btn.place(x=400, y=20)
reportesArchivobtn = Button(marcoInicial, text="Reportes", command=reporteMatrices)
reportesArchivobtn.place(x=600, y=20)
ayudaArchivobtn = Button(marcoInicial, text="Ayuda")
ayudaArchivobtn.place(x=700, y=20)

visor1lbl = Label(marcoInicial, text='Visor 1')
visor1lbl.place(x=40, y=60)
noImagen1 = Image.open('grafos/no-image.png')
tamanoImagen1 = noImagen1.resize((250, 250))
renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
imagenlbl.image = renderizadoImagen1
imagenlbl.place(x=40, y=90)

visor2lbl = Label(marcoInicial, text='Visor 2')
visor2lbl.place(x=300, y=60)
noImagen2 = Image.open('grafos/no-image.png')
tamanoImagen2 = noImagen2.resize((250, 250))
renderizadoImagen2 = ImageTk.PhotoImage(tamanoImagen2)
imagen2lbl = Label(marcoInicial, image=renderizadoImagen2)
imagen2lbl.image = renderizadoImagen2
imagen2lbl.place(x=300, y=90)

visor3lbl = Label(marcoInicial, text='Resultado')
visor3lbl.place(x=570, y=60)
noImagen3 = Image.open('grafos/no-image.png')
tamanoImagen3 = noImagen3.resize((250, 250))
renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
imagen3lbl.image = renderizadoImagen3
imagen3lbl.place(x=570, y=90)


ventanaInicial.mainloop()                                       #Ejecutar hasta cerrar