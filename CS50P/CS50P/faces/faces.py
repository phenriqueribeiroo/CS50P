def main():
    x = input("Use emoticons to express how you're feeling: \n")
    y = convert(x)
    print(y)

def convert(x):
    y = x.replace(":)", '🙂').replace(":(", '🙁')
    return y

main()
