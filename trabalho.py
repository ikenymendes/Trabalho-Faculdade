# Bem-vindo(a) ao programa de cálculo de desconto!
print("Bem-vindo(a) à Loja do Keny!")

# Entrada: valor unitário e quantidade do produto
valor_unitario = float(input("Entre com o valor do produto: "))
quantidade = int(input("Entre com a quantidade do produto: "))

# Calcula o valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Calcula o desconto com base nas condições fornecidas
if valor_total_sem_desconto < 2500:
    desconto = 0
elif 2500 <= valor_total_sem_desconto < 6000:
    desconto = 0.04
elif 6000 <= valor_total_sem_desconto < 10000:
    desconto = 0.07
else:
    desconto = 0.11

# Calcula o valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)

# Exibe os resultados
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")
# Mostra o Desconto Aplicado
print(f"Desconto aplicado: {desconto * 100:.2f}%")
