# In deep.py, implement a program that prompts the user for the answer
# to the Great Question of Life, the Universe and Everything, outputting
# Yes if the user inputs 42 or (case-insensitively) forty-two or forty
# two. Otherwise output No.

x = input("What is the Answer to the Great Question of life, the Universe and Everything? ").title().strip()
if x == "42" or x == "Forty-Two" or x == "Forty Two":
    print("Yes")
else:
    print("No")
