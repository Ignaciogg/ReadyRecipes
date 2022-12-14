#pip install SpeechRecognition

# Importar libreria
import Descarga.SpeechRecognition as sr
import Descarga.YoutubeDownloader as yt
import os

def transcribirAudio(nombre):
    #iniciamos reconocimiento de voz
    re = sr.Recognizer()
    #conversion audio-texto
    ruta = str(yt.pathAudios)+ '\\'+nombre+'.wav'
    with sr.AudioFile(ruta) as source:
        info_audio = re.record(source)
        texto = re.recognize_google(info_audio, language="es-ES")
    try:
        os.remove(ruta)
    except:
        print("No se puede borrar audio")
    return texto