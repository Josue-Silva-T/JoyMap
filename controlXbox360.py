from pywinusb import hid
import vgamepad as vg
import csv
import time

gamepad = vg.VX360Gamepad()
all_devices = hid.HidDeviceFilter().get_devices()

listaMando = []
mapeo = []

def simular(data):

    gamepad.left_trigger(value=data[5])
    gamepad.right_trigger(value=data[6])
    y = ((data[2] + 130) * 65535 // 258) - 32768
    x = ((data[1] + 130) * 65535 // 258) - 32768
    gamepad.left_joystick(x_value=x, y_value=y)
    x = ((data[3] + 130) * 65535 // 258) - 32768
    y = ((data[4] + 130) * 65535 // 258) - 32768
    gamepad.right_joystick(x_value=x, y_value=y)
    gamepad.update()

    if data[-1] != 0:
        if data[-1] & 1:
            print("lb presionado")
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        if data[-1] & 2:
            print("rb presionado")
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER) 
        if data[-1] & 4:
            print("lt presionado")
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        if data[-1] & 8:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        if data[-1] & 16:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
        if data[-1] & 32:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        if data[-1] & 64:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)  
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
    gamepad.update()

    if data[-2] != 0:
        if data[-2] & 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        if data[-2] & 2:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        if data[-2] & 4:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        if data[-2] & 8:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        if data[-2] & 16:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        if data[-2] & 32:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        if data[-2] & 64:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        if data[-2] & 128:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    gamepad.update()


def detener(dispositivo):  
    for bdispositivo in all_devices:
        if(bdispositivo.product_name == dispositivo):
            bdispositivo.close()

def simulacion(dispositivo, ruta_archivo):
    for bdispositivo in all_devices:
        if(bdispositivo.product_name == dispositivo):
            print(f"Conectado a {bdispositivo.product_name}")
            bdispositivo.open()
            with open(ruta_archivo) as file:
                csv_reader = csv.reader(file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    mando = row
                    mapeo.append(mando[-1])
                    del mando[-1]
                    listaMando.append(mando)
                    
            
            for i in range(len(listaMando)):
                for j in range(len(listaMando[i])):
                    listaMando[i][j] = int(listaMando[i][j])

            print(listaMando)
            print(mapeo)
            bdispositivo.set_raw_data_handler(lambda data: simular(data))
