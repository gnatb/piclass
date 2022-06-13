#!/usr/bin/env python


from gpiozero import LED
from time import sleep

led = LED(25)


def shortSig():
    print('short')
    led.on ()
    sleep (0.5)
    led.off()
    sleep(0.5)
    
def longSig ():
    print('long')
    led.on ()
    sleep (1.5)
    led.off()
    sleep(0.5)

sosMsg = input ('Enter your message:')
print(sosMsg)
sosLen = len(sosMsg)
print (sosLen)



while True:

    counter = 0
    
    while counter < sosLen:
        sosLetter = sosMsg[counter]
        sleep(3)
    
        print (sosLetter)
    
        if (sosLetter == 'a'):
            shortSig()
            longSig()
        elif (sosLetter == 'b') :
            longSig ()
            shortSig()
            shortSig()
            shortSig()
        elif (sosLetter == 'c'):
            longSig()
            shortSig()
            longSig()
            shortSig()
        elif (sosLetter== 'd'):
            longSig()
            shortSig()
            shortSig()
        else:
            print ('done')
    
        counter = counter + 1



