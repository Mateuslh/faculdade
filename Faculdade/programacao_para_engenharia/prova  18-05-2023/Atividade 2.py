# Elabore um programa que solicite ao usuário uma palavra ou frase e
# conte o número de vogais presentes nela. O programa deve exibir o número total de
# vogais e, em seguida, uma lista contendo todas as vogais encontradas, bem como o
# número de vezes que cada uma aparece na palavra ou frase.
string = input("palavra ou frase:")
map = {letra: string.count(letra) for letra in set(string) if letra in ("a","e","i","o","u")}
for key,value in map.items():
    print("letra ",key," tem ",value," repeticoes ")