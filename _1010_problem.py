a = input().split(' ')
b = input().split(' ')

total1 = int(a[1]) * float(a[2])
total2 = int(b[1]) * float(b[2])

total = total1 + total2
Amount = f"{total:.2f}"

print("VALOR A PAGAR: R$",Amount)