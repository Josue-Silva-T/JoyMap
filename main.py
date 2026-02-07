import pygame
import pygame_widgets
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.button import Button
from pywinusb import hid
import tkinter as tk
from tkinter import filedialog
import controlXbox360

root = tk.Tk()
root.withdraw()


ruta_archivo = ""

pygame.init()
win = pygame.display.set_mode((600, 400))

fuente = pygame.font.SysFont("Arial", 13)


def seleccionarArchivo():
    global ruta_archivo
    ruta_archivo = filedialog.askopenfilename(
    filetypes=[("Archivos CSV", "*.csv")]
    )
    


"""
    Enlista todos los dispositivos disponibles
    en el momento y los enumera
"""

all_devices = hid.HidDeviceFilter().get_devices()

dispositivos = []
numDispositivos = []
numDispositivo = 0
for dispositivo in all_devices:
    numDispositivo+=1
    numDispositivos.append(numDispositivo)
    print(f"Dispositivo {numDispositivo}: {dispositivo.product_name}")
    dispositivos.append(dispositivo.product_name)


selector = Dropdown(
    win, 50, 50, 200, 40, name='Selecciona un dispositivo',
    choices=dispositivos,
    borderRadius=10, colour=(200, 200, 200),values=dispositivos, direction='down'
)

Archivo = Button(
    # Mandatory Parameters
    win,270,50,100, 40,

    # Optional Parameters
    text='Archivo',
    fontSize=17, 
    margin=20,  
    inactiveColour=(200, 200, 200),  
    radius=10, 
    onClick=lambda: seleccionarArchivo() 
)

Comenzar = Button(
    win,390,50,100, 40,

    text='Comenzar',
    fontSize=17, 
    margin=20,  
    inactiveColour=(200, 200, 200),  
    radius=10, 
    onClick=lambda: controlXbox360.simulacion(selector.getSelected(), ruta_archivo) 
)


run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            controlXbox360.detener(selector.getSelected())

    
    win.fill((255, 255, 255))
    win.blit(fuente.render(ruta_archivo, True, (0,0,0,0)), (270, 90))
    pygame_widgets.update(events) # Actualiza los widgets
    pygame.display.update()
