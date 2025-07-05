print("Bem vindo a Livraria do Davi Silva")

# Lista para armazenar os livros cadastrados
lista_livro = []
# Variável global para controlar o id dos livros
id_global = 0

# Função para cadastrar livro
def cadastrar_livro(id):
    print("---------------------------------------------------")
    print("--------------- MENU CADASTRAR LIVRO --------------")
    print(f"Id do livro: {id}")
    # Solicita os dados do livro ao usuário
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    # Cria um dicionário com os dados do livro
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    # Adiciona o livro à lista de livros
    lista_livro.append(livro)

# Função para consultar livros
def consultar_livro():
    while True:
        print("---------------------------------------------------")
        print("--------------- MENU CONSULTAR LIVRO --------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar")
        try:
            # Solicita a opção de consulta ao usuário
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida.")
            continue
        # Consulta todos os livros cadastrados
        if opcao == 1:
            for livro in lista_livro:
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                print("---------------")
        # Consulta livro por id
        elif opcao == 2:
            try:
                id_consulta = int(input("Digite o id do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_consulta:
                        print(f"id: {livro['id']}")
                        print(f"nome: {livro['nome']}")
                        print(f"autor: {livro['autor']}")
                        print(f"editora: {livro['editora']}")
                        print("---------------")
                        encontrado = True
                if not encontrado:
                    print("Livro não encontrado.")
            except ValueError:
                print("Id inválido.")
        # Consulta livros por autor
        elif opcao == 3:
            autor_consulta = input("Digite o autor do(s) livro(s): ")
            encontrado = False
            for livro in lista_livro:
                # Compara ignorando maiúsculas/minúsculas
                if livro['autor'].lower() == autor_consulta.lower():
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    print("---------------")
                    encontrado = True
            if not encontrado:
                print("Nenhum livro encontrado para esse autor.")
        # Retorna ao menu principal
        elif opcao == 4:
            break
        # Opção inválida no menu de consulta
        else:
            print("Opção inválida.")

# Função para remover livro
def remover_livro():
    while True:
        try:
            # Solicita o id do livro a ser removido
            id_remove = int(input("Digite o id do livro a ser removido: "))
            for livro in lista_livro:
                if livro['id'] == id_remove:
                    # Remove o livro da lista
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            # Se não encontrar o id, exibe mensagem de erro
            print("Id inválido")
        except ValueError:
            print("Id inválido")

# Menu principal do sistema
while True:
    print("---------------------------------------------------")
    print("--------------- MENU PRINCIPAL --------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    try:
        # Solicita a opção do menu principal ao usuário
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida.")
        continue
    # Chama a função de cadastro de livro
    if opcao == 1:
        id_global += 1
        cadastrar_livro(id_global)
    # Chama a função de consulta de livros
    elif opcao == 2:
        consultar_livro()
    # Chama a função de remoção de livro
    elif opcao == 3:
        remover_livro()
    # Encerra o programa
    elif opcao == 4:
        print("Encerrando o programa...")
        break
    # Opção inválida no menu principal
    else:
        print("Opção inválida.")
print("Bem vindo a Livraria do Davi Silva")

# Lista para armazenar os livros cadastrados
lista_livro = []
# Variável global para controlar o id dos livros
id_global = 0

# Função para cadastrar livro
def cadastrar_livro(id):
    print("---------------------------------------------------")
    print("--------------- MENU CADASTRAR LIVRO --------------")
    print(f"Id do livro: {id}")
    # Solicita os dados do livro ao usuário
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    # Cria um dicionário com os dados do livro
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    # Adiciona o livro à lista de livros
    lista_livro.append(livro)

# Função para consultar livros
def consultar_livro():
    while True:
        print("---------------------------------------------------")
        print("--------------- MENU CONSULTAR LIVRO --------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar")
        try:
            # Solicita a opção de consulta ao usuário
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida.")
            continue
        # Consulta todos os livros cadastrados
        if opcao == 1:
            for livro in lista_livro:
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                print("---------------")
        # Consulta livro por id
        elif opcao == 2:
            try:
                id_consulta = int(input("Digite o id do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_consulta:
                        print(f"id: {livro['id']}")
                        print(f"nome: {livro['nome']}")
                        print(f"autor: {livro['autor']}")
                        print(f"editora: {livro['editora']}")
                        print("---------------")
                        encontrado = True
                if not encontrado:
                    print("Livro não encontrado.")
            except ValueError:
                print("Id inválido.")
        # Consulta livros por autor
        elif opcao == 3:
            autor_consulta = input("Digite o autor do(s) livro(s): ")
            encontrado = False
            for livro in lista_livro:
                # Compara ignorando maiúsculas/minúsculas
                if livro['autor'].lower() == autor_consulta.lower():
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    print("---------------")
                    encontrado = True
            if not encontrado:
                print("Nenhum livro encontrado para esse autor.")
        # Retorna ao menu principal
        elif opcao == 4:
            break
        # Opção inválida no menu de consulta
        else:
            print("Opção inválida.")

# Função para remover livro
def remover_livro():
    while True:
        try:
            # Solicita o id do livro a ser removido
            id_remove = int(input("Digite o id do livro a ser removido: "))
            for livro in lista_livro:
                if livro['id'] == id_remove:
                    # Remove o livro da lista
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            # Se não encontrar o id, exibe mensagem de erro
            print("Id inválido")
        except ValueError:
            print("Id inválido")

# Menu principal do sistema
while True:
    print("---------------------------------------------------")
    print("--------------- MENU PRINCIPAL --------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    try:
        # Solicita a opção do menu principal ao usuário
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida.")
        continue
    # Chama a função de cadastro de livro
    if opcao == 1:
        id_global += 1
        cadastrar_livro(id_global)
    # Chama a função de consulta de livros
    elif opcao == 2:
        consultar_livro()
    # Chama a função de remoção de livro
    elif opcao == 3:
        remover_livro()
    # Encerra o programa
    elif opcao == 4:
        print("Encerrando o programa...")
        break
    # Opção inválida no menu principal
    else:
        print("Opção inválida.")
