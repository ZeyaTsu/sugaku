import random

debug = False

num = ["1","2","3","4","5","6", "7","8","9"]
operators = ["+","-","/","*"]

finalN = []
finalC = []

length = 1



def max_digit_length(length):
    return length

def clear():
    list.clear(finalN)
    list.clear(finalC)


def numbers(): 
    global operators
    max_len = max_digit_length(length)

    for i in range(1, max_len+1):
        n = random.choice(num)
        finalN.append(n)

    if debug == True:
        print(finalN)

    x = ''.join(finalN)
    return x


def oper(mode:str):
    numbers()
    global operators
    max_len = max_digit_length(length)


    for i in range(1, max_len+1): # Loop
        op = random.choice(operators)
        finalN.append(op) # Adding operators, calling back numbers() to get the next one.
        numbers()

    y1 = ''.join(finalN) # Final calculation in str
    y = eval(y1) # Resolve
    y = str(y)

    if mode == 'with':
        return (y1,"=",y)
    if mode == 'no-res':
        return y1
    if mode == 'res':
        return y

def convert(word): # Converting oper() to a string without ( , ) ' symbols 
    convert = ''
    for char in word:
        if char not in ('(',')', "'", ','):
            convert += char
    
    wordc = convert
    return wordc