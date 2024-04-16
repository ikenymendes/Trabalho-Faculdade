# Mensagem de boas-vindas com o nome
print("Bem-vindo à Loja de Gelados do Keny Mendes!\n")

# Cardápio com preços dos gelados
print("=== Cardápio ===")
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---")
print("---| P | R$ 9.00 | R$ 11.00 |---")
print("---| M | R$ 14.00 | R$ 16.00 |---")
print("---| G | R$ 18.00 | R$ 20.00 |---\n")

# Inicialização do acumulador para somar os valores dos pedidos
total_pedido = 0

while True:  # Inicia um loop infinito para permitir vários pedidos
    # Input do sabor (CP/AC)
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper()

    # Verifica se o sabor é válido
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue  # Reinicia o loop para um novo pedido

    # Input do tamanho (P/M/G)
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()

    # Verifica se o tamanho é válido
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue  # Reinicia o loop para um novo pedido

    # Calcula o preço com base no sabor e tamanho escolhidos
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        else:
            preco = 18
    else:  # Sabor é AC
        if tamanho == 'P':
            preco = 11
        elif tamanho == 'M':
            preco = 16
        else:
            preco = 20

    # Exibe o pedido confirmado
    print(f"Você pediu um {'Cupuaçu' if sabor == 'CP' else 'Açaí'} no tamanho {tamanho}: R$ {preco:.2f}\n")

    # Adiciona o preço do pedido ao total
    total_pedido += preco

    # Pergunta se o usuário deseja pedir mais alguma coisa
    continuar = input("Deseja mais alguma coisa? (S/N): ").upper()

    # Verifica se o usuário deseja continuar
    if continuar != 'S':
        break  # Sai do loop se o usuário não quiser mais pedir

# Exibe o total do pedido
print(f"\nO valor total a ser pago: R$ {total_pedido:.2f}")
