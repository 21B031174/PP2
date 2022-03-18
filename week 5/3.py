import re 

txt=open('row.txt','r')
text=txt.read()
#text= "dsadsa-asdas"


x=re.findall(r'^[a-z]+-[a-z]+$', text)
print(x)