import re 

txt=open('row.txt','r')
text=txt.read()


x= re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
z=re.sub(r'([a-z0-9])([A-Z])', r'\1_\2',x).lower()
print(z)