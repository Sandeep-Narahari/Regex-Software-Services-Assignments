l=[]
rows=5
for x in range(2,50):
    count=0
    for y in range(2,x):
        if((x%y)==0):
            count=count+1
            break
                
           
    if(count==0):
        l.append(x)


s=9
count=0
for i in range(0,rows):
    for j in range(0,s):
        print(end=" ")
    s=s-1

    for j in range(0,i+1):
        count=count+1
        if(j!=0):
            print(l[count-1],end=" ")
        else:
            print(l[count-1], end=" ")
    print("\n")                



        


        