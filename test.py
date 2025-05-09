a = 1
while a <= 30:
    b = a
    while b <= 30:
        c_squared = a * a + b * b
        c = 1
        is_perfect_square = False
        while c * c <= c_squared:
            if c * c == c_squared:
                is_perfect_square = True
                break
            c += 1

        if is_perfect_square and c <= 30:
            print(f"({a}, {b}, {c})")
        b += 1
    a += 1