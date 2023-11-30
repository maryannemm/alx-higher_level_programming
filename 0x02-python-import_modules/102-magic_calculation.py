def magic_calculation(a, b):
    c = 0
    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

