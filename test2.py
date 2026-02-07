from pywinusb import hid
import vgamepad as vg
import time


gamepad = vg.VX360Gamepad()


def simulacion(lectura):
    print(lectura)
    gamepad.left_trigger(value=lectura[5])
    gamepad.right_trigger(value=lectura[6])
    y = ((lectura[2] + 130) * 65535 // 258) - 32768
    x = ((lectura[1] + 130) * 65535 // 258) - 32768
    gamepad.left_joystick(x_value=x, y_value=y)
    x = ((lectura[3] + 130) * 65535 // 258) - 32768
    y = ((lectura[4] + 130) * 65535 // 258) - 32768
    gamepad.right_joystick(x_value=x, y_value=y)
    gamepad.update()

all_devices = hid.HidDeviceFilter().get_devices()

if not all_devices:
    print("No se detectaron dispositivos HID")
    exit()

dispositivos = []
numDevice = 0
for device in all_devices:
    numDevice+=1
    print(f"Dispositivo {numDevice}: {device.product_name}")
    dispositivos.append(device.product_name)

numDevice = input("Ingresa el numero del dispositivo: ")
if(len(dispositivos)+1 < int(numDevice)):
    print("Dispositivo no disponible")
else:
    for device in all_devices:
        if(device.product_name == dispositivos[int(numDevice)-1]):
            print(f"Conectado a {device.product_name}")
            device.open()
            device.set_raw_data_handler(simulacion)
            print("Leyendo datos... mueve sticks o gatillos")
            input("Presiona ENTER para salir...")
            device.close()