def get_equation():
    print("enter coordinates for point 1:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("\nenter coordinates for point 2:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    if x2 - x1 == 0:
        if y2 - y1 == 0:
            print(f"P1({x1},{y1}) and P2({x2},{y2}) are the same point")
        else:
            print(f"The equation of the line is: x = {x1} (a vertical line)")
    else:
        #coeficiente angular a: representa a inclinação (delta_y / delta_x)
        a = (y2 - y1) / (x2 - x1)

        #coeficiente linear b: isolando b na fórmula y = ax + b -> b = y - ax
        b = y1 - a * x1

        if b >= 0:
            print(f"equation: y = {a:.2f}x + {b:.2f}")
        else:
            print(f"equation: y = {a:.2f}x {b:.2f}")

get_equation()
