
"""
def list():
    lists = [1, 8, 3, 4]
    print(max(lists))


list()

"""
# Write a function to find a largest number in list.

def largest(num):
   
    print(max(num))


print(largest([1,53,8,3]))

# Write a Python program to find the sum of all even numbers from 1 to 100.
"""
First write a program which will give all even number
second sum up all
 
"""
b = 0
list = []
while b<100:
    b += 2
    list.append(b)

print(list)
print(sum(list))


# Generate the first N Fibonacci numbers, where N is input by the user.
"""
0, 1,1,2,3,5,8,13.21
start with 0
+ 1 = value
+ 1 = value which become next 2 
+ 2 = value become 3

in order to that
i need to take input and add that input on next value

value 
store value 
new value
value + stored value = store value

value 
new value + old value 

"""

# Number of Fibonacci numbers to generate
N = 10

a,b = 0,1

for _ in range(10):
    print(a, end =" ")
    a,b = b, b+a














    
    


    
    
    
