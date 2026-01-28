# write a program to find the number is odd or even
num1=int(input("Enter a number to check num is odd or even : "))

if num1 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# write a program that print decimal equivalents of 1/2, 1/3.....

num = int(input("Enter a number to print decimal equivalents: "))

for i in range(2, num+1):
    print(f"1/{i} = {1/i}")