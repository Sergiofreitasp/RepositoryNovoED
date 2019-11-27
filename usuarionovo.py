
def usuarionovo():

    username = str(input("Crie seu nome de usuário: "))

    arq = open('arquivoDeLogin.txt', 'r')
    for linha in arq:
        valor = linha.split()
        while valor[0] == username:
            print("Username ja existe! Tente Novamente!")
            username = str(input("Crie seu nome de usuário: "))

    arq.close()

    funcao = str(input("Qual a sua função? c (Coordenador), g (gestor) ou o(outra): "))
    while funcao != "c" and funcao != "g" and funcao != "o":
        print("Comando INVÁLIDO! Tente Novamente!")
        funcao = str(input("Qual a sua função? c (Coordenador), g (gestor) ou o(outra): "))

    senha = str(input("Crie sua senha: "))
    confirmasenha = str(input("Confirme sua senha: "))
    while senha != confirmasenha:
        print("Campos não correspondem! Tente Novamente!")
        senha = str(input("Crie sua senha: "))
        confirmasenha = str(input("Confirme sua senha: "))

    arq = open('arquivoDeLogin.txt', 'r')
    conteudo = arq.readlines()

    argumento = str(f"{username} {senha} {funcao} \n")

    conteudo.append(argumento)

    arq = open('arquivoDeLogin.txt', 'w')
    arq.writelines(conteudo)
    arq.close()






