l=[4,6,64,6,2,43,4,3,3,5,4]
i=1
p=[]

for i in range(0,len(l)):
    flag=0
    j=i+1
    for j in range(0,i):
        if(l[i]==l[j]):
            flag=1
            break
        else:
            flag=0    
    if flag==0:
        print(l[i])


   
        

