# try:
#     number = int(input("Digite um número inteiro: "))

#     if 0 <= number < 10:
#         print("O número está dentro da faixa desejada.")
#     else:
#         print("O número está fora da faixa desejada.")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# def exemplo_indetacao(valor):
#     if valor > 10:
#         print("Valor é maior que 10")
#     else:
#         print("O Valor é igual ou menor que 10")

# exemplo_indetacao(15)

# Exemplo de valores Falsy em Python
falsy_values = [False, None, 0, 0.0, '', [], {}]

# Exemplo de valores Truthy em Python
truthy_values = [True, 1, 3.14, 'texto', [1, 2, 3], {'chave': 'valor'}]

# Função para verificar se um valor é Truthy ou Falsy
def verificar_truthy_falsy(valor):
    if valor:
        print(f'O valor {repr(valor)} é Truthy.')
    else:
        print(f'O valor {repr(valor)} é Falsy.')

# Testando os valores Falsy
print("Valores Falsy:")
for valor in falsy_values:
    verificar_truthy_falsy(valor)

# Testando os valores Truthy
print("\nValores Truthy:")
for valor in truthy_values:
    verificar_truthy_falsy(valor)