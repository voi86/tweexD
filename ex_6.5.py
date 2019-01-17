text = "X-DSPAM-Confidence:    0.8475";
num = text.find(' ')

num=text[num+4:]

a=float(num)
print(a)