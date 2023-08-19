from gtts import gTTS
import os
txt=open("sample.txt")
text=txt.read()
language="en"

obj=gTTS(text=text,lang=language,slow=False)
obj.save("Sample.mp3")
os.system("sample.mp3")