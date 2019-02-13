import urllib.request

try:
    urlname = input("Please enter the URL: ")
except EOFError:
    print("Bye!")
except:
    print("That's not a valid string. ")
else:

    try:
        webpage = urllib.request.urlopen(urlname)
    except Exception as msg:
        print("URL retrieval failed!", msg)
    else:
        s = str(webpage.read())
        print(s)