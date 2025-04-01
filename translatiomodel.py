# from transformers import MarianMTModel, MarianTokenizer
# import pyttsx3  # Import TTS library

# # Load English to Hindi model
# model_name = "Helsinki-NLP/opus-mt-en-hi"
# tokenizer = MarianTokenizer.from_pretrained(model_name)
# model = MarianMTModel.from_pretrained(model_name)

# # Input text
# text = "Hello, how are you?"

# # Tokenize and translate
# tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
# translated = model.generate(**tokens)

# # Decode translation
# translation = tokenizer.decode(translated[0], skip_special_tokens=True)
# print("Translated Text:", translation)

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)  # Speed of speech
# engine.setProperty('voice', 'hi')  # Hindi voice (if available)
# engine.say(translation)  # Speak the translated text
# engine.runAndWait()
