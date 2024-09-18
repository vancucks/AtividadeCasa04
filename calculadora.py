novamente= 5
while novamente == 5:
    n1 = float(input("entre com o primeiro numero: "))
    n2 = float(input("entre com o segundo numero: "))
    print("selecione a operação:\n"
                          "1 soma\n"
                          "2 subtração\n"
                          "3 multiplicação\n"
                          "4 divisão\n")
    opcao = int(input(":"))

    while opcao == 1:
        soma = n1+n2
        print(f"{n1} + {n2}: {soma}")
        opcao = opcao+5

    while opcao == 2:
        subtracao = n1-n2
        print(f"{n1} - {n2}: {subtracao}")
        opcao = opcao+5

    while opcao == 3:
        multiplicacao = n1*n2
        print(f"{n1} * {n2}: {multiplicacao}")
        opcao = opcao+5

    while opcao == 4:
        divicao = n1/n2
        print(f"{n1} / {n2}: {divicao}")
        opcao = opcao+5

    novamente = int(input("5 novo numero\n"
                      "6 sair\n"
                      ":"))


