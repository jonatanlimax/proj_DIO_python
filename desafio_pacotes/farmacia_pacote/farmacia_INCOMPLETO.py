def exibir_menu():
    menu = """
    [1] dor de cabeça
    [2] dor de garganta
    [3] dor de estômago
    [4] sair
    """
    print()
    print("Bem-vindo à Farmácia Saramorreu!")
    print(menu)

def comprar_medicamento(categoria, catalogo):
    print(f"Você está com {categoria}? (S/N)")
    resposta = input().strip().lower()
    if resposta == "s" or resposta == "sim":
        print(f"Certo, vou te mostrar nosso catálogo para {categoria}")
        print(catalogo)
        try:
            opcao = int(input("Qual é a sua opção? "))
            if opcao in catalogo:
                medicamento = catalogo[opcao]
                preco_unitario = medicamento['preco']
                print(f"O preço unitário é de R$ {preco_unitario}")
                qtde = int(input("Quantos você deseja? "))
                preco_total = qtde * preco_unitario
                print(f"O preço total de {qtde} {medicamento['nome']} é de R$ {preco_total}")
                confirmacao = input("Deseja confirmar a compra? (S/N) ").strip().lower()
                if confirmacao == "s" or confirmacao == "sim":
                    print("Obrigado pela compra, volte sempre!")
                else:
                    print("Tudo bem, quem sabe na próxima!")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")
    else:
        print("Ok, volte sempre!")

def iniciar():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Qual é a sua opção? ").strip())
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        if opcao == 1:
            catalogo = {
                1: {'nome': 'Paracetamol', 'preco': 3},
                2: {'nome': 'Dorflex', 'preco': 4},
                3: {'nome': 'Doril', 'preco': 5},
                4: {'nome': 'Dipirona', 'preco': 1}
            }
            comprar_medicamento("dor de cabeça", catalogo)
        
        elif opcao == 2:
            catalogo = {
                1: {'nome': 'Vitamina C', 'preco': 2},
                2: {'nome': 'Nimesulida', 'preco': 5},
                3: {'nome': 'Multigripe', 'preco': 7},
                4: {'nome': 'Neosaldina', 'preco': 3}
            }
            comprar_medicamento("dor de garganta", catalogo)
        
        elif opcao == 3:
            print("Você está com dor de estômago? (S/N)")
            resposta = input().strip().lower()
            if resposta == "s" or resposta == "sim":
                print("Vou te ajudar com isso na próxima versão.")
            else:
                print("Ok, volte sempre!")

        elif opcao == 4:
            print("Você deseja sair do app Farmácia Saramorreu? (S/N)")
            resposta = input().strip().lower()
            if resposta == "s" or resposta == "sim":
                print("Obrigado por usar a Farmácia Saramorreu!")
                break
            else:
                print("Ok, vamos continuar!")

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    iniciar()
