xs = eval(input("Enter the x: "))
ys = eval(input("Enter the y: "))
b = []

print("Lagrange")
print()
print("Results:")
print()
print("Interpolating polynomials:")
print()
expression = ""
result = 1
polim = "*"
for i in xs:
    for k in xs:
        if xs.index(i) != xs.index(k): 
            polim += (f"(x - {k})*")
            result *= i - k  
    polim = polim[0:len(polim)-1]
    print(polim[1:])
    result = 1/result
    result = ys[xs.index(i)]*result
    b.append(result)
    expression += "("+str(result)+polim+")"+"+"
    polim = "*"
    result = 1
expression = expression[0:len(expression)-1]

print()
print("Polynomial coefficients:")
print()
for i in b:
    print(i)
print()
print("Polynomial:")
print()
print(expression) 