import random
import re
from time import sleep

####
from Buyer import Refresher
import pyautogui
import pytesseract
import uuid
# while(not Refresher((2260,220,200,45), '[^a-zA-Z]', 'stock')):
#     print('Not found...', flush=True)
#     sleep(0.1)
# while(not Refresher((1050,680,460,40), '[^a-zA-Z]', 'purchased')): #for checking already purchased message
#     print('Not found...', flush=True)
#     sleep(0.1)
sleep(2)

retry_counter = 0
while(retry_counter < 1):
    print('Checking if successful... retries: %i' % retry_counter, end='\r', flush=True)
    if(retry_counter >= 50):
        print('\nERROR: Retry limit reached.')
        break
    if(retry_counter < 50 and Refresher((1780, 192, 220, 88), '\D', '920', 50, True, "test msg")):
        print('\n Purchase successful! Saving img... \n')
        log_img = pyautogui.screenshot()
        log_img.save('purchase_logs/'+str(uuid.uuid4())+'.png')
        break
    retry_counter += 1
    sleep(0.1)

###


list = ['wkcup',
'@4sd7',
'v!fry',
'17 rl',
'u3k1k',
'xl7t3',
'j0bl2',
'ivmv2',
'rhs6l',
'n0io4',
'79c9j',
'q7rce',
'r0dl1',
'3lht6',
'gyw7u',
'y42mz',
'avswi',
'4q1la',
'p3mzj',
'j8kty',
'yvp11',
'wcre6',
'bfv3w',
'4hsc8',
'u4eub',
'vtnkl',
'3py9c',
'6inlx',
'nt9ec',
'2e8ku',
]

#using re -- approx TIME TAKEN (real): 0.039s
# for var in list:
#     print('poo:{}!'.format(re.sub("\D", "", var)))

#using join + isdigit + filter -- approx TIME TAKEN (real): 0.038s
# for var in list:
#     print('poo:{}!'.format(''.join(filter(lambda i: i.isdigit(), var)) ))

# for var in list:
#     print('poo:{}!'.format(re.sub("[^a-zA-Z]", "", var)))