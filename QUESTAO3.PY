# Função para escolha do serviço
def escolha_servico():
    while True:
        print("Entre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        service = input(">>").lower()
        if service in ["dig", "ico", "ipb", "fot"]:
            # Retorna o valor do serviço com base na escolha do usuário
            if service == "dig":
                return 1.10
            elif service == "ico":
                return 1.00
            elif service == "ipb":
                return 0.40
            elif service == "fot":
                return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")

# Função para escolha do número de páginas com desconto
def num_paginas():
    while True:
        try:
            print("Entre com o número de páginas:")
            num_pages = int(input(">>"))
            if num_pages < 20:
                return num_pages
            elif 20 <= num_pages < 200:
                return num_pages * 0.85
            elif 200 <= num_pages < 2000:
                return num_pages * 0.80
            elif 2000 <= num_pages < 20000:
                return num_pages * 0.75
            else:
                print("Não aceitamos tantas paginas de ua vez.")
        except ValueError:
            print("Número de páginas inválido. Por favor, entre com um número inteiro.")

# Função para escolha do serviço adicional
def servico_extra():
    extra_cost = 0
    while True:
        print("Deseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        option = input(">>")
        if option == "1":
            extra_cost += 15.00
            return extra_cost
        elif option == "2":
            extra_cost += 40.00
            return extra_cost
        elif option == "0":
            return extra_cost
        else:
            print("Opção inválida. Por favor, escolha novamente.")

# Função principal
def main():
    # Mensagem de boas-vindas
    print("Bem vindo a Copiadora do Keny")
    
    # Escolha do serviço
    servico = escolha_servico()
    
    # Escolha do número de páginas
    num_pag = num_paginas()
    
    # Serviço adicional
    extra = servico_extra()
    
    # Cálculo do total
    total = (servico * num_pag) + extra
    
    # Impressão do total
    print(f"Total: R$ {total:.2f} (serviço: {servico} * páginas: {num_pag} + extra: {extra:.2f})")

if __name__ == "__main__":
    main()
