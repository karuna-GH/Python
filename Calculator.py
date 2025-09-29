class Calculator:

    def addition(self,num1,num2):
      print(num1+num2)
    def subtraction(self,num1,num2):
        print(num1-num2)

    def multiplication(self,num1,num2):
        print(num1*num2)

    def division(self,num1,num2):
        if num2<=0:
            raise ZeroDivisionError("Enter proper number to divide")
        else:
            print(num1 / num2)




try:

    obj = Calculator()
    while True:

        print("Enter operation you want to perform ")
        print(f" + - * / ")
        operator = input("Enter Operator : ")
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter Second number"))

        if operator == "+":
            obj.addition(num1,num2)

        elif operator == "-":
            obj.subtraction(num1,num2)

        elif operator == "*":
            obj.multiplication(num1,num2)

        elif operator == "/":
            obj.division(num1,num2)

        else:
            print("Enter proper operator")
except ValueError:
    print("Please Enter Numbers only ")
except Exception as e:
    print("Something went wrong ",e)




