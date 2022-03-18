import re 

txt=open('row.txt','r')
text=txt.read()
#text= "bhkvfanv-3.kbifkj"


x=re.findall(r'a.*b', text)
print(x)