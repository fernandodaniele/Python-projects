x = 1
while x <= 3:
    for i in range(1, 5):
        print("Iteración de for:", i)
    print("Veces que se ha utilizado el for:", x)
    x = x + 1
print("Bucles terminados")

for a in [1, 2, 3]:
    for b in [1, 2, 3, 4]:
        a = a + b
    print(a)
print("Finito")