import re 

txt=open('row.txt','r')
text=txt.read()
#text= "dsadsa-asdas"


x=re.findall(r'[A-ZА-Я]{1}[a-zа-я]+', text)
print(x)