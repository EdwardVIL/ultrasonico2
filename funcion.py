import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Set GPIO numbering mode
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

def servo():
    #start PWM running, but with value of 0 (pulse off)
    servo1.start(0)
    print ("Waiting for 2 seconds")
    time.sleep(2)
    #Let's move the servo!
    print ("Rotating 180 degrees in 10 steps")
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
    print ("Turning back to 90 degrees for 2 seconds")
    servo1.ChangeDutyCycle(7)
    time.sleep(2)
    #turn back to 0 degrees
    print ("Turning back to 0 degrees")
    servo1.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print ("Goodbye")

def ultrasonico():
    archivo=open("distancia.txt","w")
    while True:
        GPIO.output(18,1)
        time.sleep(0.000001)
        GPIO.output(18,0)
        inicio=time.time()
        while(GPIO.input(16)==GPIO.LOW):
            inicio=time.time()
        while(GPIO.input(16)==GPIO.HIGH):
            final=time.time()
        tiempo=final-inicio
        distancia=tiempo*34000/2
        if distancia>=2 and distancia<=400:
            archivo.write("distancia: "+str(distancia)+chr(10))
            print(distancia)
        if (time.time()-init_tiempo)>=30:
            break
    archivo.close()
    print("PROGRAMA HA FINALIZADO")
    import RPi.GPIO as GPIO
    import time
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.IN)
    GPIO.setup(18,GPIO.OUT)
    init_tiempo=time.time()
    archivo=open("distancia.txt","w")
    while True:
        GPIO.output(18,1)
        time.sleep(0.000001)
        GPIO.output(18,0)
        inicio=time.time()
        while(GPIO.input(16)==GPIO.LOW):
            inicio=time.time()
        while(GPIO.input(16)==GPIO.HIGH):
            final=time.time()
        tiempo=final-inicio
        distancia=tiempo*34000/2
        if distancia>=2 and distancia<=400:
            archivo.write("distancia: "+str(distancia)+chr(10))
            print(distancia)
        if (time.time()-init_tiempo)>=30:
            break
    archivo.close()
    print("PROGRAMA HA FINALIZADO")
    
servo()
ultrasonico()
