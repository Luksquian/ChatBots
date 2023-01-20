import speech_recognition as sr
import openai
from gtts import gTTS
from pygame import mixer
import os
import time as ti
import random


openai.api_key = "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"

def transformar_audio_a_texto():

    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Ya puedes hablar!")
        audio = r.listen(origen)
        try:
            pedido = r.recognize_google(audio, language="es-AR")
            print("You: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("Ups, no entendi!")
            return "Sigo esperando"

        except sr.RequestError:
            print("Ups, no hay servicio!")
            return "Sigo esperando"

        except:
            print("Ups, algo salio mal!")
            return "Sigo esperando"

def hablar(mensaje):
    volume = 0.7
    tts = gTTS(mensaje, lang="es", slow=False)
    ran = random.randint(0,9999)
    filename = 'Temp' + format(ran) + '.mp3'
    tts.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(volume)
    mixer.music.play()

    while mixer.music.get_busy():
        ti.sleep(0.3)

    mixer.quit()
    os.remove(filename)


def main():
    conversation = "Vicky es un chatbot que responde de mala gana y responde a todo con sarcasmo!\n\nYou: Cual es el sentido de la vida?\nVicky: No lo se pero puedes preguntarle a google!\nYou: ¿Qué significa HTML?\nVicky: ¿Google estaba demasiado ocupado? Lenguaje de marcado de hipertexto. La T es para tratar de hacer mejores preguntas en el futuro."

    hablar("Hola! Soy Vicky tu asistente personal, ¿en que puedo ayudarte?")

    while True:
        question = transformar_audio_a_texto().lower()

        conversation += "\nYou: " + question + "\nVicky:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.5,
            max_tokens=100,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["\n", " You:", " Vicky:"]
        )
        answer = response.choices[0].text.strip()
        conversation += answer
        print("Vicky: " + answer + "\n")
        hablar(answer)


main()









