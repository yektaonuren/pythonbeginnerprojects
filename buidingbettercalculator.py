num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))
op = input("enter process")

if(op=="+"):
    print(num1+num2)
elif(op=="-") :
    print(num1-num2)
elif(op=="*") :
    print(num1*num2)
elif(op=="/"):
    print(num1/num2)
else:
    print("invalid input")

