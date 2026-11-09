#14/09
#To-Do
# verificação de input vazio
# verificação hexa se não for A-F
# verificação em outras bases para caracter incorreto
#=======================Strings===============================
num = "" # contraditório não é?, eu também to achando
string = "" # o importante é funcionar
resultado_hex = "" # resultado do hexadecimal
digito_hex = "" # str é uma mentira da sociedade ## fui concatenar e depois de 20 minutos descobri que str do built-in é um tipo especial
resultado_bin = "" # resultado do binario
digito_bin = "" # concatenação do binario, tem que ser string por causa dos 0s
resultado_octal = "" #resultado do octal
digito_octal = "" # var para auxilio nas conta, muita conta, muita váriavel e pouco neurônio
texto_invertido = "" # to criando variavel que nem sabia que teria que criar
limpo = "" #uma variavel pra limpar zero é sacanagem, mas ta valendo tudo
grupo = ""
resultado_oct = ""
#=======================Boolean================================
valido = True # literalmente o botao de desligar do codigo
#Reset == False # essa idéia é interessante
comecou = False #quero ver sobrar zero a esquerda no Octal para Bin
#=======================Int=====================================
tipo = 0 # primeira solução
tipo1 = 0 # segunda seleção
#num = 0 # numero ##importante citar que está sendo definida para str na pergunta do input, mas é int na hora de fazer a conta ###declarada duas vezes em dois tipos diferentes é sacanagem
count_char = 0 # contagem de character
char = 0 #Char de character
decimal = 0 # resposta de decimal
octal = 0 # respota para octal
Q = 0 #Quociente
R = 0 #Resto
pos = 0
pot = 0 # irmao do pos, diferente do pos, eu sei oque esse faz, serve só pra potencializar
resultado_pot = 1 #nao vou mexer no pot, nao mexe no que ta funcionando
cont_grupo = 0
#=================================Código==========================
while valido == True:
    count_char = 0
    char = 0
    decimal = 0
    octal = 0
    Q = 0
    R = 0
    pos = 0
    pot = 0
    cont_grupo = 0
    resultado_pot = 1
    comecou = False
    valido = True
    num = ""
    string = ""
    digito_hex = ""
    resultado_hex = ""
    resultado_bin = ""
    digito_bin = ""
    resultado_octal = ""
    digito_octal = ""
    texto_invertido = ""
    limpo = ""
    grupo = ""
    resultado_oct = ""
    if comecou == True:
        comecou = False
    print("+====================================================+")
    print("+                   Origem do Número                 +")
    print("+====================================================+")
    print("+                (1) Número Octal                    +")
    print("+                (2) Número Decimal                  +")
    print("+                (3) Número Hexadecimal              +")
    print("+                (4) Número Binário                  +")
    print("+====================================================+")
    print("+                (-1) Para SAIR                      +")
    print("+====================================================+")

    tipo = int(input("Digite a origem do seu número para conversão (1 até 4)"  ))
    if tipo == -1:
        print ("Saindo...")
        break

    num = str(input("Digite o seu número para conversão (1 até 9999) ")).upper() # upper para estética, não sei se é necessário, mas vai que o usuário digita a-f
    if num == "-1": # acredito que dá pra validar aqui com if tipo == 1, tipo == 2, para pegar caracteres invalidos, ficaria mais bonito e mais fácil de mexer pois fica no começo e não vou precisar de 16 CTRL C e CTRL V
        print("Saindo...")
        break

    print("+====================================================+")
    print("+                 Sistema de conversão               +")
    print("+====================================================+")
    print("+                (1) Número Octal                    +")
    print("+                (2) Número Decimal                  +")
    print("+                (3) Número Hexadecimal              +")
    print("+                (4) Número Binário                  +")
    print("+====================================================+")
    print("+                (-1) Para SAIR                      +")
    print("+====================================================+")
    
    tipo1 = int(input(f"Selecione o sistema que queira converter o número {num} "))
    if tipo1 == -1:
        print ("saindo...")
        break

    #parte mais bonita do código é a UI

    if tipo == 1 and tipo1 == 1: #Octal pra Octal
        print(f"O número continua sendo {num}, pois é a mesma base de conversão.")
    elif tipo == 1 and tipo1 == 2: #Octal para Decimal
        for char_str in num:
            if char_str < "0" or char_str > "7":
                print("Número tem que ser maior que zero (0) e menor que sete (7) para Octal")
                valido = False
                break
            count_char += 1
            if count_char > 5:
                print("Por favor, digitar apenas 5 números")
                valido = False
                break
        if valido:
            pos = count_char - 1
            for char_str in num:
                digito = int(char_str)
                decimal = decimal + digito * (8 ** pos)
                pos -= 1
            print("Valor Decimal:", decimal)

    elif tipo == 1 and tipo1 == 3: #Octal para Hexadecimal # 15/09
        for char_str in num: #não sei se pode usar len, vai assim mesmo, melhor prevenir do que remediar
            if char_str == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                char = int(char_str) # converte a string char_str para int para poder ser utilizado novamente
                if char < 0 or char > 7: #se for menor que 0 e maior que 7 vai recusar
                    print("Número tem que ser maior que zero (0) e menor que sete (7) para Octal") # arrumar é hexadecimal
                    valido = False
                else:
                    count_char += 1
                    if count_char > 5:
                        print("Por favor, digitar apenas 5 números")
                        break
        pos = count_char - 1 

        for char_str in num:
            if pos == -1 : #deu certo de alguma forma inesperada, Deus é bom ## linha 56 tava me dando AVC,
                break #eu errei no calculo dos resultado
            else:
                digito = int(char_str) # não preciso de if, elif pra cada numero
            #print(f"pos: {pos}, count_char: {count_char}") # foi pra entender o pq tava saindo 4x o resultado ## tava saindo 4x pq tava dentro do for -_-
            decimal = decimal + digito * (8 ** pos)
            pos -= 1
        Q = decimal
        if Q == 0:
            resultado_hex = "0"

        while Q != 0: # para quando chegar no zero
            R = Q % 16 #antes de escrever o tabloíde de IF, que sdds da lista, index e matriz

            if R == 0: # e se for?
                digito_hex = "0" 
            elif R == 1: # e se não for?
                digito_hex = "1"
            elif R == 2:
                digito_hex = "2"
            elif R == 3:
                digito_hex = "3"
            elif R == 4:
                digito_hex = "4"
            elif R == 5:
                digito_hex = "5"
            elif R == 6:
                digito_hex = "6"
            elif R == 7:
                digito_hex = "7"
            elif R == 8:
                digito_hex = "8"
            elif R == 9:
                digito_hex = "9"
            elif R == 10:
                digito_hex = "A"
            elif R == 11:
                digito_hex = "B"
            elif R == 12:
                digito_hex = "C"
            elif R == 13:
                digito_hex = "D"
            elif R == 14:
                digito_hex = "E"
            elif R == 15:
                digito_hex = "F" 

            resultado_hex = digito_hex + resultado_hex
            Q = Q // 16 # tem que dividir até chegar no Q == 0, melhor do que converter pro binário (humilde opnião)
        print(resultado_hex)

    elif tipo == 1 and tipo1 == 4: #Octal para Binario
        
        for char_str in num:
            char = int(char_str)
            if char < 0 or char > 7: #se for menor que 0 e maior que 7 vai recusar
                print("Número tem que ser maior que zero (0) e menor que sete (7) para Octal") # arrumar é hexadecimal
                valido = False
                break
            else:
                count_char += 1
            if count_char > 5:
                print("Por favor, digitar apenas 5 números")
                break
            if char == 0: #abomino binário do fundo do meu coração, quero o Qubit logo
                digito_bin = "000"
            elif char == 1:
                digito_bin = "001" #nesse ponto é birra do VSC
            elif char == 2:
                digito_bin = "010" #syntax error, por causa de 0 e 1, surpreendentemente faz mais sentido quando se fala em voz alta
            elif char == 3:
                digito_bin = "011" #nunca vai dar certo mesmo, como vou concatenar int?
            elif char == 4:
                digito_bin = "100"
            elif char == 5: # é incrivel que eu fiz ele separar o numero do input e tava verificando o numero inteiro do mesmo jeito
                digito_bin = "101"
            elif char == 6:
                digito_bin = "110"
            elif char == 7:
                digito_bin = "111"

            resultado_bin = resultado_bin + digito_bin # eu tinha um sonho de concatenar int, não preciso dizer que deu tudo errado né, o Ronan tava certo, sobrou 0 a esquerda mesmo
            #senhores e senhoras, mais um IF para nossa alegria
        if valido:
            limpo = ""
            comecou = False
            for bit in resultado_bin: # for para rodar a sequencia de caractere
                if bit == "1": # se tiver 1 ele começa a adicionar na variavel limpo
                    comecou = True # começou a adicionar na variavel
                if comecou: # if comecou == True:
                    limpo = limpo + bit 
            
            if limpo == "":# pra pegar o bobo na casca do ovo, vai que adiciona ""
                limpo = "0"
            print(limpo)

    elif tipo == 2 and tipo1 == 1: #Decimal para Octal
        for char_str in num:
            if char_str < "0" or char_str > "9":
                print("Número decimal só aceita dígitos de 0 a 9")
                valido = False
                break
            count_char += 1
            if count_char > 4:
                print("Por favor, digitar apenas 4 dígitos")
                valido = False
                break

        if valido:
            pos = count_char - 1
            for char_str in num:
                decimal = decimal + int(char_str) * (10 ** pos)
                pos -= 1

            if decimal < 1 or decimal > 9999:
                print("O número tem que estar entre 1 e 9999")
                valido = False

        if valido:
            Q = decimal
            while Q != 0:
                R = Q % 8
                digito_octal = str(R)
                resultado_octal = digito_octal + resultado_octal
                Q = Q // 8
            print("Valor Octal:", resultado_octal)

    elif tipo == 2 and tipo1 == 2: #Decimal para Decimal
        print(f"O número continua sendo {num}, pois é a mesma base de conversão.")

    elif tipo == 2 and tipo1 == 3: #Decimal para Hexadecimal
        for char_str in num:
            if char_str < "0" or char_str > "9":
                print("Número decimal só aceita dígitos de 0 a 9")
                valido = False
                break
            count_char += 1
            if count_char > 4:
                print("Por favor, digitar apenas 4 dígitos")
                valido = False
                break

        if valido:
            pos = count_char - 1
            for char_str in num:
                decimal = decimal + int(char_str) * (10 ** pos)
                pos -= 1

            if decimal < 1 or decimal > 9999:
                print("O número tem que estar entre 1 e 9999")
                valido = False

        if valido:
            Q = decimal
            if Q == 0:
                resultado_hex = "0"
            while Q != 0:
                R = Q % 16

                if R < 10:
                    digito_hex = str(R)
                elif R == 10:
                    digito_hex = "A"
                elif R == 11:
                    digito_hex = "B"
                elif R == 12:
                    digito_hex = "C"
                elif R == 13:
                    digito_hex = "D"
                elif R == 14:
                    digito_hex = "E"
                elif R == 15:
                    digito_hex = "F"
                resultado_hex = digito_hex + resultado_hex
                Q = Q // 16
            print(resultado_hex)

    elif tipo == 2 and tipo1 == 4:  # Decimal para Binario
        for char_str in num:
            if char_str < "0" or char_str > "9":
                print("Número decimal só aceita dígitos de 0 a 9")
                valido = False
                break
            count_char += 1
            if count_char > 4:
                print("Por favor, digitar apenas 4 dígitos")
                valido = False
                break
 # ta sem comentario, pq eu nao aguento mais refazer isso
        if valido:
            pos = count_char - 1
            for char_str in num:
                decimal = decimal + int(char_str) * (10 ** pos)
                pos -= 1

            if decimal < 1 or decimal > 9999:
                print("O número tem que estar entre 1 e 9999")
                valido = False

        if valido:
            Q = decimal
            while Q != 0:
                R = Q % 2
                Q = Q // 2
                resultado_bin = str(R) + resultado_bin
            print(resultado_bin)
    
    elif tipo == 3 and tipo1 == 1: #Hexadecimal para Octal
        for char_str in num:
            if not (("0" <= char_str <= "9") or ("A" <= char_str <= "F")):
                print("Número hexadecimal só aceita 0-9 e A-F")
                valido = False
                break
            count_char += 1
            if count_char > 5:
                print("Por favor, digitar apenas 5 caracteres")
                valido = False
                break
        for char_str in num:
            if char_str == "-": # "Não vai subir ninguem!" - Capitao Nascimento contra número negativo.v4
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                texto_invertido = char_str + texto_invertido # dahora, inverti o texto, e o resto? estaca zero de novo
                if count_char > 5:
                    print("Por favor, digitar apenas 5 números")
                    valido = False
                    break

        if valido == True:
            for char_str in texto_invertido:
                if char_str == "0":
                    digito = 0
                elif char_str == "1":
                    digito = 1
                elif char_str == "2":
                    digito = 2
                elif char_str == "3":
                    digito = 3
                elif char_str == "4":
                    digito = 4
                elif char_str == "5":
                    digito = 5
                elif char_str == "6":
                    digito = 6
                elif char_str == "7":
                    digito = 7
                elif char_str == "8":
                    digito = 8
                elif char_str == "9":
                    digito = 9
                elif char_str == "A":
                    digito = 10
                elif char_str == "B":
                    digito = 11
                elif char_str == "C":
                    digito = 12
                elif char_str == "D" :
                    digito = 13
                elif char_str == "E":
                    digito = 14
                elif char_str == "F":
                    digito = 15
                else:
                    print("Número hexadecimal inválido")
                    valido = False
                    break

                decimal += digito * resultado_pot
                resultado_pot *= 16

        # Conversão de decimal para octal, fora do FOR anterior
        if valido:
            if decimal == 0:
                resultado_octal = "0"
            else:
                resultado_octal = ""
                while decimal > 0:
                    R = decimal % 8
                    decimal = decimal // 8

                    if R == 0:
                        digito_octal = "0"
                    elif R == 1:
                        digito_octal = "1"
                    elif R == 2:
                        digito_octal = "2"
                    elif R == 3:
                        digito_octal = "3"
                    elif R == 4:
                        digito_octal = "4"
                    elif R == 5:
                        digito_octal = "5"
                    elif R == 6:
                        digito_octal = "6"
                    elif R == 7:
                        digito_octal = "7"

                    resultado_octal = digito_octal + resultado_octal

            print(resultado_octal)

    elif tipo == 3 and tipo1 == 2: #Hexadecimal para Decimal
        for char_str in num: 
            if char_str == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo.v4
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                #break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                count_char += 1
                texto_invertido = char_str + texto_invertido # dahora, inverti o texto, e o resto? estaca zero de novo
                if count_char > 5:
                    print("Por favor, digitar apenas 5 números")
                    valido = False
                    #break
               
        if valido == True:
            for char_str in texto_invertido:
                if char_str == "0":
                    digito = 0
                elif char_str == "1":
                    digito = 1
                elif char_str == "2":
                    digito = 2
                elif char_str == "3":
                    digito = 3
                elif char_str == "4":
                    digito = 4
                elif char_str == "5":
                    digito = 5
                elif char_str == "6":
                    digito = 6
                elif char_str == "7":
                    digito = 7
                elif char_str == "8":
                    digito = 8
                elif char_str == "9":
                    digito = 9
                elif char_str == "A":
                    digito = 10
                elif char_str == "B":
                    digito = 11
                elif char_str == "C":
                    digito = 12
                elif char_str == "D" :
                    digito = 13
                elif char_str == "E":
                    digito = 14
                elif char_str == "F":
                    digito = 15
                else:
                    print("Número hexadecimal inválido")
                    valido = False
                    break
                decimal += digito * resultado_pot
                resultado_pot *= 16
            if valido == True:    
                print(decimal)
            
    elif tipo == 3 and tipo1 == 3: #Hexadecimal para Hexadecimal
        print(f"O número continua sendo {num}, pois é a mesma base de conversão.")
    elif tipo == 3 and tipo1 == 4: #Hexadecimal para Binario #esse ta feito
        for char_str in num: 
            if char_str == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo.v7
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break          
            else:
                count_char += 1
            if count_char > 5:
                print("Por favor, digitar apenas 5 números")
                break
            # fazer upper em todas as outras
        # conversoes de hexadecimal pra estetica
        for string in num: #
            if string == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo.v6
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False # é pra para o código
                break # esse aqui é pra ter CERTEZA que vai parar.
            elif string == "0":
                digito_bin = "0000"
            elif string == "1":
                digito_bin = "0001"
            elif string == "2":
                digito_bin = "0010"
            elif string == "3":
                digito_bin = "0011"
            elif string == "4":
                digito_bin = "0100"
            elif string == "5":
                digito_bin = "0101"
            elif string == "6":
                digito_bin = "0110"
            elif string == "7":
                digito_bin = "0111"
            elif string == "8":
                digito_bin = "1000"
            elif string == "9":
                digito_bin = "1001"
            elif string == "A":
                digito_bin = "1010"
            elif string == "B":
                digito_bin = "1011"
            elif string == "C":
                digito_bin = "1100"
            elif string == "D":
                digito_bin = "1101"
            elif string == "E":
                digito_bin = "1110"
            elif string == "F":
                digito_bin = "1111"
            else:
                print("Digite apenas caracteres hexadecimais (0-9, A-F).")
                resultado_bin = ""
                break

            resultado_bin += digito_bin # 

        if resultado_bin:
            print(resultado_bin)
    
    elif tipo == 4 and tipo1 == 1:  # Binario para Octal
        for char_str in num:
            if char_str != "0" and char_str != "1":
                print("Número binário só aceita 0 e 1")
                valido = False
                break
            count_char += 1
            if count_char > 14:
                print("Por favor, digitar apenas 14 dígitos binários")
                valido = False
                break

        if count_char == 0:
            valido = False

        if valido:
            resto = count_char % 3
            if resto == 1:
                num_pad = "00" + num
            elif resto == 2:
                num_pad = "0" + num
            else:
                num_pad = num

            for bit in num_pad:
                grupo = grupo + bit
                cont_grupo += 1

                if cont_grupo == 3:
                    if grupo == "000":
                        digito_octal = "0"
                    elif grupo == "001":
                        digito_octal = "1"
                    elif grupo == "010":
                        digito_octal = "2"
                    elif grupo == "011":
                        digito_octal = "3"
                    elif grupo == "100":
                        digito_octal = "4"
                    elif grupo == "101":
                        digito_octal = "5"
                    elif grupo == "110":
                        digito_octal = "6"
                    elif grupo == "111":
                        digito_octal = "7"
                    resultado_oct = resultado_oct + digito_octal
                    grupo = ""
                    cont_grupo = 0

            print(resultado_oct)
                
    elif tipo == 4 and tipo1 == 2: #Binario para Decimal #feito
        
        for char_str in num:
            if char_str != "0" and char_str != "1":
                print("Número binário só aceita 0 e 1")
                valido = False
                break
            count_char += 1
            if count_char > 14:
                print("Por favor, digitar apenas 14 dígitos binários")
                valido = False
                break
        if valido:
            for bit in num:
                decimal = decimal * 2 + int(bit)
            print(decimal)

    elif tipo == 4 and tipo1 == 3:  # Binario para Hexadecimal
        for char_str in num:
            if char_str != "0" and char_str != "1":
                print("Número binário só aceita 0 e 1")
                valido = False
                break
            count_char += 1

            if count_char > 14:
                print("Por favor, digitar apenas 14 dígitos binários")
                valido = False
                break

        if count_char == 0:
            valido = False

        if valido:
            resto = count_char % 4
            if resto == 1:
                num_pad = "000" + num
            elif resto == 2:
                num_pad = "00" + num
            elif resto == 3:
                num_pad = "0" + num
            else:
                num_pad = num

            for bit in num_pad:
                grupo = grupo + bit
                cont_grupo += 1

                if cont_grupo == 4:
                    valor = 0
                    for b in grupo:
                        valor = valor * 2 + int(b)

                    if valor < 10:
                        resultado_hex = resultado_hex + str(valor)
                    elif valor == 10:
                        resultado_hex = resultado_hex + "A"
                    elif valor == 11:
                        resultado_hex = resultado_hex + "B"
                    elif valor == 12:
                        resultado_hex = resultado_hex + "C"
                    elif valor == 13:
                        resultado_hex = resultado_hex + "D"
                    elif valor == 14:
                        resultado_hex = resultado_hex + "E"
                    else:
                        resultado_hex = resultado_hex + "F"

                    grupo = ""
                    cont_grupo = 0

            print(resultado_hex) # rapaz, tudo que tinha no exercicio eu fiz errado nesse ultimo
            # derreteu meus neuronios ja


#--------------------------------------#
# resetar as variaveis no inicio de cada if seria top, talvez eu consiga ainda
# ia ficar melhor que resetar tudo em ma linha so
# é necessário um for pra verificar se tem negativo?

#==============Bloco de explicação============================

#for char_str in num: 
#           if char_str == "-":
#                print("Saindo...") 
#                valido = False # é pra quebrar o codigo
#                break          # aqui é pra ter certeza
#            else:
#                count_char += 1
#                if count_char > 5:
#                    print("Por favor, digitar apenas 5 números")
#                    break
#        pos = count_char - 1 # esse pos eu tenho que lembrar oque caralhos é, no dia que fiz tava inspirado

# é um loop usando for que, verifica cada caracter dentro de num e se algum caracter for "-" ele sai
# ele também conta quantos caracteres foram colocados na resposta, se passar de 5 ele sai
#=================================================================
