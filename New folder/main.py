user = str(input("Enter the sentence "))
 
words = user.split()

print(len(words))
    

print(words)
longest = ""
for word in words:
    if len(word)> len(longest):
        longest = word

print (" Longest word is ", longest)

num = len(words)
print (num)
if num%2==0:
    print(user, " is even")
else:
    print("odd")



