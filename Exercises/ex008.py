# Your Student ID:230543014
# Your Name and Surname:Uğur Yalın
number = (int)(input("Enter a number: "))
for i in range(number):
    for j in range(number - i - 1):        
        print(" ",end="")
    for j in range(2*i + 1):
        print("*",end="")
    print()
