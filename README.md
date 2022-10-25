# Sugaku
**Sugaku** is a Python module to generate a calculation chain.

# ⚠️ Functions length, oper(mode) import to make it works!

# Installation
`pip install sugaku`

# Usage
```py
import sugaku

sugaku.length = x # max_digit, 1= 1number, 2=2numbers (example sugaku.length=2 OUTPUT BETWEEN 1 TO 99   
sukagu.calength = x # calulation_length, 2= x ? y, 4= x ? y ? z ? s etc..

sugaku.oper('with') # with  :  return the calculus and its result
sugaku.oper('no-res') # no-res  :  return only the calculus
sugaku.oper('res') # res  :  return only the result

sugaku.clear() # clear all (IMPORTANT)
```

# Examples

![ex1](https://user-images.githubusercontent.com/43354103/197816684-02b0cb99-4032-4bed-89ab-7776f9e20b2d.JPG) (with mode)
### OUTPUT: 51-98+32=-15
![ex2](https://user-images.githubusercontent.com/43354103/197817112-c95db8e3-30ef-40a1-88f8-c533b9ce027f.JPG) (no-res mode)
### OUTPUT: 74/56*83
![ex3](https://user-images.githubusercontent.com/43354103/197817254-f9be704b-5b9e-46e0-8817-6f58ed982e50.JPG) (res mode)
### OUTPUT: 113

```py
import sugaku

# res mode
sugaku.length = 2
sugaku.calength = 3
sugaku.clear()

calculus = sugaku.oper('res')
calculus = sugaku.convert(calculus)

print(calculus)

# no-res mode
sugaku.length = 2
sugaku.calength = 2
sugaku.clear()

calculus = sugaku.oper('no-res')
calculus = sugaku.convert(calculus)

print(calculus)
print("-----------------------------------_")

# with mode
sugaku.length = 1
sugaku.calength = 5
sugaku.clear()

calculus = sugaku.oper('with')
calculus = sugaku.convert(calculus)

print(calculus)
```
