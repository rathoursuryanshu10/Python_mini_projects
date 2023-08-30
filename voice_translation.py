import googletrans
import speech_recognition 
import gtts
import playsound
input_lang="hi" #hindi
output_lang="de" #german
recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now:: ")
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language=input_lang)
    print(text)

#text="Hello"
translator = googletrans.Translator()
translation=translator.translate(text,dest=output_lang)
print(translation.text)
converted_audio=gtts.gTTS(translation.text,lang=output_lang)
converted_audio.save("test.mp3")
playsound.playsound("test.mp3")
