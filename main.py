from tkinter import filedialog                      #Módulo para abrir ventana de selección
from tkinter import messagebox                      #Módulo para cuadros de mensaje
from io import open                                 #Módulo para abrir el archivo
from tkinter import *                               #Módulo para entorno gráfico

import xml.etree.ElementTree as ET                  #importando libreria para manipular XML

#---------------------------------------Manejo del XML-----------------------------------------------------------
documentoXML = None                                   #Variable para el archivo XML
matricesRaiz = None                                   #Variable para la etiqueta matrices y así poder iterar

def cargarXML(ruta):
    global documentoXML
    global matricesRaiz
    try:
        documentoXML = ET.parse(ruta)                           #Conviritendo a legible
        matricesRaiz = documentoXML.getroot()                   #Obteniendo la raíz
        messagebox.showinfo("información", "Se cargo con éxtio...\n\nEl archivo se encuentra en:\n" + ruta)
        procesarXML()
    except:
        messagebox.showinfo("información", "No se pudo cargar el archivo...")

def procesarXML():
    global documentoXML
    global matricesRaiz
    



#----------------------------------------Ventana inicial-----------------------------------------------------------
ventanaInicial = Tk()                               #Objeto de tipo ventana
ventanaInicial.title('Proyecto 2 - IPC2')
ventanaInicial.resizable(False, False)              #No permitir cambios al ancho y alto de la ventana

marcoInicial = Frame(ventanaInicial, width="900", height="650")
marcoInicial.pack()                                 #Marco agregado a la ventana

#-------------------------------------Método para bótones------------------------------------------------------------
def buscarXML():
    #Cuadro de dialogo para buscar y luego asignarlo a la variable texto
    rutaXML = filedialog.askopenfilename(title = "Seleccionar archivo XML")
    cargarXML(rutaXML)
       
    
#------------------------------------------#Widgets------------------------------------------------------------------
cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", command=buscarXML)
cargarArchivobtn.place(x=50, y=20)
operacionesbtn = Button(marcoInicial, text="Operaciones")
operacionesbtn.place(x=200, y=20)
reportesArchivobtn = Button(marcoInicial, text="Reportes" )
reportesArchivobtn.place(x=320, y=20)
ayudaArchivobtn = Button(marcoInicial, text="Ayuda")
ayudaArchivobtn.place(x=410, y=20)



ventanaInicial.mainloop()                           #Ejecutar hasta cerrar