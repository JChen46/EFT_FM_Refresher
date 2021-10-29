import pyautogui
import pytesseract
import re
from time import sleep
import winsound
import uuid

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/John Chen/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

def Scanner(buy_price):
    print('in scanner', flush=True)

    if(Refresher(region=(1780, 192, 220, 88), regex='[^0-9]', keyword=buy_price, retries=10, msg='Checking price...', check_price=True)):
        PurchaseItem()

    return False

def PurchaseItem():
    purchase_approval = True
    if(Refresher(region=(2260,220,200,45), regex='[^a-zA-Z]', keyword='purchase', retries=1000, msg='Waiting to buy...', check_price=False)):
        purchase_approval = True

    # while(not Refresher((2260,220,200,45), '[^a-zA-Z]', 'purchase', 1, 'Waiting to buy...')):
    #     if(retry_counter > timeout):
    #         print('\nERROR: Retry limit reached.')
    #         purchase_approval = False
    #         break
    #     print('Waiting to buy... retries: %i' % retry_counter, end='\r', flush=True)
    #     retry_counter += 1
    #     sleep(0.1)

    if(purchase_approval):
        pyautogui.click(x=2360, y=244) #click purchase button
        winsound.Beep(988, 120) ; winsound.Beep(784, 120) ; winsound.Beep(988, 120) ; winsound.Beep(784, 120)
        # take picture for logging
        log_img = pyautogui.screenshot()

        pyautogui.press('y') # AUTO purchases item
        # Check if purchase is successful
        if(Refresher(region=(1050,680,460,40), regex='[^a-zA-Z]', keyword='purchased', retries=50, msg="Checking if successful...", check_price=False)):
            # Save image of purchase to purchase_logs directory
            file_name = 'purchase_logs/'+str(uuid.uuid4())+'.png'
            print('\n --- Purchase successful! Saving img as {}! --- \n'.format(file_name))
            log_img.save(file_name)

        # retry_counter = 0
        # while(True):
        #     print('Checking if successful... retries: %i' % retry_counter, end='\r', flush=True)
        #     if(retry_counter > 50):
        #         break
        #     if(retry_counter <= 50 and Refresher((1050,680,460,40), '[^a-zA-Z]', 'purchased', False)): # Successfully purchased item
        #         
        #         break
        #     retry_counter += 1
        #     sleep(0.1)

def Refresher(region, regex, keyword, retries, check_price, msg): #region is of type (left, top, width, height)
    retry_count = 0
    while(retry_count < retries):
        
        print(msg+'| Retries: %i' % retry_count, end='\r', flush=True)
        
        region_img = pyautogui.screenshot(region=region)
        region_img.save('wtf.png') # temp save to see
        raw_result = pytesseract.image_to_string(region_img)
        processed_result = re.sub(regex, "", raw_result)
        print('\nRefresher result is: {}!'.format(processed_result), flush=True)
        try:
            if(not check_price):
                if(keyword.lower() in processed_result.lower()):
                    print('\nFOUND!')
                    return True
                else:
                    return False
            else: #called from Scanner
                if(int(processed_result) <= int(keyword)):
                    return True
        except ValueError:
            pass
        retry_count += 1
        sleep(0.1)
    print('\nERROR: Retry limit reached.', flush=True)
    return False
