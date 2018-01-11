import autopy3 as autopy
import os
#from autopy3.bitmap import capture_screen
import string
import random
def id_generator(size=6,chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def screenshot():
    autopy.bitmap.capture_screen().save(os.getcwd()+'\\Screenshot\\'+id_generator()+'.png')
screenshot()
