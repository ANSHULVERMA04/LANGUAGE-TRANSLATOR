# import speech_recognition as sr
# from googletrans import Translator
# import pyttsx3

# # Initialize Translator and Speech Engine
# translator = Translator()
# engine = pyttsx3.init()

# # Function to Translate Hindi to English
# def translate_hindi_to_english(text):
#     translated = translator.translate(text, src='hi', dest='en')
#     return translated.text

# # Function to Speak Text
# def speak_text(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function for Live Translation
# def live_meeting_translation():
#     recognizer = sr.Recognizer()
#     mic = sr.Microphone()

#     with mic as source:
#         print("🔊 Listening for Hindi speech in live meeting... (Press Ctrl+C to stop)")
#         recognizer.adjust_for_ambient_noise(source)

#         while True:
#             try:
#                 # Step 1: Listen to speech continuously
#                 audio = recognizer.listen(source, timeout=5)

#                 # Step 2: Convert Speech to Hindi Text
#                 hindi_text = recognizer.recognize_google(audio, language="hi-IN")
#                 print(f"🎤 Hindi Speech: {hindi_text}")

#                 # Step 3: Translate to English
#                 translated_text = translate_hindi_to_english(hindi_text)
#                 print(f"🔄 Translated (English): {translated_text}")

#                 # Step 4: Speak Out Translated Text
#                 speak_text(translated_text)

#             except sr.UnknownValueError:
#                 print("⚠️ Could not understand the speech.")
#             except sr.RequestError:
#                 print("⚠️ Speech recognition API is unavailable.")
#             except KeyboardInterrupt:
#                 print("\n🔴 Translation Stopped.")
#                 break

# # Start Live Translation
# live_meeting_translation()
