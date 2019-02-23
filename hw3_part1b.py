#define function that checks if a string is reverse alphabetic
def isrevalpha(s):
    #import regular expression module
    import re
    #sub function that will remove any character that is non-alphabetic
    s = re.sub("[^a-zA-Z]+", "", s)
    #lower function to turn any uppercase characters to lower case
    s = s.lower()
    #define index, since base 0, it's 1 less than the length of the string
    index = len(s) - 1 
    #base case: empty string will return a true
    if s == "":
        return True
    #recursive case: check if second to last character is >= last character; if so, check rest of string
    else:
        if s[index-1] >= s[index]:
            return isrevalpha(s[:index])
        return False

#main routine
#while loop to coninutally run program
while True:
    #input string
    try:
        s=str(input("The string? "))
        #print output based on what the isrevalpha function returns
        if isrevalpha(s) == True:
            print(s + " is reverse alphabetic\n")
        else:
            print(s + " is not reverse alphabetic\n") 
    #exits program on any error, including EOF with CTRL D (CTRL Z on windows)
    except:
        break

