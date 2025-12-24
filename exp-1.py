a=35
print(type(a))
b=5+2j
print("Complex : ", b, type(b))
number=[1,2,3,4,5,"abc",2.25]
print(type(number))
tuple_number = (10,20,30,30,30)
print("Tuple:", tuple_number, type(tuple_number))
unique_values = {10,20,30,30,30}
print("Set:", unique_values, type(unique_values))
student = {"name": "rohit","age": 20,"course": "Python"}
print("Dictionary:", student, type(student))

# practice Q 
# WAP to add two number . Input should be taken from user and data type should be of integer/ float 

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3 = num1 + num2
print(num3)
# num4=float(input("Enter first number : "))
# num5=float(input("Enter second number : "))
# num6 = num4 + num5
# print(num6)
# num7=int(input("Enter first number : "))
# num8=float(input("Enter second number : "))
# num9 = num7 + num8
# print(num9)

# question 2 
# chek that the given number is even or odd.

if (num1%2 == 0):
    print("number", num1, "is even")
elif (num1%2 != 0):
    print("number", num1, "is odd")
else:
    print("input is not a number")
# question 3
# find largest among two number 

if (num1 > num2 ):
    print(num1, "is greater then ",num2)
elif (num2 > num1 ):
    print(num2, "is greater then ",num1)
else:
    print("both are equal")
# question 4
# check that the given number is prime or not 

if num1 > 1:
    for i in range (2, num1):
        if num1 % i == 0:
            print("not a prime.")
            break
        else:
            print("prime number")
            break
else:
    print("not a prime")

# question 5
# cal compound intrest and take the value from user 

p = int(input("enter the principle value for CI : "))
r = float(input("enter the rate of intrest value for CI : "))
t = int(input("enter the time for CI : "))

CI = p * (1 + ( r / 100 )) ** t
print("CI : ", CI)