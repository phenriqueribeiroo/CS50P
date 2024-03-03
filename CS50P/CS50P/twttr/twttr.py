a = input("Input: ")
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
print("Output: ", end="")
for i in a:
    if i in vowels:
        print("", end="")
    else:
        print(i, end="")
print()
