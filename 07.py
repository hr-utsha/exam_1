def calculator(a,b,c) : 
    if c == "add" : 
        return a + b
    elif c == "sub":
        return a - b 
    elif c == "mul" : 
        return a * b
    elif c == "div" :
        return a / b

print(calculator(5,10,"div"))
