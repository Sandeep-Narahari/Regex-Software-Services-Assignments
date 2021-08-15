d1={"a":1,"b":2,"c":3,"d":4}
d2={"b":2,"d":4,"f":6,"g":7}
d3={}

def disJoint():
    union=dict(d1.items() | d2.items())
    intersection=dict(d1.items() & d2.items())
    d3=dict(union.items() ^ intersection.items())
    return d3


print(disJoint())        