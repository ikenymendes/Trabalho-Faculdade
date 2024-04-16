# Bem-vindo(a) ao programa de cálculo de desconto!
print("Bem-vindo(a) à Loja do Keny!")  # Exigência de código 1 e 6

# Entrada: valor unitário e quantidade do produto
valor_unitario = float(input("Entre com o valor do produto: "))  # Exigência de código 2
quantidade = int(input("Entre com a quantidade do produto: "))  # Exigência de código 2

# Calcula o valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade  # Exigência de código 4

# Calcula o desconto com base nas condições fornecidas
if valor_total_sem_desconto < 2500:  # Exigência de código 5
    desconto = 0  # Exigência de código 5
elif 2500 <= valor_total_sem_desconto < 6000:  # Exigência de código 5
    desconto = 0.04  # Exigência de código 5
elif 6000 <= valor_total_sem_desconto < 10000:  # Exigência de código 5
    desconto = 0.07  # Exigência de código 5
else:  # Exigência de código 5
    desconto = 0.11  # Exigência de código 5

# Calcula o valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)  # Exigência de código 4

# Exibe os resultados
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}")  # Exigência de código 4
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}")  # Exigência de código 4
# Mostra o Desconto Aplicado
print(f"Desconto aplicado: {desconto * 100:.2f}%")  # Exigência de código 4
