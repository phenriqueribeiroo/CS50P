def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

letters_and_digits = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0] not in letters_and_digits[:25]:
        return False
    if s[1] not in letters_and_digits[:25]:
        return False
    for i in s:
        if i not in letters_and_digits:
            return False

main()
