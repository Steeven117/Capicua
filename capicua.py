#NUMEROS CAPICUA DE 5 TERMINOS

print("-----------------------------------------------")
print("----------------BIENVENIDO---------------------")
print("-----------------------------------------------")

#INPUT

a=int(input("Digite el primer valor: "))
b=int(input("Digite el segundo valor: "))
c=int(input("Digite el tercer valor: "))
d=int(input("Digite el cuarto valor: "))
e=int(input("Digitre el ultimo digito: "))

#PROCESSING

if e==a:
    if d==b:
        if c==c:
            rta="El numero es capicua"
        else:
            rta="El numero no es capicua"
    else:
        rta="El numero no es capicua"
else:
    rta="El numero no es capicua"

#OUTPUT

print(rta)