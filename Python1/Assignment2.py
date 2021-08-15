
def wallOneCost(lengthOne,heightOne):
    global areaOneCost
    areaOneCost=lengthOne*heightOne*120
    print("The cost of wall One is :%2d"%(areaOneCost))

def wallTwoCost(lengthTwo,heightTwo):
    global areaTwoCost
    areaTwoCost=lengthTwo*heightTwo*120
    print("The cost of wall Two is :%2d"%(areaTwoCost))

def totalCost():
    totalWallCost=areaOneCost+areaTwoCost
    print("The total cost of Wall One and Wall Two is %2d"%(totalWallCost))

lOne=int(input("Enter the Wall One length "))    
hOne=int(input("Enter the Wall one height "))
lTwo=int(input("Enter the Wall Two length "))    
hTwo=int(input("Enter the Wall Two height "))

wallOneCost(lOne,hOne)
wallTwoCost(lTwo,hTwo)
totalCost()