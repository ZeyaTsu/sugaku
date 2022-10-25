# Sugaku
**Sugaku** is a Python module to generate a calculation chain.

# ⚠️ Functions length, oper(mode) import to make it works!

# Installation
`pip install sugaku`

# Usage
```py
import sugaku

sugaku.length = 1 # max_digit_length, 1= 1number, 2=2numbers (example sugaku.length=2 OUTPUT BETWEEN 1 TO 99   

sugaku.oper('with') # OUTPUT: "calculus = result"
sugaku.oper('no-res') # OUTPUT: "calculus"
sugaku.oper('res') # OUTPUT: "result"
```

# Examples

![ex1](https://user-images.githubusercontent.com/43354103/197816684-02b0cb99-4032-4bed-89ab-7776f9e20b2d.JPG) (with mode)
### OUTPUT: 51-98+32=-15
![ex2](https://user-images.githubusercontent.com/43354103/197817112-c95db8e3-30ef-40a1-88f8-c533b9ce027f.JPG) (no-res mode)
### OUTPUT: 74/56*83
![ex3](https://user-images.githubusercontent.com/43354103/197817254-f9be704b-5b9e-46e0-8817-6f58ed982e50.JPG) (res mode)
### OUTPUT: 113
