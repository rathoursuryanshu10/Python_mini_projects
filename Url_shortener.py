import pyshorteners as pys
long_url=input("Enter the URL for shorten :: ")
type_tiny=pys.Shortener()
short_url=type_tiny.tinyurl.short(long_url)
print("the shorten URL is:: "+short_url)
