# input
x = int(input("Digite un número"))

R = x%2
if R==0:
    msj="par"
else:
    msj="impar"

print("el numero: " + str(x) + " es: " + msj)