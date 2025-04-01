import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize Translator
translator = Translator()
recognizer = sr.Recognizer()
mic = sr.Microphone()

def live_meeting_translation():
    with mic as source:
        print("🔊 Listening for Hindi speech in real-time... (Press Ctrl+C to stop)")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                # Step 1: Listen to speech (Set phrase limit to 5 seconds for faster response)
                print("🎤 Speak now...")
                audio = recognizer.listen(source, phrase_time_limit=5)

                # Step 2: Convert Speech to Hindi Text
                hindi_text = recognizer.recognize_google(audio, language="hi-IN")
                print(f"🗣️ Hindi Speech: {hindi_text}")

                # Step 3: Translate to English
                translated_text = translator.translate(hindi_text, src="hi", dest="en").text
                print(f"🔄 Translated (English): {translated_text}")

                # Step 4: Convert Text to Speech & Speak Out Translation
                tts = gTTS(text=translated_text, lang="en")
                tts.save("response.mp3")
                os.system("start response.mp3")  # Play the translated speech

            except sr.UnknownValueError:
                print("⚠️ Could not understand the speech.")
            except sr.RequestError:
                print("⚠️ Speech recognition API is unavailable.")
            except KeyboardInterrupt:
                print("\n🔴 Translation Stopped.")
                break

# Start Live Translation
live_meeting_translation()
