from sympy import symbols, Eq, solve

x, y = symbols("x y")

offset_x = 7711068
offset_y = 7874365
v_x1 = 7508165
v_y1 = 7699690
v_x2 = 7388541
v_y2 = 7814037

equation_1 = Eq((((v_x1 - offset_x)/x) + (v_y1 - offset_y)/y), -168)
equation_2 = Eq((((v_x2 - offset_x)/x) + (v_y2 - offset_y)/y), -168)


print("Equation 1:", equation_1)
print("Equation 2:", equation_2)
solution = solve((equation_1, equation_2), (x, y))
print("Solution:", solution)
print("Solution:", float(solution[0][0]), float(solution[0][1]))