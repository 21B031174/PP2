import re 

txt=open('row.txt','r')
text=txt.read()
x=re.findall(r"ab*", text)
print(x)