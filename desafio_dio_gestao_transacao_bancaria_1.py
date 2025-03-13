def calcular_saldo(transacoes):
    # Calcula o saldo total somando todos os valores da lista de transações
    saldo = sum(transacoes)
    # Retorna o saldo formatado com 2 casas decimais
    return f"Saldo: R$ {saldo:.2f}"

# Solicita ao usuário que insira uma lista de transações como uma string
entrada_usuario = input()

# Converte a entrada do usuário para uma lista de números (utilizando a função eval)
# A entrada deve ser algo como: [100, -50, 200]
try:
    entradas = eval(entrada_usuario)  # A função eval converte a string para uma lista de inteiros/float
    if isinstance(entradas, list) and all(isinstance(i, (int, float)) for i in entradas):
        # Condicional para processar a lista de transações específica
        if entradas == [100, -50, 200]:
            resultado = calcular_saldo(entradas)
            print(resultado)

        elif entradas == [500, -200, -100]:
            resultado = calcular_saldo(entradas)
            print(resultado)

        elif entradas == [250, -150, -50]:
            resultado = calcular_saldo(entradas)
            print(resultado)

        else:
            # Se as transações não se encaixam nas opções acima, calcula o saldo
            resultado = calcular_saldo(entradas)
            print(resultado)
    else:
        print("Erro: A entrada não é uma lista válida de números.")
except:
    print("Erro: Formato de entrada inválido. Por favor, insira uma lista de números.")
