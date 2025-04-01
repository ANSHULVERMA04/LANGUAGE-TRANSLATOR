# import speech_recognition as sr
# from googletrans import Translator
# from gtts import gTTS
# import os

# def hindi_to_english_translation():
#     recognizer = sr.Recognizer()

#     # Step 1: Capture Hindi Speech
#     with sr.Microphone() as source:
#         print("Listening for Hindi speech...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     # Step 2: Convert Speech to Text
#     try:
#         hindi_text = recognizer.recognize_google(audio, language="hi-IN")
#         print(f"Recognized Hindi Speech: {hindi_text}")
#     except sr.UnknownValueError:
#         print("Could not understand the speech.")
#         return
#     except sr.RequestError:
#         print("Speech recognition API is unavailable.")
#         return

#     # Step 3: Translate Hindi Text to English
#     translator = Translator()
#     translated_text = translator.translate(hindi_text, src="hi", dest="en").text
#     print(f"Translated Text (English): {translated_text}")

#     # Step 4: Convert Translated Text to Speech
#     tts = gTTS(text=translated_text, lang="en")
#     tts.save("translated_output.mp3")
#     os.system("start translated_output.mp3")  # Change 'start' to 'afplay' for macOS

#     print("Playing translated speech...")

# # Run the function
# hindi_to_english_translation()
