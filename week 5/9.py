import re 

txt=open('row.txt','r')
text=txt.read()

x=re.sub(r"(\w)([A-Z])", r"\1 \2",text)
print(x)