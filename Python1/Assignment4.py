
def armstrong(number):
    add=0
    temp= number
    while(temp>0):
        reminder=temp%10
        add=add+(reminder*reminder*reminder)
        temp=temp//10
  

    if(add==number):
        print("it is armstrong number")
    else:
        print(" It is not the armstrong number")    

n=int(input("Enter your number to check armstrong or not ! "))   
armstrong(n)

    