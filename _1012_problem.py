a=input().split(' ')


triangle_area=(0.5*float(a[0])*float(a[2]))
area1=f"{triangle_area:.3f}"
print("TRIANGULO:",area1)

circle_area=(3.14159*(float(a[2])*float(a[2])))
area2=f"{circle_area:.3f}"
print("CIRCULO:",area2)

trapezium_area=(0.5*(float(a[0])+float(a[1]))*float(a[2]))
area3=f"{trapezium_area:.3f}"
print("TRAPEZIO:",area3)

square_area=(float(a[1])* float(a[1]))
area4=f"{square_area:.3f}"
print("QUADRADO:",area4)

rectangle_area=(float(a[0])*float(a[1]))
area5=f"{rectangle_area:.3f}"
print("RETANGULO:",area5)