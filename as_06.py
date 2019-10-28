text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('0')
#epos=text.find('',pos)
num=text[pos:]
value=float(num)
print(value)
