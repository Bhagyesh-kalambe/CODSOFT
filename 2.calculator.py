while True:
    num1=input("enter the first value:")
    num2=input("enter the second value:")
    operator=input("enter the operator +,-,*,/,%,// : ")

    num1=int(num1)
    num2=int(num2)
    
    if operator=='+':
        print(f"result={num1+num2}")
    elif operator=='-':
        print(f"result={num1-num2}")
    elif operator=='*':
        print(f"result={num1*num2}")
    elif operator=='/':
        print(f"result={num1/num2}")
    elif operator=='%':
        print(f"result={num1%num2}")
    elif operator=='//':
        print(f"result={num1//num2}")
    else:
        print("invalid operation")
    print("Thank you")
    m=input("press q to quit:")
    if m=="q":
        break

