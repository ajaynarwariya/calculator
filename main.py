def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y
    
def multiplication(x,y):
    return x*y

def devide(x,y):
    return x/y

def modulo(x,y):
    return x%y

def floordivision(x,y):
    return x//y

def exponentiation(x,y):
    return x**y

num1 = int(input("Enter first number: " ))
num2 = int(input("Enter second number: "))
print(addition(num1,num2))
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. modulo")
print("6. floordivision")
print("7. exponentiation")
choice = int(input("Enter your choice  for operation(1,2,3,4,5,6,7): "))
match choice:
    case 1:
       print(addition(num1,num2))
    case 2:
       print(subtraction(num1,num2))
    case 3:
       print(multiplication(num1,num2))
    case 4:
       print(devide(num1,num2))
    case 5:
       print(modulo(num1,num2))
    case 6:
       print(floordivision(num1,num2))
    case 7:
       print(exponentiation(num1,num2))
    case _:
       print("you entered a Invalid Input")
