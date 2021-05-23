import RPi.GPIO as GPIO
import time
import threading
GPIO.setwarnings(False)
init_tiempo=time.time()
TRIG = 18
ECHO = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
#GPIO.setup(16,GPIO.IN)
#GPIO.setup(18,GPIO.OUT)

def servo():
    try:
        while True: 
            GPIO.setup(11,GPIO.OUT)
            
            #start PWM running, but with value of 0 (pulse off)
            servo1.start(0)
            print ("Inicio de servo")
            time.sleep(2)
            #Let's move the servo!
            print ("Rotando 180")
            # Define variable duty
            duty = 2
            # Loop for duty values from 2 to 12 (0 to 180 degrees)
            while duty <= 12:
                servo1.ChangeDutyCycle(duty)
                time.sleep(1)
                duty = duty + 1
            # Wait a couple of seconds
            time.sleep(2)
            # Turn back to 90 degrees
            print ("regresando a 90")
            servo1.ChangeDutyCycle(7)
            time.sleep(2)
            #turn back to 0 degrees
            print ("regresando a 0")
            servo1.ChangeDutyCycle(2)
            time.sleep(0.5)
            servo1.ChangeDutyCycle(0)
            #Clean things up at the end
            servo1.stop()
            GPIO.cleanup()
            print ("Fin de servo")
    finally:
        GPIO.cleanup()


def ultrasonico():
    try:
        #print("Medicion de distancias en progreso")
    
        while True:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)
            GPIO.output(TRIG, GPIO.LOW)
            #print("Esperando a que el sensor se estabilice")
            time.sleep(2)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.output(TRIG, GPIO.LOW)
            #print("Iniciando eco")
            while True:  
                pulso_inicio = time.time()
                GPIO.setup(ECHO, GPIO.IN)
                if GPIO.input(ECHO) == GPIO.HIGH:
                    break
            while True:
                pulso_fin = time.time()
                GPIO.setup(ECHO, GPIO.IN)
                if GPIO.input(ECHO) == GPIO.LOW:
                    break
            duracion = pulso_fin - pulso_inicio
            distancia = (34300 * duracion) / 2
            print("Distancia: %.2f cm" % distancia)

    finally:
        GPIO.cleanup()



t = threading.Thread(target=ultrasonico, name='ultrasonico')
w = threading.Thread(target=servo, name='servo')
t.start()
w.start()
