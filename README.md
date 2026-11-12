# 🎮 JoyMap

Programa para usar el mando **SteelSeries Nimbus+** en Windows como si fuera un **mando de Xbox 360**. Lee los datos crudos del mando por HID y los reenvía a un mando virtual, así que los juegos lo reconocen sin configuración adicional.

![Interfaz de JoyMap](https://github.com/user-attachments/assets/4701997a-5595-41e9-8bc0-26127be41a8d)

## Cómo funciona

```
┌──────────────┐   HID (datos crudos)   ┌──────────────────┐   XInput   ┌─────────┐
│ Mando Nimbus+│ ─────────────────────► │      JoyMap      │ ─────────► │  Juego  │
└──────────────┘      (pywinusb)        │ (mando virtual   │ (ViGEmBus) └─────────┘
                                        │   Xbox 360)      │
                                        └──────────────────┘
```

1. Se listan los dispositivos HID conectados.
2. Eliges el mando y un archivo CSV con el mapeo.
3. Al pulsar **Comenzar**, cada reporte HID se traduce a ejes, gatillos y botones de un mando virtual Xbox 360.

## Requisitos

- Windows
- Python 3.8+
- [ViGEm Bus Driver](https://vigembusdriver.com/) (obligatorio, crea el mando virtual)
- Librerías de Python:

```bash
pip install pywinusb vgamepad pygame pygame-widgets
```

`tkinter` viene incluido con Python en Windows.

## Uso

```bash
python main.py
```

1. Conecta el mando (por cable o Bluetooth).
2. Selecciona tu mando en el menú **Selecciona un dispositivo**.
3. Pulsa **Archivo** y elige el CSV de mapeo. La ruta aparece debajo del botón.
4. Pulsa **Comenzar**. El mando virtual queda activo mientras el programa esté abierto.
5. Cierra la ventana para liberar el dispositivo.
