from googletrans import Translator
import sys
from plyer import *
import time
import os
import pyperclip

def translateMe(word):
    translatedWord = Translator().translate(word, dest='ar')
    notification.notify(
        title=translatedWord.origin,
        message=translatedWord.text,
        app_name='Targmly',
        #ticker='',
        #app_icon='avatar.ico',
        timeout=10
    )

sys.path.append(os.path.abspath("SO_site-packages"))
recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        translateMe(recent_value)
    time.sleep(0.1)