from time import time, sleep

import keyboard
bean = True
while 1:

    sleep(1)
    if not bean :
        print('This frame takes {} seconds.'.format(time()-begin_time))
    print(time())
    if bean :
        begin_time = time()
        bean = not bean

    if time()-begin_time > 10 :
        print('over ten')
        break
    else :
        print('not over 10')
    sleep(1)
    if keyboard.is_pressed('q'):
        break