def BMI(weight,height):
    bodyMassIndex=weight/(height*height)
    

    if(bodyMassIndex<18.5):
        print("Your Body Mass Index is %.2f"%(bodyMassIndex))
        print("Under Weight")
    elif(bodyMassIndex>=18.5 and bodyMassIndex<=24.9):
        print("Your Body Mass Index is %.2f"%(bodyMassIndex))
        print("Normal")
    elif(bodyMassIndex>=25 and bodyMassIndex<=29.9):
        print("Your Body Mass Index is %.2f"%(bodyMassIndex))
        print("Over Weight")   
    else:
        print("Your Body Mass Index is %.2f"%(bodyMassIndex))
        print("Obese")     

w=float(input("Enter your weight in KGS (Ex:55)  "))
h=float(input("Enter your height in METERS (Ex:1.60) "))

BMI(w,h)