# Crie um programa que leia uma frase e mostre quantas vogais ela possui:

texto = input("Informe um texto: ")
vogais = 0
vogais_encontradas = ""
vogais_string = "aeiouAEIOU"

for letra in texto:
    if letra in vogais_string:
        vogais += 1
        vogais_encontradas += letra

print(f"O texto informado possui {vogais} vogais.")

if vogais_encontradas:
    print("As vogais encontradas são:", vogais_encontradas)
else:
    print("Nenhuma vogal encontrada."
