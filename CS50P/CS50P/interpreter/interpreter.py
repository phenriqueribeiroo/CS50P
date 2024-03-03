a = input("Expression: ").split(" ")
x = int(a[0])
y = a[1]
z = int(a[2])

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
