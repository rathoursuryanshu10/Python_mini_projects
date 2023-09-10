from langdetect import detect as dt
from iso639 import languages as lg
text=input("Enter the text in any language :: ")
detected_lang=dt(text)
lang_code=detected_lang
full_name=lg.get(part1=lang_code)
if full_name:
    print("Language name:: ",full_name.name)
else:
    print("Language can not be found ",text)
