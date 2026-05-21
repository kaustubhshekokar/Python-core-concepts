import math
h=int(input("tell the height of the wall:"))
w=int(input("tell the width of the wall:"))
coverage=7
def paint(h,w,coverage):
    area=h*w
    
    cans=math.ceil(area/coverage)
    
    print(f"{cans} no. of cans will be required")

paint(h,w,7)

















