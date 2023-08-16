from csv import DictWriter
from json import dump

# De modo a facilitar a interpretação no projeto, não foi utilizado integração com nenhum banco de dados, e o regitros
# dos dados foi feito em duas variáveis eventosList e usuariosList. A função buscarJsonsPorPropriedade funciona como um
# select no que seria o banco de dados do projeto.
# O usuário admin possui o usuário recebendo 'admin' e senha 'admin'.
eventosList = []
usuariosList = [{
    "usuario": "admin",
    "nome": "admin da silva",
    "senha": "admin",
    "idade": "999"}]

# A variavel 'usuário' é utilizada ao longo de todas a funções para definir o usuário que está logado no momento.
usuario = ""


# ________________________________________________Funções basicas___________________________________________________
def limparConsole():
    print("\n"*50)


def buscarJsonsPorPropriedade(lista, propriedadesValores):
    resultados = []
    for jsonObj in lista:
        correspondeTodasPropriedades = True
        for propriedade, valor in propriedadesValores.items():
            # Analisa se a lista possui correspondecia de propriedade, bem como o valor da mesma
            if propriedade not in jsonObj or jsonObj[propriedade] != valor:
                correspondeTodasPropriedades = False
                break
        if correspondeTodasPropriedades:
            # Se a posição tiver correspondecia em todos os campos, ela é adiciona a lista de resultados
            resultados.append(jsonObj)
    return resultados


def imprimirEventos(eventos):
    if len(eventos) == 0:
        print("Sem resultados para a consulta!")
    else:
        indice = 0
        for evento in eventos:
            indice += 1
            print("_"*20)
            print("["+str(indice)+"]")
            print("Data: " + evento["data"])
            print("Título: " + evento["titulo"])
            print("Corpo: " + evento["corpo"])
            print("Feito: " + evento["feito"])


# Menus
def chamarMenu():
    nomeUsuario = buscarJsonsPorPropriedade(lista=usuariosList,propriedadesValores={"usuario":usuario})[0]["nome"]
    print("\n\nOla "+nomeUsuario+", qual acão você deseja realizar",
          "\n[1] Criar Evento.\n" 
          "[2] Consultar evento.\n" 
          "[3] Deletar Evento.\n" 
          "[4] Editar Evento.\n" 
          "[5] Exportar Eventos.\n"
          "[6] Editar Conta.\n"
          "[7] Sair da conta.")
    if usuario == "admin":
        print("[8] Funções de administrador.\n")
    retorno = int(input())
    limparConsole()
    if retorno == 1:
        criarEvento()
    elif retorno == 2:
        consultarEvento()
    elif retorno == 3:
        deletarEvento()
    elif retorno == 4:
        editarEvento()
    elif retorno == 5:
        exportarEvento()
    elif retorno == 6:
        AlterarConta()
    elif retorno == 7:
        chamarLobby()
    elif retorno == 8 and usuario == "admin":
        chamarMenuAdministrador()
    else:
        print("Digite uma opção valida!")
    chamarMenu()


def chamarLobby():
    retorno = int(input("[1] Login\n[2] Cadastrar-se\n"))
    if retorno == 1:
        limparConsole()
        logarUsuario()
    elif retorno == 2:
        limparConsole()
        criarUsuario()


def chamarMenuAdministrador():
    print(
        "\n\nQual acão você deseja realizar?\n[1] Deletar Usuario.\n[2] Deletar Evento.\n[3] Consultar Usuarios." +
        "\n[4] Consultar eventos.\n[5] Acessar aplicação com o contexto de outro usuario.\n[6] Sair do ambiente admin.")
    retorno = int(input())
    limparConsole()
    if retorno == 1:
        adminDeletarUsuario()
    elif retorno == 2:
        adminDeletarEvento()
    elif retorno == 3:
        adminConsultarUsuarios()
    elif retorno == 4:
        adminConsultarEventos()
    elif retorno == 5:
        adminAlterarContextoDeUsuario()
    elif retorno == 6:
        chamarMenu()
    else:
        print("Digite uma opção valida!")
        chamarMenuAdministrador()
    chamarMenuAdministrador()


# _____________________________________________________Funções de admin______________________________________________
def adminDeletarUsuario():
    indice = 0
    for usuarios in usuariosList:
        print("[" + str(indice) + "] " + str(usuarios["usuario"]))
        indice += 1
    del usuariosList[int(input("Digite o numero do usuario a ser deletado"))]
    limparConsole()
    print("Usuario deletado!\n")


def adminDeletarEvento():
    eventos = eventosList
    if len(eventos) == 0:
        print("Sem eventos para exclusão")
    else:
        imprimirEventos(eventos)
        del eventosList[eventosList.index(eventos[int(input("\n\nQual o numero do evento que deseja excluir?")) - 1])]
        limparConsole()
        print("Evento Deletado!\n")


def adminConsultarUsuarios():
    indice = 0
    for itemUsuario in usuariosList:
        indice += 1
        print("_" * 20)
        print("[" + str(indice) + "]")
        print(
            "\nUsuario: ",itemUsuario["usuario"],
            "\nNome: ",itemUsuario["nome"],
            "\nSenha: ",itemUsuario["senha"],
            "\nIdade: ",itemUsuario["idade"]
        )
    print("_"*20)


def adminAlterarContextoDeUsuario():
    global usuario
    adminConsultarUsuarios()
    usuario = usuariosList[int(input("Qual o contexto de usuario que voce deseja acessar?"))-1]["usuario"]
    limparConsole()
    chamarMenu()


def adminConsultarEventos():
    imprimirEventos(eventosList)
    print("\n")


# __________________________________________________Funções de usuário____________________________________________
def editarConta():
    global usuario
    Jsonusuario = buscarJsonsPorPropriedade(lista=usuariosList, propriedadesValores={"usuario": usuario})[0]
    indexUsuario = usuariosList.index(Jsonusuario)
    print("Apenas aperte 'Enter' caso não deseja atualizar o campo!")
    for campo,valor in Jsonusuario.items():
        if campo != "usuario":
            print(campo.upper(), " Atual:" ,valor)
            novoValor = input("Novo Valor:")
            if novoValor:
                print("atualizado")
                usuariosList[indexUsuario][campo] = novoValor
    limparConsole()
    print("Usuario atualizado!\n")


def AlterarConta():
    global usuario
    usuarioAtual = buscarJsonsPorPropriedade(lista=usuariosList, propriedadesValores={"usuario": usuario})[0]
    retorno = int(input("Qual acão você deseja realizar.\n[1] Editar Conta.\n[2] Excluir conta."))
    if retorno == 1:
        editarConta()
    elif retorno == 2:
        if input("Confirme exclusão digitando 's'\n") in ['s','S']:
            del usuariosList[usuariosList.index(usuarioAtual)]
            for evento in buscarJsonsPorPropriedade(lista=eventosList, propriedadesValores={"usuario": usuario}):
                del eventosList[eventosList.index(evento)]
            limparConsole()
            print("Conta e eventos vinculados a ela foram deletadas.")
            chamarLobby()


def logarUsuario():
    global usuario
    login = input("Usuario:")
    senha = input("Senha:")
    listaConsultaUsuarioSenha = buscarJsonsPorPropriedade(lista=usuariosList,
                                                          propriedadesValores={"usuario": login, "senha": senha})
    if len(listaConsultaUsuarioSenha) == 1:
        usuario = login
        limparConsole()
        chamarMenu()
    elif int(input("Usuario não encontrado\n[1] Tentar Novamente\n[2] Voltar ao lobby")) == 1:
        limparConsole()
        logarUsuario()
    else:
        limparConsole()
        chamarLobby()


def criarUsuario():
    global usuario
    login = input("digite o seu usuario:")
    if len(buscarJsonsPorPropriedade(lista=usuariosList, propriedadesValores={"usuario": login})) == 1:
        limparConsole()
        print("Esse usuario já está sendo utilizado,favor digitar outro nome de usuario.")
        criarUsuario()
    usuariosList.append({
        "usuario": login,
        "nome": input("digite o seu nome:"),
        "senha": input("digite a sua senha:"),
        "idade": input("digite a sua idade:")
    })
    usuario = login
    chamarMenu()


# _____________________________________________________Funções de Eventos____________________________________________
def exportarEvento():
    print("\n\nComo deseja exportar?",
          "\n[1] CSV(arquivo delimitado por ';'.\n" +
          "[2] JSON.\n" +
          "[3] Voltar\n")
    retorno = int(input())
    eventos = buscarJsonsPorPropriedade(lista=eventosList, propriedadesValores={"usuario": usuario})
    if retorno == 1:
        with open(usuario+".csv", 'w', newline='') as arquivo_csv:
            escritor_csv = DictWriter(arquivo_csv, fieldnames=set().union(*(mapa.keys() for mapa in eventos)),delimiter=";")
            escritor_csv.writeheader()
            for mapa in eventos:
                escritor_csv.writerow(mapa)
                arquivo_csv.flush()
    elif retorno == 2:
        with open(usuario+".json", 'w', newline='') as arquivo_json:
            dump(eventos, arquivo_json)
    elif retorno == 3:
        chamarMenu()
    else:
        print("Digite uma opção valida!")
        exportarEvento()


def criarEvento():
    global eventosList
    eventosList.append({
        "titulo":input("Digite o titulo do evento"),
        "data":input("Digite a data no formato dd/MM/yyyy"),
        "corpo":input("Digite o texto do evento"),
        "feito":input("Digite sim para marcar como feito e não para não feito"),
        "usuario": usuario
    })
    limparConsole()
    print("Evento criado com sucesso.")


def editarEvento():
    global usuario
    eventos = buscarJsonsPorPropriedade(lista=eventosList, propriedadesValores={"usuario": usuario})
    if len(eventos) == 0:
        limparConsole()
        print("Sem eventos para edição!\n")
    else:
        imprimirEventos(eventos)
        indexEvento = eventosList.index(eventos[int(input("\n\nQual o numero do evento que deseja editar?"))-1])
        jsonEvento = eventosList[indexEvento]
        print("Apenas aperte 'Enter' caso não deseja atualizar o campo!")
        for campo,valor in jsonEvento.items():
            if campo != "usuario":
                print(campo.upper() + " Atual:" + valor)
                novoValor = input("Novo Valor:")
                if novoValor:
                    print("atualizado")
                    eventosList[indexEvento][campo] = novoValor
        limparConsole()
        print("Evento atualizado!\nNovo valor:")
        imprimirEventos([eventosList[indexEvento]])


def consultarEvento():
    global usuario
    retorno = int(input("Qual consulta você deseja fazer?\n[1] Ver todos os eventos.\n[2] Ver eventos com um filtro especifico."))
    if retorno == 1:
        eventosUsuario = buscarJsonsPorPropriedade(lista=eventosList, propriedadesValores={"usuario": usuario})
        limparConsole()
        imprimirEventos(eventosUsuario)
    elif retorno == 2:
        limparConsole()
        consultarAvancadaEvento()


def consultarAvancadaEvento():
    global usuario

    mapAcoesFiltroAvancado = {
        "1": "titulo",
        "2": "data",
        "3": "corpo"
    }
    acao = input("Qual o campo que será utilizado para consulta:\n[1] Título.\n[2] Data.\n[3] Corpo.\n")
    limparConsole()
    valorDoCampo = input("Qual o valor que o campo precisa receber?\n")
    limparConsole()
    filtro = {
        "usuario":usuario,
        mapAcoesFiltroAvancado[acao]:valorDoCampo
    }
    imprimirEventos(buscarJsonsPorPropriedade(lista=eventosList,propriedadesValores=filtro))


def deletarEvento():
    global usuario
    eventos = buscarJsonsPorPropriedade(lista=eventosList, propriedadesValores={"usuario": usuario})
    if len(eventos) == 0:
        limparConsole()
        print("Sem eventos para exclusão")
    else:
        imprimirEventos(eventos)
        del eventosList[eventosList.index(eventos[int(input("\n\nQual o numero do evento que deseja excluir?"))-1])]
        limparConsole()
        print("Evento deletado com sucesso!")


# ________________________________________________Adição de dados para testes___________________________________________
if True:
    eventosList.append({
            "titulo":"TESTE",
            "data":"01/01/2023",
            "corpo":"teste ste ste",
            "feito":"sim",
            "usuario": "teste"
        })
    eventosList.append({
            "titulo":"TESTEADMIN",
            "data":"01/01/2023",
            "corpo":"teste ste steADMIN",
            "feito":"sim",
            "usuario": "admin"
        })
    eventosList.append({
            "titulo":"TESTEADMIN2",
            "data":"01/01/2024",
            "corpo":"teste ste steADMIN2",
            "feito": "não",
            "usuario": "admin"
        })
    usuariosList.append({
            "usuario": "teste",
            "nome": "teste da silva",
            "senha": "teste",
            "idade": "19"})
# ______________________________________________________________________________________________________________________
chamarLobby()