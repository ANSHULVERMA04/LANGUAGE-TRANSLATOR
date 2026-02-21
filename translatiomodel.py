from transformers import MarianMTModel, MarianTokenizer
import pyttsx3 


model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


text = "Hello, how are you?"


tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
translated = model.generate(**tokens)

translation = tokenizer.decode(translated[0], skip_special_tokens=True)
print("Translated Text:", translation)


engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('voice', 'hi')  
engine.say(translation)  
engine.runAndWait()

