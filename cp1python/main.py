# Guilherme Pereira Ruiz da silva RM:573360
# Gustavo Bidin Marto RM: 570272
# Gustavo Leal RM: 569361
# Matheus Mandu de Lima RM: 571348

#Início do Sistema

print("""-----------------------
\n 𝘽𝙀𝙈-𝙑𝙄𝙉𝘿𝙊 𝘼𝙊 𝙎𝙄𝙎𝙏𝙀𝙈𝘼 𝙅𝙊𝙑𝙄.
1- Foto de anotações
2- Selfie em grupo
3- Imagem em movimento
4- Ambiente noturno
5- Foto da lousa
6- Outros
""")

#Adicionando a variável desc

desc = "Não Inserida."

#Validando a variavel opcao

opcao = int(input("Digite o número da situação: "))

if opcao <= 0 or opcao > 6:
    print("Número inválido")

else:
    if opcao == 6:
        desc = input("Descreva sua situação: ")

#Adicionando as perguntas

    print("\nAgora responda as seguintes perguntas.\n")

    dificuldade = int(input("Como você avalia a dificuldade? (1-baixa, 2-média, 3-alta): "))
    tentativas = int(input("Quantas tentativas foram necessárias: "))
    if dificuldade != 0 and tentativas != 0:
        ajuda = input("Deseja ajuda automática da câmera? (sim/não): ").lower()
        importante = input("Essa captura é importante? (sim/não): ").lower()

#Inserindo verificação de dificuldade e tentativa para prosseguir o código

        if ((ajuda == "sim" or ajuda == "s") or (ajuda == "não" or ajuda == "nao" or ajuda == "n")) and ((importante == "sim" or importante == "s") or (importante == "não" or importante == "nao" or importante == "n")) :

#Validando as possibilidades pedidas

            if ajuda == "não" or ajuda == "nao" or ajuda == "n":
                classificacao = "Modo padrãol."
                acao = "Manter a interface simples e seguir com captura comum."

            elif (ajuda == "sim" or ajuda == "s") and dificuldade == 3 and (importante == "sim" or importante == "s"):
                classificacao = "Modo inteligente prioritário."
                acao = "Ativar recomendação avançada de apoio à captura."

            elif dificuldade == 3 or tentativas >= 3:
                classificacao = "Ajuste recomendado."
                acao = "Sugerir recurso apropriado para melhorar o resultado."

            else:
                classificacao = "Captura guiada."
                acao = "Exibir orientação básica para o usuário antes da foto."

#Saída

            print(f"""\nApós analisar sua situação:
Classificação: {classificacao}
Ação: {acao}
Descrição: {desc} """)
        else:print("Resposta não aceita. Finalizando programa.")
    else:
        print("Valor inserido inválido. Finalizando programa.")