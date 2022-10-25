import sugaku

# res mode
sugaku.length = 2
sugaku.clear()

calculus = sugaku.oper('res')
calculus = sugaku.convert(calculus)

print(calculus)

# no-res mode
sugaku.length = 2
sugaku.clear()

calculus = sugaku.oper('no-res')
calculus = sugaku.convert(calculus)

print(calculus)

# with mode
sugaku.length = 2
sugaku.clear()

calculus = sugaku.oper('with')
calculus = sugaku.convert(calculus)

print(calculus)
