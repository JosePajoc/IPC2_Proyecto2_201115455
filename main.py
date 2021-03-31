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

marcoInicial = Frame(ventanaInicial, width="800", height="550")
marcoInicial.pack()                                             #Marco agregado a la ventana


#--------------------------------------------Manejo del XML------------------------------------------------------------
documentoXML = None                                             #Variable para el archivo XML
matricesRaiz = None                                             #Variable para la etiqueta matrices y así poder iterar
listaMatrix1 = listaMatrizOrtogonal()                 #Creación de lista simple enlazada para las matrices ortogonales


def cargarXML(ruta):
    global documentoXML
    global matricesRaiz
    global listaMatrix1
    try:
        documentoXML = ET.parse(ruta)                           #Conviritendo a legible
        matricesRaiz = documentoXML.getroot()                   #Obteniendo la raíz del XML
        messagebox.showinfo("información", "Se cargo con éxtio...\n\nEl archivo se encuentra en:\n" + ruta)
        procesarXML()
    except:
        messagebox.showinfo("información", "No se pudo cargar el archivo...")


def procesarXML():
    global documentoXML
    global matricesRaiz
    
    indice = 0
    for matriz in matricesRaiz:                         #Todas las etiquetas de cada matriz son asignadas al elemento
        #print('El nombre de la matriz es ', matriz[0].text)
        filas = int(matriz[1].text)                             #Valor de la etiqueta filas del XML
        columnas = int(matriz[2].text)                          #Valor de la etiqueta columnas del XML
        
        imagenEntrada =  matriz[3].text.replace(' ', '')        #Quitando espacios en blanco de la imagen
        imagenSinSaltos = imagenEntrada.replace('\n','')        #Sustitución de saltos por &
        #print('Filas: ', matriz[1].text)                        #<------------------QUITAR
        #print('Columnas: ', matriz[2].text)                     #<------------------QUITAR
        #print('Imagen: ', imagenSinSaltos)                      #<------------------QUITAR
        #matrizOrto1 = matrizOrtogonal()                         #Instanciando matriz ortogonal
        #matrizOrto1.llenado(columnas, filas, imagenSinSaltos)   
        #matrizOrto1.mostrarMatriz(columnas, filas)    

        listaMatrix1.insertarFinal(indice, matriz[0].text)      #Se crea el nodo con posición y nombre
        #Se busca el nodo creado, se llama al atributo tipo matriz ortogonal, se llena la matriz con la info de la imagen del XML
        listaMatrix1.buscarPosicionMatriz(indice).matrizOrtogonal.llenado(columnas, filas, imagenSinSaltos)
        #listaMatrix1.buscarPosicionMatriz(indice).matrizOrtogonal.mostrarMatriz(columnas, filas)
        #Crear imagenes a partir de la matriz ortogonal
        listaMatrix1.buscarPosicionMatriz(indice).matrizOrtogonal.crearGrafo(matriz[0].text, filas, columnas)
        indice = indice + 1 
        #print('----------------------------------------------------------------------------------------------\n')
    mostrarImagenes()
        
    
def mostrarImagenes():
    imagen1 = Image.open('grafos/Matriz_1.dot.png')
    tamanoImagen1 = imagen1.resize((250, 250))
    renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
    imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
    imagenlbl.image = renderizadoImagen1
    imagenlbl.place(x=40, y=70)

    imagen2 = Image.open('grafos/Matriz_2.dot.png')
    tamanoImagen2 = imagen2.resize((250, 250))
    renderizadoImagen2 = ImageTk.PhotoImage(tamanoImagen2)
    imagen2lbl = Label(marcoInicial, image=renderizadoImagen2)
    imagen2lbl.image = renderizadoImagen2
    imagen2lbl.place(x=300, y=70)
    

#-------------------------------------Abrir cuadro de dialogo para buscar--------------------------------------------
def buscarXML():
    #Cuadro de dialogo para buscar y luego asignarlo a la variable texto
    rutaXML = filedialog.askopenfilename(title = "Seleccionar archivo XML")
    cargarXML(rutaXML)                                          #Método para abrir el archivo XML
       
    
#------------------------------------------#Widgets------------------------------------------------------------------
cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", command=buscarXML)
cargarArchivobtn.place(x=50, y=20)
operacionesbtn = Button(marcoInicial, text="Operaciones")
operacionesbtn.place(x=200, y=20)
reportesArchivobtn = Button(marcoInicial, text="Reportes" )
reportesArchivobtn.place(x=320, y=20)
ayudaArchivobtn = Button(marcoInicial, text="Ayuda")
ayudaArchivobtn.place(x=410, y=20)


ventanaInicial.mainloop()                                       #Ejecutar hasta cerrar