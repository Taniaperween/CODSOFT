def simple_calculator(num1,operation,num2):
        if operation == '+':
                result = num1+num2
        elif operation == '-':
                result = num1-num2
        elif operation == '*':
                result = num1*num2
        elif operation == '/':
                if num2!= 0:
                        result=num1/num2
                else:
                        print("error!division by zero")
        elif operation == '%':
                if num2!= 0:
                        result=num1%num2
        else:
                print("Invalid sytax")
        return result          
a = int(input("Enter the first number of your choice"))
operation=input("Enter a operation of your choice (+,-,*,/,%)")
b = int(input("Enter the second number of your choice"))
print("The result is:",simple_calculator(a,operation,b))                                                 
                                   



