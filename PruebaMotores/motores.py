import RPi.GPIO as GPIO
import tkinter as tk
import time
import threading

# Configuración de pines GPIO
GPIO.setmode(GPIO.BCM)
motor_pins = {"motor1": [17, 18], "motor2": [27, 22], "motor3": [27, 24]}
limit_switch_pins = [25, 5, 6, 12, 13, 19]

for motor, pins in motor_pins.items():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

for pin in limit_switch_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Funciones para controlar los motores
def girar_motor(motor, sentido):
    GPIO.output(motor_pins[motor][sentido], GPIO.HIGH)
    GPIO.output(motor_pins[motor][1 - sentido], GPIO.LOW)

def detener_motor(motor):
    for pin in motor_pins[motor]:
        GPIO.output(pin, GPIO.LOW)

def controlar_motor(motor, sentido, limit_switch):
    girar_motor(motor, sentido)
    while not GPIO.input(limit_switch):
        time.sleep(0.1)
    detener_motor(motor)

# Funciones para controlar los botones
def abrir():
    t1 = threading.Thread(target=controlar_motor, args=("motor1", 0, limit_switch_pins[0]))
    t2 = threading.Thread(target=controlar_motor, args=("motor2", 0, limit_switch_pins[1]))
    t3 = threading.Thread(target=controlar_motor, args=("motor3", 0, limit_switch_pins[2]))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

def cerrar():
    t1 = threading.Thread(target=controlar_motor, args=("motor1", 1, limit_switch_pins[3]))
    t2 = threading.Thread(target=controlar_motor, args=("motor2", 1, limit_switch_pins[4]))
    t3 = threading.Thread(target=controlar_motor, args=("motor3", 1, limit_switch_pins[5]))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Control de Motores")

# Botones
btn_abrir = tk.Button(root, text="Abrir", command=abrir)
btn_abrir.pack(pady=10)

btn_cerrar = tk.Button(root, text="Cerrar", command=cerrar)
btn_cerrar.pack(pady=10)

# Ejecuta la interfaz gráfica
root.mainloop()

# Limpia los pines GPIO y termina la ejecución cuando el programa se detiene
GPIO.cleanup()