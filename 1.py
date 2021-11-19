quantidade_pares = 0
for numero in range(5000000):
    if numero % 2 == 0 and numero % 49 == 0 and numero % 37 == 0:
        quantidade_pares += 1 

print(quantidade_pares)