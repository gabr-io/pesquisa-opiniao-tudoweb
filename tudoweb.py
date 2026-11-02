
# Pesquisa de Opiniao - TudoWeb

# Inicializacao dos contadores
excelente = 0
bom = 0
ruim = 0

print("====================================")
print("       PESQUISA DE OPINIAO")
print("             TUDOWEB")
print("====================================")

# Repeticao para entrevistar 50 pessoas
for i in range(1, 51):

    print(f"\nEntrevistado {i} de 50")

    # Coleta dos dados
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nQual sua opiniao sobre o atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opcao: "))

    # Verificacao da opiniao
    if opiniao == 1:
        excelente += 1
        resposta = "EXCELENTE"

    elif opiniao == 2:
        bom += 1
        resposta = "BOM"

    elif opiniao == 3:
        ruim += 1
        resposta = "RUIM"

    else:
        resposta = "OPCAO INVALIDA"

    # Exibicao dos dados do entrevistado
    print("\n--- Dados do entrevistado ---")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Opiniao:", resposta)

# Resultado final da pesquisa
print("\n====================================")
print("       RESULTADO DA PESQUISA")
print("====================================")
print("Total de respostas EXCELENTE:", excelente)
print("Total de respostas BOM:", bom)
print("Total de respostas RUIM:", ruim)
print("====================================")
