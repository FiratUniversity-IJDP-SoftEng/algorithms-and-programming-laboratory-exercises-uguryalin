# Your Student ID:230543014
# Your Name and Surname:Uğur Yalın
w = input("Please enter a text: ")
print("Character frequencies: ")
charCount = {}
for i in w:
    charCount[i] = charCount.get(i, 0) + 1
for i in sorted(charCount):
    print(f"{i}: {charCount[i]}")
