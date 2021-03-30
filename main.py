from tkinter import *                               #Módulo para entorno gráfico

ventanaInicial = Tk()                               #Objeto de tipo ventana
ventanaInicial.title('Proyecto 2 - IPC2')
ventanaInicial.resizable(False, False)              #No permitir cambios al ancho y alto de la ventana

marcoInicial = Frame()
marcoInicial.pack(fill="both", expand="True")                                 #Marco agregado a la ventana
marcoInicial.config(width="900", height="650")

ventanaInicial.mainloop()                           #Ejecutar hasta cerrar