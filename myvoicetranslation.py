import speech_recognition as sr
from googletrans import Translator
import os

translator = Translator()
recognizer = sr.Recognizer()
mic = sr.Microphone()


def translate_text(text, src_lang, dest_lang):
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text


def generate_speech(text):
    os.system(f'tts --text "{text}" --model_path "output/best_model.pth" --out_path output.wav')
    os.system("aplay output.wav")  


def live_meeting_translation():
    with mic as source:
        print(" Listening for Hindi speech in live meeting... (Press Ctrl+C to stop)")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
               
                print("\n Speak in Hindi...")
                audio = recognizer.listen(source, timeout=5)
                hindi_text = recognizer.recognize_google(audio, language="hi-IN")
                print(f" Hindi Speech: {hindi_text}")

                
                translated_text = translate_text(hindi_text, 'hi', 'en')
                print(f" Translated (English): {translated_text}")

               
                print("\n Your turn to speak in English...")
                audio = recognizer.listen(source, timeout=5)
                english_response = recognizer.recognize_google(audio, language="en")
                print(f" Your Response (English): {english_response}")

               
                translated_response = translate_text(english_response, 'en', 'hi')
                print(f" Your Response Translated (Hindi): {translated_response}")

                
                generate_speech(translated_response)

            except sr.UnknownValueError:
                print(" Could not understand the speech.")
            except sr.RequestError:
                print(" Speech recognition API is unavailable.")
            except KeyboardInterrupt:
                print("\n Translation Stopped.")
                break


live_meeting_translation()



