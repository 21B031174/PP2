import re 

txt=open('row.txt','r')
text=txt.read()

x=re.findall("[A-Z][^A-Z]*",text)
print(x)