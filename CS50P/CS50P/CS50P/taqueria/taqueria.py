# One of the most popular places to eat in Harvard Square is Felipe’s
# Taqueria, which offers a menu of entrees, per the dict below, wherein
# the value of each key is a price in dollars:

# In a file called taqueria.py, implement a program that enables a user
# to place an order, prompting them for items, one per line, until the
# user inputs control-d (which is a common way of ending one’s input to
# a program). After each inputted item, display the total cost of all
# items inputted thus far, prefixed with a dollar sign ($) and formatted
# to two decimal places. Treat the user’s input case insensitively.
# Ignore any input that isn’t an item. Assume that every item on the
# menu will be titlecased.

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        total = total + menu[item]
        print(f"Total: ${total:.2f}")
    except EOFError:
        break
    except KeyError:
        pass
