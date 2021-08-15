hour=00
min=00
seconds=00

def secondsConverter(seconds):

#1Minute = 60 seconds
#1Hour = 60 minutes
    seconds = seconds % (24 * 3600)
    hour= seconds//3600
    seconds=seconds%3600
    min=seconds//60
    seconds= seconds%60
    return "%d:%2d:%2d" %(hour,min,seconds)

#second= int(input("Enter the seconds  "))
print(secondsConverter(3601))




