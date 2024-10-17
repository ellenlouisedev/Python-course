x = int(input("Digite o primeiro número: "))
y = int(input("Digete o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x + y > z and x + z > x:
    print("Os números podem formar um triângulo")
    
else:
    print("Os números não podem formar um triângulo")