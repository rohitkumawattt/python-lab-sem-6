import sys
#formula : sqrt((x2 - x1)^2 + (y2 - y1)^2).
# distance between two porints 
x1= int(input("enter X1 value"))
x2= int(input("enter X2 value"))
y1= int(input("enter y1 value"))
y2= int(input("enter y2 value"))
result=(((x2-x1)**2 + (y2-y1)**2)**0.5)
print("the distance between two points",(x1,x2),"and",(y1,y2),"=",result)

# Add Two Numbers Using Command Line Arguments
sys.argv = ['add.py', '10', '20']
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print("Sum =", num1 + num2)