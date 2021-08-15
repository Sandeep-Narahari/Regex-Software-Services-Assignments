str=input("Enter your String")

char_list={}
for i in range(len(str)):
    flag=0
    for j in range(len(str)):
        if(str[i]==str[j]):
            flag=flag+1
            char_list[str[i]]=flag    
print(char_list)
