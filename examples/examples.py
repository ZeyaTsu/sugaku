import sugaku

# res mode
sugaku.length = 2

calculus = sugaku.oper('res')
calculus = sugaku.convert(calculus)

print(calculus)

# no-res mode
sugaku.length = 2

calculus = sugaku.oper('no-res')
calculus = sugaku.convert(calculus)

print(calculus)

# with mode
sugaku.length = 2

calculus = sugaku.oper('with')
calculus = sugaku.convert(calculus)

print(calculus)
