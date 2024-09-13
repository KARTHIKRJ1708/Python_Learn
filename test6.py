name=input("Enter your name: ")
print("Your name is:",name)
length = len(name)
print("Your name length is:",length)
for i in range(length):
    for j in range(i+1):
        print(name[j],end="")
    print()