# WAP to demostarte list and tuple in python
itmes = [1,2,3,4,5,6,7]
tup_items = (1,2,3,4,5,6,7)
print("List items are:")
for item in itmes:
    print(item)

print("Tuple items are:")
for tup_item in tup_items:
    print(tup_item)
    
# WAP using a loop that loops over a sequence.

inpString = "Rohit"
print("Characters in the string are:")
for char in inpString:
    print(char)
    
# WAP using while loop that ask the user fr a number and print countdown from that number to zero.

num = int(input("Enter a number for countdown:"))

while num >= 0:
    print(num)
    num -=1
