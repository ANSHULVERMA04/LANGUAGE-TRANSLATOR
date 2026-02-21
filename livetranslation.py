import speech_recognition as sr
from googletrans import Translator
import pyttsx3


translator = Translator()
engine = pyttsx3.init()


def translate_hindi_to_english(text):
    translated = translator.translate(text, src='hi', dest='en')
    return translated.text


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def live_meeting_translation():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print(" Listening for Hindi speech in live meeting... (Press Ctrl+C to stop)")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                
                audio = recognizer.listen(source, timeout=5)

               
                hindi_text = recognizer.recognize_google(audio, language="hi-IN")
                print(f" Hindi Speech: {hindi_text}")

                
                translated_text = translate_hindi_to_english(hindi_text)
                print(f" Translated (English): {translated_text}")

                
                speak_text(translated_text)

            except sr.UnknownValueError:
                print(" Could not understand the speech.")
            except sr.RequestError:
                print(" Speech recognition API is unavailable.")
            except KeyboardInterrupt:
                print("\n Translation Stopped.")
                break


live_meeting_translation()

