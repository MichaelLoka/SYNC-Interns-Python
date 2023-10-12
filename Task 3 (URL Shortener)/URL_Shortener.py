import pyshorteners as shr

url = input("Please Enter The URL: ")

def shorten_link(url):
    short = shr.Shortener()
    print(short.tinyurl.short(url))

shorten_link(url)