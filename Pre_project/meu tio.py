# try:
#     number = int(input("Digite um número inteiro: "))

#     if 0 <= number < 10:
#         print("O número está dentro da faixa desejada.")
#     else:
#         print("O número está fora da faixa desejada.")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

def exemplo_indetacao(valor):
    if valor > 10:
        print("Valor é maior que 10")
    else:
        print("O Valor é igual ou menor que 10")

exemplo_indetacao(15)