from tkinter import filedialog                      #Módulo para abrir ventana de selección
from io import open                                 #Módulo para abrir el archivo
from tkinter import *                               #Módulo para entorno gráfico

ventanaInicial = Tk()                               #Objeto de tipo ventana
ventanaInicial.title('Proyecto 2 - IPC2')
ventanaInicial.resizable(False, False)              #No permitir cambios al ancho y alto de la ventana

marcoInicial = Frame(ventanaInicial, width="900", height="650")
marcoInicial.pack()                                 #Marco agregado a la ventana

#------------------------------------------------------------------------------------------------------------------
rutaXML = StringVar()                               #Variable para usar global

def buscarXML():
    #Cuadro de dialogo para buscar y luego asignarlo a la variable texto
    rutaXML.set(filedialog.askopenfilename(title = "Seleccionar archivo XML"))   
    
#-------------------------------------------------------------------------------------------------------------------

#Widgets
cargarArchivobtn = Button(marcoInicial, text="Cargar archivo XML", command=buscarXML)
cargarArchivobtn.place(x=50, y=20)
operacionesbtn = Button(marcoInicial, text="Operaciones")
operacionesbtn.place(x=200, y=20)
reportesArchivobtn = Button(marcoInicial, text="Reportes" )
reportesArchivobtn.place(x=320, y=20)
ayudaArchivobtn = Button(marcoInicial, text="Ayuda")
ayudaArchivobtn.place(x=410, y=20)

rutaTextolbl = Label(marcoInicial, text="El archivo se encuentra en:")
rutaTextolbl.place(x=50, y=70)
rutalbl = Label(marcoInicial, textvariable=rutaXML)
rutalbl.place(x=50, y=90)



ventanaInicial.mainloop()                           #Ejecutar hasta cerrar