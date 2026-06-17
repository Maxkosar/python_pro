a=input("Ingresa una palabra:")
vocales= 0

for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o"or i=="u":
        vocales+=1
print("Numeros de vocales:", vocales)
