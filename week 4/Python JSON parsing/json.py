import json
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
txt=open('sample.txt', 'r')

text=txt.read()

js = json.loads(text)


for i in js['imdata']:
    print(i["l1PhysIf"]["attributes"]["dn"].ljust(42), ' '*20, i["l1PhysIf"]["attributes"]["descr"]," "*6,i["l1PhysIf"]["attributes"]["speed"],' ',i["l1PhysIf"]["attributes"]["mtu"])

