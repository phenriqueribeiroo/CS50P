# Suppose that you’re in the habit of making a list of items you need
# from the grocery store.

# In a file called grocery.py, implement a program that prompts the user
# for items, one per line, until the user inputs control-d (which is a
# common way of ending one’s input to a program). Then output the user’s
# grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that
# item. No need to pluralize the items. Treat the user’s input
# case-insensitively.

grocery = {} #Create a dictionary

while True:
    try:
        item = input().upper() #Ask for item and uppercase it
    except EOFError: #break when user inputs ctrl+d
        print()
        break
    if item in grocery:
        grocery[item] += 1 #if item already in grocery, add 1
    else:
        grocery[item] = 1 #if not, label it with 1

for item in sorted(grocery.keys()): #sorted() makes it alphabetical
    print(grocery[item], item)

#grocery.keys() are the items we inputted, sorted() makes it alphabetical

