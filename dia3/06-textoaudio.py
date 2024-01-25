from gtts import gTTS
import os

texto = input('escribe el texto a convertir : ')
tts = gTTS(text=texto,lang='es')
filename = 'hello.mp3'
tts.save(filename)
os.system(f'start {filename}')