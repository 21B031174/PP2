import re 

txt=open('row.txt','r')
text=txt.read()

temp = text.split('_')
  
res = temp[0] + ''.join(ele.title() for ele in temp[1:])
      

print(str(res)) 