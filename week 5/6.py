import re 

txt=open('row.txt','r')
text=txt.read()
text= "bhkv fanv-3.kbifkj"

x=re.sub("[\s,.]", ":", text)

print(x)