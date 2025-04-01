# import speech_recognition as sr
# from googletrans import Translator
# import os

# translator = Translator()
# recognizer = sr.Recognizer()
# mic = sr.Microphone()

# # Function to Translate Text
# def translate_text(text, src_lang, dest_lang):
#     translated = translator.translate(text, src=src_lang, dest=dest_lang)
#     return translated.text

# # Function to Generate Speech in Your Voice
# def generate_speech(text):
#     os.system(f'tts --text "{text}" --model_path "output/best_model.pth" --out_path output.wav')
#     os.system("aplay output.wav")  # Play the generated voice file

# # Function for Live Translation with Your Voice Response
# def live_meeting_translation():
#     with mic as source:
#         print("🔊 Listening for Hindi speech in live meeting... (Press Ctrl+C to stop)")
#         recognizer.adjust_for_ambient_noise(source)

#         while True:
#             try:
#                 # Step 1: Listen to Hindi speech
#                 print("\n🎤 Speak in Hindi...")
#                 audio = recognizer.listen(source, timeout=5)
#                 hindi_text = recognizer.recognize_google(audio, language="hi-IN")
#                 print(f"🗣️ Hindi Speech: {hindi_text}")

#                 # Step 2: Translate to English
#                 translated_text = translate_text(hindi_text, 'hi', 'en')
#                 print(f"🔄 Translated (English): {translated_text}")

#                 # Step 3: Your Response (Listening in English)
#                 print("\n🎤 Your turn to speak in English...")
#                 audio = recognizer.listen(source, timeout=5)
#                 english_response = recognizer.recognize_google(audio, language="en")
#                 print(f"🗣️ Your Response (English): {english_response}")

#                 # Step 4: Translate Your Response Back to Hindi
#                 translated_response = translate_text(english_response, 'en', 'hi')
#                 print(f"🔄 Your Response Translated (Hindi): {translated_response}")

#                 # Step 5: Speak the Response in Your Voice
#                 generate_speech(translated_response)

#             except sr.UnknownValueError:
#                 print("⚠️ Could not understand the speech.")
#             except sr.RequestError:
#                 print("⚠️ Speech recognition API is unavailable.")
#             except KeyboardInterrupt:
#                 print("\n🔴 Translation Stopped.")
#                 break

# # Start Live Meeting Translation
# live_meeting_translation()



# needs to downloads tts 
# https://chatgpt.com/share/67dd785c-29fc-800b-8fa1-56e9ea9036cc
# https://chatgpt.com/share/67dd786f-1bfc-800b-ae9d-f4c04aaeb58f