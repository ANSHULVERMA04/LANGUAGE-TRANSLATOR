import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os


translator = Translator()
recognizer = sr.Recognizer()
mic = sr.Microphone()

def live_meeting_translation():
    with mic as source:
        print(" Listening for Hindi speech in real-time... (Press Ctrl+C to stop)")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
              
                print("🎤 Speak now...")
                audio = recognizer.listen(source, phrase_time_limit=5)

                
                hindi_text = recognizer.recognize_google(audio, language="hi-IN")
                print(f"🗣️ Hindi Speech: {hindi_text}")

               
                translated_text = translator.translate(hindi_text, src="hi", dest="en").text
                print(f"🔄 Translated (English): {translated_text}")

                
                tts = gTTS(text=translated_text, lang="en")
                tts.save("response.mp3")
                os.system("start response.mp3")  

            except sr.UnknownValueError:
                print("⚠️ Could not understand the speech.")
            except sr.RequestError:
                print("⚠️ Speech recognition API is unavailable.")
            except KeyboardInterrupt:
                print("\n🔴 Translation Stopped.")
                break


live_meeting_translation()

