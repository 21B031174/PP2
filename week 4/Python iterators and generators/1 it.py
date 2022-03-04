class ars():
    def __iter__(self):
        self.x=1
        return self
    
    def __next__(self):
        x=self.x
        self.x+=1
        return x*x

a=ars()
k=int(input())
p=0
for it in a:
    print(it, end = ' ')
    p+=1
    if(k==p):
        break