import re 

txt=open('row.txt','r')
text=txt.read()

x=re.findall(r"ab{2,3}", text)
print(x)