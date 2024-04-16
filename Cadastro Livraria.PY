# Mensagem de boas-vindas
def mensagem_boas_vindas(nome):
    print(f"Bem-vindo à Livraria do {nome}\n")

# Função para cadastrar livro
def cadastrar_livro(id):
    livro = {}
    livro["id"] = id
    livro["nome"] = input("Por favor, entre com o nome do livro: ")
    livro["autor"] = input("Por favor, entre com o autor do livro: ")
    livro["editora"] = input("Por favor, entre com a editora do livro: ")
    print(f"\nLivro cadastrado com sucesso! ID do livro: {id}")
    lista_livros.append(livro)

# Função para consultar todos os livros
def consultar_todos():
    print("\n=== Listagem de todos os livros ===")
    if lista_livros:
        for livro in lista_livros:
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
    else:
        print("Nenhum livro cadastrado.")

# Função para consultar por ID
def consultar_por_id():
    id = int(input("\nDigite o ID do livro que deseja consultar: "))
    for livro in lista_livros:
        if livro["id"] == id:
            print("\nLivro encontrado:")
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            return
    print("Livro não encontrado.")

# Função para consultar por autor
def consultar_por_autor():
    autor = input("\nDigite o nome do autor que deseja consultar: ")
    print(f"\nLivros do autor {autor}:")
    for livro in lista_livros:
        if livro["autor"].lower() == autor.lower():
            print(f"ID: {livro['id']}, Nome: {livro['nome']}, Editora: {livro['editora']}")
    if not any(livro["autor"].lower() == autor.lower() for livro in lista_livros):
        print("Nenhum livro encontrado para este autor.")

# Função para remover livro
def remover_livro():
    id = int(input("\nDigite o ID do livro que deseja remover: "))
    for livro in lista_livros:
        if livro["id"] == id:
            lista_livros.remove(livro)
            print("Livro removido com sucesso.")
            return
    print("ID inválido. Livro não encontrado.")

# Função principal
def main():
    nome = "Bruno Kostiuk"  # Seu nome
    mensagem_boas_vindas(nome)

    global id_global
    id_global = 0

    # Loop principal
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Livro")
        print("2 - Consultar Livro(s)")
        print("3 - Remover Livro")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            id_global += 1
            print(f"\nID do livro: {id_global}")
            cadastrar_livro(id_global)
        elif opcao == "2":
            while True:
                print("\n=== MENU CONSULTAR LIVRO(S) ===")
                print("Escolha a opção desejada:")
                print("1 - Consultar Todos")
                print("2 - Consultar por ID")
                print("3 - Consultar por Autor")
                print("4 - Retornar ao menu")

                consulta_opcao = input("Opção: ")

                if consulta_opcao == "1":
                    consultar_todos()
                elif consulta_opcao == "2":
                    consultar_por_id()
                elif consulta_opcao == "3":
                    consultar_por_autor()
                elif consulta_opcao == "4":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Lista de livros
lista_livros = []

# Chamada da função principal
if __name__ == "__main__":
    main()
