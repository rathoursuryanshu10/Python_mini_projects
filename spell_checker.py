from textblob import TextBlob
def convert(string):
    li=list(string.split())
    return li
str1=input("Enter the word to check the spelling:: ")
words=convert(str1)
corrected_words=[]
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong word:: ",words)
print("Corrected words:: ",corrected_words)
for i in corrected_words:
    print(i.correct(),end=" ")

