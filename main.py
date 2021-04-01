from tkinter import filedialog                      #Módulo para abrir ventana de selección
from tkinter import messagebox                      #Módulo para cuadros de mensaje
from tkinter import *                               #Módulo para entorno gráfico
from nodoMatrix import listaMatrizOrtogonal         #Módulo para crear lista enlazada simplde de matrices ortogonales
from PIL import Image, ImageTk                      #Instalar módulo, pip install Pillow, para usar imagenes con más opciones

import xml.etree.ElementTree as ET                  #importando libreria para manipular XML


#-------------------------------------------Ventana inicial-----------------------------------------------------------
ventanaInicial = Tk()                                           #Objeto de tipo ventana
ventanaInicial.title('Proyecto 2 - IPC2')
ventanaInicial.resizable(False, False)                          #No permitir cambios al ancho y alto de la ventana

marcoInicial = Frame(ventanaInicial, width="830", height="500")
marcoInicial.pack()                                             #Marco agregado a la ventana


#--------------------------------------------Manejo del XML------------------------------------------------------------
documentoXML = None                                             #Variable para el archivo XML
matricesRaiz = None                                             #Variable para la etiqueta matrices y así poder iterar
listaMatrix1 = listaMatrizOrtogonal()                 #Creación de lista simple enlazada para las matrices ortogonales
indice = 0                                            #Indice global para saber cuantas matrices ortogonales existen
marcoOperaciones = None

def cargarXML(ruta):
    global documentoXML
    global matricesRaiz
    global listaMatrix1
    #try:
    documentoXML = ET.parse(ruta)                           #Conviritendo a legible
    matricesRaiz = documentoXML.getroot()                   #Obteniendo la raíz del XML
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

    for matriz in matricesRaiz:                         #Todas las etiquetas de cada matriz son asignadas al elemento
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
        
        indice = indice + 1 
    cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", state=DISABLED)  #Deshabilitar botón principal
    cargarArchivobtn.place(x=50, y=20)
    mostrarImagenes(indice, nombreM1, nombreM2)
        

#-----------------------------------------Mostrar imagenes en los visores------------------------------------------    
def mostrarImagenes(indice, nombreM1, nombreM2):
    if indice == 1:
        imagen1 = Image.open('grafos/' + nombreM1 + '.dot.png')
        tamanoImagen1 = imagen1.resize((250, 250))
        renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
        imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
        imagenlbl.image = renderizadoImagen1
        imagenlbl.place(x=40, y=70)
    else:
        imagen1 = Image.open('grafos/' + nombreM1 + '.dot.png')
        tamanoImagen1 = imagen1.resize((250, 250))
        renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
        imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
        imagenlbl.image = renderizadoImagen1
        imagenlbl.place(x=40, y=70)

        imagen2 = Image.open('grafos/' + nombreM2 + '.dot.png')
        tamanoImagen2 = imagen2.resize((250, 250))
        renderizadoImagen2 = ImageTk.PhotoImage(tamanoImagen2)
        imagen2lbl = Label(marcoInicial, image=renderizadoImagen2)
        imagen2lbl.image = renderizadoImagen2
        imagen2lbl.place(x=300, y=70)

#-------------------------------Proceso rotación horizontal de una matriz---------------------------------------------
def rotacionHorizontalMatriz():
    global listaMatrix1
    global indice
    global marcoOperaciones

    colNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).columnas
    filNuevaOrtogonal = listaMatrix1.buscarPosicionMatriz(0).filas
    listaMatrix1.insertarFinal(indice, 'Matriz_Rotacion_Horizontal', colNuevaOrtogonal, filNuevaOrtogonal) #Se crea el nodo con posición y NOMBRE
    cadenaMatrizOrtogonal0 = listaMatrix1.buscarPosicionMatriz(0).matrizOrtogonal.devolvercadena(colNuevaOrtogonal, filNuevaOrtogonal)
    #print(cadenaMatrizOrtogonal0)
    listaMatrix1.buscarNombreMatriz('Matriz_Rotacion_Horizontal').matrizOrtogonal.llenadoRotacionHorizontal(colNuevaOrtogonal, filNuevaOrtogonal, cadenaMatrizOrtogonal0)
    listaMatrix1.buscarNombreMatriz('Matriz_Rotacion_Horizontal').matrizOrtogonal.crearGrafo('Matriz_Rotacion_Horizontal', colNuevaOrtogonal, filNuevaOrtogonal)
    noImagen3 = Image.open('grafos/Matriz_Rotacion_Horizontal.dot.png')
    tamanoImagen3 = noImagen3.resize((250, 250))
    renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
    imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
    imagen3lbl.image = renderizadoImagen3
    imagen3lbl.place(x=550, y=70)
    
    rotacionHorizontal = Button(marcoOperaciones, text='Rotación horizontal', state=DISABLED)   #Deshabilitar botón secundario
    rotacionHorizontal.place(x=10, y=10)

    indice = indice + 1


#---------------------------------Mostrar operaciones que se pueden realizar----------------------------------------

def mostrarOperaciones():
    global marcoOperaciones

    if indice == 1:
        marcoOperaciones = LabelFrame(marcoInicial, text="La operaciones para una matriz son:", height=120, width=600)
        marcoOperaciones.place(x=40, y= 350)
        rotacionHorizontal = Button(marcoOperaciones, text='Rotación horizontal', command=rotacionHorizontalMatriz)
        rotacionHorizontal.place(x=10, y=10)
        rotacionVertical = Button(marcoOperaciones, text='Rotación vertical')
        rotacionVertical.place(x=160, y=10)
        transpuesta = Button(marcoOperaciones, text='Transpuesta')
        transpuesta.place(x=310, y=10)
        limpiarZona = Button(marcoOperaciones, text='Limpiar zona')
        limpiarZona.place(x=420, y=10)
        agregarLineaHorizontal = Button(marcoOperaciones, text='Agregar línea horizontal')
        agregarLineaHorizontal.place(x=10, y=60)
        agregarLineaVertical = Button(marcoOperaciones, text='Agregar línea vertical')
        agregarLineaVertical.place(x=160, y=60)
        agregarRectangulo = Button(marcoOperaciones, text='Agregar ractángulo')
        agregarRectangulo.place(x=290, y=60)
        agregarTrianguloRectangulo = Button(marcoOperaciones, text='Agregar triángulo rectángulo')
        agregarTrianguloRectangulo.place(x=410, y=60)
    else:
        marcoOperaciones = LabelFrame(marcoInicial, text="La operaciones para dos matriz son:", height=120, width=600)
        marcoOperaciones.place(x=40, y= 350)
    
    operacionesbtn = Button(marcoInicial, text="Operaciones", state=DISABLED)       #Deshabilitar botón principal
    operacionesbtn.place(x=200, y=20)


#-------------------------------------Abrir cuadro de dialogo para buscar--------------------------------------------
def buscarXML():
    #Cuadro de dialogo para buscar y luego asignarlo a la variable texto
    rutaXML = filedialog.askopenfilename(title = "Seleccionar archivo XML")
    cargarXML(rutaXML)                                          #Método para abrir el archivo XML
       
    
#------------------------------------------#Widgets------------------------------------------------------------------
cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", command=buscarXML)
cargarArchivobtn.place(x=50, y=20)
operacionesbtn = Button(marcoInicial, text="Operaciones", command=mostrarOperaciones)
operacionesbtn.place(x=200, y=20)
reportesArchivobtn = Button(marcoInicial, text="Reportes" )
reportesArchivobtn.place(x=320, y=20)
ayudaArchivobtn = Button(marcoInicial, text="Ayuda")
ayudaArchivobtn.place(x=410, y=20)

noImagen1 = Image.open('grafos/no-image.png')
tamanoImagen1 = noImagen1.resize((250, 250))
renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
imagenlbl.image = renderizadoImagen1
imagenlbl.place(x=40, y=70)

noImagen2 = Image.open('grafos/no-image.png')
tamanoImagen2 = noImagen2.resize((250, 250))
renderizadoImagen2 = ImageTk.PhotoImage(tamanoImagen2)
imagen2lbl = Label(marcoInicial, image=renderizadoImagen2)
imagen2lbl.image = renderizadoImagen2
imagen2lbl.place(x=300, y=70)

noImagen3 = Image.open('grafos/no-image.png')
tamanoImagen3 = noImagen3.resize((250, 250))
renderizadoImagen3 = ImageTk.PhotoImage(tamanoImagen3)
imagen3lbl = Label(marcoInicial, image=renderizadoImagen3)
imagen3lbl.image = renderizadoImagen3
imagen3lbl.place(x=550, y=70)


ventanaInicial.mainloop()                                       #Ejecutar hasta cerrar