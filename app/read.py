
import random
import string
from gtts import gTTS

language = 'pt-br'


def readAndSave(text):
    audio = gTTS(text=text, lang=language, slow=False,)
    letters = string.ascii_uppercase
    fileName = './habla/'+(''.join(random.choice(letters)
                                 for i in range(10)))+'.mp3'
    audio.save(fileName)
    return fileName
