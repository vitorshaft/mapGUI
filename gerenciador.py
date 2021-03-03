#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 01, 2021 11:12:38 AM -03  platform: Windows NT

import sys
from PIL import Image, ImageDraw, ImageGrab
width = 500
height = 500
center = height//2
white = (255,255,255)
black = (0,0,0)

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gerenciador_support
from tkinter import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Principal (root)
    gerenciador_support.init(root, top)
    root.mainloop()

w = None
def create_Principal(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Principal(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Principal (w)
    gerenciador_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Principal():
    global w
    w.destroy()
    w = None

class Principal:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x600+326+56")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Gerenciador de mapas")
        top.configure(background="#d9d9d9")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.05, rely=0.1, relheight=0.852, relwidth=0.9)
        self.Canvas1.configure(background="#4d4d4d")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        #self.Canvas1.pack()
        self.Canvas1.delete("all")
        self.img = PhotoImage(file="C:/Users/vitor/Documents/Python/mapGUI/mapa.png")
        self.Canvas1.create_image(0,0, anchor='nw', image=self.img)
        #mainloop()

        self.Desenhar = tk.Button(top)
        self.Desenhar.place(relx=0.05, rely=0.033, height=24, width=77)
        self.Desenhar.configure(activebackground="#ececec")
        self.Desenhar.configure(activeforeground="#000000")
        self.Desenhar.configure(background="#8ccef3")
        self.Desenhar.configure(disabledforeground="#a3a3a3")
        self.Desenhar.configure(foreground="#000000")
        self.Desenhar.configure(highlightbackground="#d9d9d9")
        self.Desenhar.configure(highlightcolor="black")
        self.Desenhar.configure(pady="0")
        self.Desenhar.configure(text='''Desenhar''')

        self.Abrir = tk.Button(top)
        self.Abrir.place(relx=0.2, rely=0.033, height=24, width=67)
        self.Abrir.configure(activebackground="#ececec")
        self.Abrir.configure(activeforeground="#000000")
        self.Abrir.configure(background="#8ccef3")
        self.Abrir.configure(disabledforeground="#a3a3a3")
        self.Abrir.configure(foreground="#000000")
        self.Abrir.configure(highlightbackground="#d9d9d9")
        self.Abrir.configure(highlightcolor="black")
        self.Abrir.configure(pady="0")
        self.Abrir.configure(text='''Abrir''')

        self.Salvar = tk.Button(top)
        self.Salvar.place(relx=0.333, rely=0.033, height=24, width=67)
        self.Salvar.configure(activebackground="#ececec")
        self.Salvar.configure(activeforeground="#000000")
        self.Salvar.configure(background="#8ccef3")
        self.Salvar.configure(disabledforeground="#a3a3a3")
        self.Salvar.configure(foreground="#000000")
        self.Salvar.configure(highlightbackground="#d9d9d9")
        self.Salvar.configure(highlightcolor="black")
        self.Salvar.configure(pady="0")
        self.Salvar.configure(text='''Salvar''', command=self.gravar(self.Canvas1))

        self.Rota = tk.Button(top)
        self.Rota.place(relx=0.467, rely=0.033, height=24, width=77)
        self.Rota.configure(activebackground="#ececec")
        self.Rota.configure(activeforeground="#000000")
        self.Rota.configure(background="#4d4d4d")
        self.Rota.configure(disabledforeground="#a3a3a3")
        self.Rota.configure(foreground="#ffffff")
        self.Rota.configure(highlightbackground="#d9d9d9")
        self.Rota.configure(highlightcolor="black")
        self.Rota.configure(pady="0")
        self.Rota.configure(text='''Gerar rota''')

    def gravar(self, fonte):
      	#imagem = Image.new("RGB",(width,height),black)
      	arquivo = "desenho.png"
      	x = root.winfo_rootx()+fonte.winfo_x()
      	y = root.winfo_rooty()+fonte.winfo_y()
      	x1 = x+fonte.winfo_width()
      	y1 = y+fonte.winfo_height()
      	#ImageGrab.grab().crop((x,y,x1,y1)).save(arquivo)
      	ImageGrab.grab().save(arquivo)	#esta tirando print da tela



if __name__ == '__main__':
    vp_start_gui()





