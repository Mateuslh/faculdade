# Desenvolva um programa em linguagem Python para cadastrar matrícula,
# nome e salário dos funcionários de uma empresa. Ao fim, o programa deve mostrar
# todos os funcionários cadastrados e, em seguida, aumentar para R$ 1.800,00 o salário
# dos funcionários com salários inferiores a R$ 1.500,00. Depois do aumento salarial, o
# programa deve exibir a nova listagem
map ={}
prints = ""
while True:
    retorno = input("Caso queira parar digite 'parar'\nDigite o nome,matricula e salario do funcionario divido por ';'").split(";")
    if retorno != ["parar"]:
        map[retorno[1]] = {
            "nome": retorno[0],
            "salario": retorno[2]
        }
    else:
        break
for key,value in map.items():
    print("Matricula: " + key + " Nome: " + value["nome"] +" salario " + value["salario"])
    map[key]["salario"] = str(1800) if float(value["salario"]) < 1500 else value["salario"]
print("\nApos alteração:\n")
for key,value in map.items():
    print("Matricula: " + key + " Nome: " + value["nome"] +" salario " + value["salario"])