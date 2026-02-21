import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def hindi_to_english_translation():
    recognizer = sr.Recognizer()

 
    with sr.Microphone() as source:
        print("Listening for Hindi speech...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

   
    try:
        hindi_text = recognizer.recognize_google(audio, language="hi-IN")
        print(f"Recognized Hindi Speech: {hindi_text}")
    except sr.UnknownValueError:
        print("Could not understand the speech.")
        return
    except sr.RequestError:
        print("Speech recognition API is unavailable.")
        return

  
    translator = Translator()
    translated_text = translator.translate(hindi_text, src="hi", dest="en").text
    print(f"Translated Text (English): {translated_text}")

   
    tts = gTTS(text=translated_text, lang="en")
    tts.save("translated_output.mp3")
    os.system("start translated_output.mp3")  # Change 'start' to 'afplay' for macOS

    print("Playing translated speech...")


hindi_to_english_translation()

