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
        count=1
        for i in webpage.readlines():
            print("%5d " % count, i)
            count += 1