# Crie um programa em linguagem Python que solicite ao usuário para
# digitar uma sequência de números inteiros positivos. O programa deve, em seguida,
# calcular e imprimir a soma de todos os números ímpares na sequência. Utilize lista na
# resolução do problema

print(sum([int(item) for item in input("Digite uma sequência de números inteiros positivos separados por vírgula:").split(",") if int(item) % 2 == 0]))