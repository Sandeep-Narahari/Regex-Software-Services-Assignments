d1 = {}
d2 = {}
d3 = {}
count=1
countTwo=1

while(count<5):
    name = int(input("1 st semister id: "))
    d1[name] = int(input(" 1 st semsstre marks: "))
    count=count+1
     
while(countTwo<5):
    name = int(input("2nd sem id"))
    d2[name] =int(input(" 2nd sem marks"))
    countTwo=countTwo+1

      
            
for i in range(1,count):
    d3[i]=(d1[i]+d2[i])/2
    
print(d1)
print(d2)    
print(d3)            
    

