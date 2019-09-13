''' Python script on motioneyeos to turn on/off motion detection by GPiO Pin [switch]
Whole idea of script is watching state of state GPiO pins and setting up a motiondetection by loscalhost command
For cam nr 0:

Motiondetection OFF = 'curl http://localhost:8080/0/detection/pause'
Motiondetection ON = 'curl http://localhost:8080/0/detection/start'

'''

import RPi.GPIO as GPIO                                             
import time
import os

class Kamera:
    '''
    Class Kamera have num, state, and t_pasuse
    num is a camera number in motion starts from 0
    state us a state motion detection [ start = ON, pause = OFF]
    t_pause is a delay time 
    '''
    def __init__(self, num, state='start', t_pause = 0.1):
        self.num = num
        self.state = state
        self.t_pause = t_pause

    def consol(self):
        con = 'curl http://localhost:8080/{}/detection/{}'.format(self.num, self.state)
        return os.system(con)

def start_rec(*argv):
        for arg in argv:
            arg.state = 'start'                
            arg.consol()
            time.sleep(arg.t_pause)

def pause_rec(*argv):
        for arg in argv:
            arg.state = 'pause'                        
            arg.consol()
            time.sleep(arg.t_pause)


kam1 = Kamera(0)
kam2 = Kamera(1)
kam3 = Kamera(2)
pin = 27
d_stat = 'close'

#GPIO.cleanup()
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('motion on off - 2drzwi.py')
while True:
     time.sleep(5)
     input_state = GPIO.input(pin)
#     print(input_state)
     if input_state == True and d_stat == 'open':
         start_rec(kam1, kam2, kam3)
         d_stat = 'close'
#         print('zamknietet') 
     elif input_state == False and d_stat == 'close':
         time.sleep(120)
         pause_rec(kam1, kam2, kam3)
         d_stat = 'open'
#         print('OTWARTE')

