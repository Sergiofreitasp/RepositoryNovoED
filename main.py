
import usuarionovo
'''import usuarioativo
import outromenu
import coordenadormenu
import gestormenu'''
import reuniaolist
import sys
sistema = True
global username
import reuniao

status = "nulo"


def menu1():

    status = str(input("Você é um usuario cadastrado? Digite s(sim) ou n(não)! Digite x para sair!"))
    if status == "s":

        username = str(input("Digite seu Username: "))

        senha = str(input("Digite sua senha: "))
        arq = open('arquivoDeLogin.txt', 'r')
        for linha in arq:
            valor = linha.split()
            print(valor)

            if valor[0] == username and valor[1] == senha and valor[2] == "c":
                # menu do coordenador
                opcao = str(
                    input("Escolha uma opção - 1(criar reuniao) 2(confirmar presença) 3(vizualizar ata de reuniao)"
                          "/n 4(editar ata de reuniao) 5(baixar ata de reuniao) 6(adicionar participantes as reuniões)/n "
                          "/n 7(negar presença)"))
                if opcao == "1":
                    print("CRIAR REUNIAO")
                    tipo = str(input("Coloque o tipo de reunião publica(1) privada(2)"))
                    if tipo == "1":
                        reuniaolist.criarreuniaoPuC()
                    elif tipo == "2":
                        reuniaolist.criarreuniaoPrC()
                elif opcao == "2":
                    print("CONFIRMAR PRESENÇA")
                elif opcao == "3":
                    reuniaolist.visualizaratasCordenador()
                elif opcao == "4":
                    reuniaolist.editaratasCordenador()
                elif opcao == "5":
                    reuniaolist.salvaratareuniaoCordenador()
                elif opcao == "6":
                    print("ADICIONAR PARTICIPANTE")
                elif opcao == "7":
                    print("Negar presença")
                else:
                    menu1()


            elif valor[0] == username and valor[1] == senha and valor[2] == "g":
                # menu do gestor

                opcao = str(input("Escolha uma opção - 1(Cadastrar nova sala de reunião)"))
                if opcao == "1":
                    print("Cadastrar nova sala de reunião")
                    reuniaolist.gestoraddnovasala()
                else:
                    menu1()

            elif valor[0] == username and valor[1] == senha and valor[2] == "o":
                # Menu de usuario comum
                print(reuniaolist.reunioespublicas)
                opcao = str(input("Escolha uma opção:\n"
                                  "1(criar reuniao)\n"
                                  "2(confirmar presença)\n"
                                  "3(vizualizar ata de reuniao)\n"
                                  "4(baixar ata de reuniao)\n"
                                  "5(Adicionar participantes)\n"
                                  "6( Editar atas de reuniões do qual é o proprietário)\n"
                                  "7 (Negar presença)\n"
                                  "8 (Sair)"))
                if opcao == "1":
                    print("CRIAR REUNIAO")
                    tipo = str(input("Coloque o tipo de reunião publica(1) privada(2)"))
                    if tipo == "1":
                        reuniaolist.criarreuniaoPrO()
                    elif tipo == "2":
                        reuniaolist.criarreuniaoPrO()
                elif opcao == "2":
                    print("CONFIRMAR PRESENÇA")
                    reuniaolist.confirmarpresença()
                elif opcao == "3":
                    reuniaolist.visualizaratasOutro()
                elif opcao == "4":
                    reuniaolist.salvaratareuniaoOutro()
                elif opcao == "5":
                    print("ADICIONAR PARTICIPANTES")
                    reuniaolist.outroaddparticipantes()
                elif opcao == "6":
                    reuniaolist.editaratasOutro()
                else:
                    menu1()
            else:
                print("Usuario e senha nao correspondem! ")
            arq.close()

    elif status == "n":
        usuarionovo.usuarionovo()

    elif status == "x":
        sys.exit()

    while status != "x":
        menu1()









menu1()