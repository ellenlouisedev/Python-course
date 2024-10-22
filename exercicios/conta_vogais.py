# Crie um programa que leia uma frase e mostre quantas vogais ela possui:

texto = input("Informe um texto: ")
vogais = 0

for letra in texto:
    if letra in "aeiou":
        vogais += 1
print(f"O texto informado possui {vogais} vogais.")

VOGAIS = "AEIOU"
print("As vogais encontradas são: ")
for letra in texto:
     if letra.upper() in VOGAIS:
        print(letra, end="")
        
else: 
    print("Nenhuma vogal encontrada.")