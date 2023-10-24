import pyshorteners as shr

# Take the URL From the User
url = input("Please Enter The URL: ")

# Function Uses Pyshortener Library For URL Shortening
def shorten_link(url):
    short = shr.Shortener()
    print(short.tinyurl.short(url))

# Calling the Function with the Intended URL
shorten_link(url)