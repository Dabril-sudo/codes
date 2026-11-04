#14/09
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
#=======================Boolean================================
valido = True # literalmente o botao de desligar do codigo
#Reset == False # essa idéia é interessante
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
#=================================Código==========================
while valido == True:
    if num or decimal or count_char or char or R or Q or octal or pos or pot or resultado_pot != 0: # o famoso if do reset de variavel # posso por uma unica varial (ex: reset == true pra resetar tudo)
        count_char = 0
        char = 0
        decimal = 0
        octal = 0
        Q = 0
        R = 0
        pos = 0
        pot
    if digito_hex or resultado_hex or digito_bin or resultado_bin != "": # esqueci de resetar a variavel deu F12FFFF0209DD10 na terceira conta
        num = ""
        string = ""
        digito_hex = ""
        resultado_hex = ""
        resultado_bin = ""
        digito_bin = ""
        resultado_octal = ""
        digito_octal = ""
        texto_invertido = ""
        
    print("+====================================================+")
    print("+                   Origem do Número                 +")
    print("+====================================================+")
    print("+                (1) Número Octal                    +")
    print("+                (2) Número Decimal                  +")
    print("+                (3) Número Hexadecimal              +")
    print("+                (4) Número Binário                  +")
    print("+====================================================+")

    tipo = int(input("Digite a origem do seu número para conversão (1 até 4)"  ))
    if tipo == -1:
        print ("Saindo...")
        break

    num = str(input("Digite o seu número para conversão (1 até 9999) ")).upper() # upper para estética, não sei se é necessário, mas vai que o usuário digita a-f

    print("+====================================================+")
    print("+                 Sistema de conversão               +")
    print("+====================================================+")
    print("+                (1) Número Octal                    +")
    print("+                (2) Número Decimal                  +")
    print("+                (3) Número Hexadecimal              +")
    print("+                (4) Número Binário                  +")
    print("+====================================================+")

    tipo1 = int(input(f"Selecione o sistema que queira converter o número {num} "))
    if tipo1 == -1:
        print ("saindo...")
        break

    #parte mais bonita do código é a UI

    if tipo == 1 and tipo1 == 1: #Octal pra Octal
        print(f"O número continua sendo {num}, pois é a mesma base de conversão.")
    elif tipo == 1 and tipo1 == 2: #Octal para Decimal
        for char_str in num: #não sei se pode usar len, vai assim mesmo, melhor prevenir do que remediar
            if char_str == "-": # "Não vai subir ninguem  - Capitao Nascimento contra número negativo"
                print("Saindo...")
                valido = False
                break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                char = int(char_str) # converte a string char_str para int para poder ser utilizado novamente
                if char < 0 or char > 7: #se for menor que 0 e maior que 7 vai recusar
                    print("Número tem que ser maior que zero (0) e menor que sete (7) para Octal")
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
            
        print("Valor Decimal:", decimal) # ta imprimindo o resultado 4 vezes, as duas primeiras certas depois começa a passar, uso if ou não, eis a questão
                        
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

    elif tipo == 1 and tipo1 == 4: #Octal pra Binario
        
        for char_str in num:
            char = int(char_str)
            if char < 0 or char > 7: #se for menor que 0 e maior que 7 vai recusar
                print("Número tem que ser maior que zero (0) e menor que sete (7) para Octal") # arrumar é hexadecimal
                valido = False
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
            elif char == 8:
                digito_bin = "1000"
            elif char == 9:
                digito_bin = "1001"

            resultado_bin = resultado_bin + digito_bin # eu tinha um sonho de concatenar int, não preciso dizer que deu tudo errado né
        print(resultado_bin)

    elif tipo == 2 and tipo1 == 1: #Decimal para Octal
        for char_str in num: 
            if char_str == "-": # "Não vai subir ninguem  - Capitao Nascimento contra número negativo.v2"
                print("Saindo...")
                valido = False
                break         
        char = int(char_str) # converte a string char_str para int para poder ser utilizado novamente
        count_char += 1
        if count_char > 5:
            print("Por favor, digitar apenas 5 números")
            break

        Q = int(num)
        if Q == 0:
            resultado_octal = "0"
        while Q != 0:
            R = Q % 8
            if R >= 0 and R <= 7:
                digito_octal = str(R)
                resultado_octal = digito_octal + resultado_octal
                Q = Q //8
            print("Valor Octal:", resultado_octal) # ta imprimindo o resultado 4 vezes, as duas primeiras certas depois começa a passar, uso if ou não, eis a questão
                                
    elif tipo == 2 and tipo1 == 2: #Decimal para Decimal
        print(f"O número continua sendo {num}, pois é a mesma base de conversão.")

    elif tipo == 2 and tipo1 == 3: #Decimal para Hexadecimal
        for char_str in num: 
            if char_str == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo.v3
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                char = int(char_str) # converte a string char_str para int para poder ser utilizado novamente
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
            decimal = decimal + digito * (10 ** pos)
            pos -= 1
        Q = decimal
        if Q == 0:
            resultado_hex = "0"

        while Q != 0: # para quando chegar no zerofor char_str in num: #não sei se pode usar len, vai assim mesmo, melhor prevenir do que remediar
            if char_str == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                count_char += 1 # acho que esse counter ta com b.o 19/09/2026 - Alex
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
            pos -= 1
            Q = decimal
            if Q == 0:
                resultado_hex = "0"

            while Q != 0: # para quando chegar no zero
                R = Q % 16 #antes de escrever o tabloíde de IF, que sdds da lista, index e matriz

                if R < 10: # na teoria, deve funcionar e é bom que otimiza
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
            Q = Q // 16 # tem que dividir até chegar no Q == 0, melhor do que converter pro binário (humilde opnião)
        print(resultado_hex)

    elif tipo == 2 and tipo1 == 4: #Decimal para Binario
        for char_str in num: 
            if char_str == "-": # "Não vai subir ninguem!"  - Capitao Nascimento contra número negativo.v4
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                count_char += 1
                if count_char > 5:
                    print("Por favor, digitar apenas 5 números")
                    break
        pos = count_char - 1 
        temp = int(num)
        for char_str in num:
            if pos == -1 : 
                break #eu errei no calculo dos resultado
            else:
                Q = temp
                while Q > 2: # tava > 2, entrou em um loop infinito quando foi digitado 100 # diferente de 0 resolveu
                    print (Q)
                    R = Q % 2 # é bom atualizar a variavel
                    #print(f"R:", R) #ignore o print de debug, é só pra ver se tava dando certo
                    Q = Q // 2
                    resultado_bin = str(R) + resultado_bin
        print(resultado_bin)
    
    elif tipo == 3 and tipo1 == 1: #Hexadecimal para Octal
        for char_str in num:
            if char_str == "-": # "Não vai subir ninguem!" - Capitao Nascimento contra número negativo.v4
                print("Saindo...") ## PEDE PRA SAIR RECRUTA
                valido = False
                break #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                count_char += 1
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
                elif char_str == "A" or char_str == "a":
                    digito = 10
                elif char_str == "B" or char_str == "b":
                    digito = 11
                elif char_str == "C" or char_str == "c":
                    digito = 12
                elif char_str == "D" or char_str == "d":
                    digito = 13
                elif char_str == "E" or char_str == "e":
                    digito = 14
                elif char_str == "F" or char_str == "f":
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
                break          #IMPORTANTE CITAR QUE -1 TEM QUE PARAR
            else:
                count_char += 1
                texto_invertido = char_str + texto_invertido # dahora, inverti o texto, e o resto? estaca zero de novo
                if count_char > 5:
                    print("Por favor, digitar apenas 5 números")
                    break
                for i in range(len(texto_invertido)): # esse +1 é pra não dar index out of range, mas não sei se é a melhor forma de fazer isso ## favor, opnião nesse len, se pode ou não, se não pode, me fala que eu mudo
                    char = texto_invertido[count_char] # verificar se isso é permitdo, se nao é for in texto_invertido, char_str, vai dar certo confia po
                    if char == "0":
                        digito = 0
                    elif char == "1":
                        digito = 1
                    elif char == "2":
                        digito = 2
                    elif char == "3":
                        digito = 3
                    elif char == "4":
                        digito = 4
                    elif char == "5":
                        digito = 5
                    elif char == "6":
                        digito = 6
                    elif char == "7":
                        digito = 7
                    elif char == "8":
                        digito = 8
                    elif char == "9":
                        digito = 9
                    elif char == "A":
                        digito = 10
                    elif char == "B":
                        digito = 11
                    elif char == "C":
                        digito = 12
                    elif char == "D":
                        digito = 13
                    elif char == "E":
                        digito = 14
                    elif char == "F":
                        digito = 15 
                    print(f"texto_invertido: {texto_invertido}") #debug
                    print(f"char: {char}") #debug
                    decimal = decimal + (digito * 16 ** pot)
                    pot += 1
                    if i == len(num):
                        pass
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
    
    elif tipo == 4 and tipo1 == 1: #Binario para Octal #feito ##mudei de opnião, binario é muito bom, muito facil converter com o limite de 5 digitos
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
        if len(num) >= 4:
            print("Nessa conversão, apenas 3 digitos binarios serão aceitos")
        if num == "000":
            digito_octal = 0
        elif num == "001":
            digito_octal = 1
        elif num == "010":
            digito_octal = 2
        elif num == "011":
            digito_octal = 3
        elif num == "100":
            digito_octal = 4
        elif num == "101":
            digito_octal = 5
        elif num == "110":
            digito_octal = 6
        elif num == "111":
            digito_octal = 7
        else:
            print("numero inválido, apenas 3 digitos")
        print(digito_octal)
                
    elif tipo == 4 and tipo1 == 2: #Binario para Decimal #feito
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
            if num == "0000":
                decimal = 0
            elif num == "0001":
                decimal = 1
            elif num == "0010":
                decimal = 2
            elif num == "0011":
                decimal = 3
            elif num == "0100":
                decimal = 4
            elif num == "0101":
                decimal = 5
            elif num == "0110":
                decimal = 6
            elif num == "0111":
                decimal = 7
            elif num == "1000":
                decimal = 8
            elif num == "1001":
                decimal = 9
            elif num == "1010":
                decimal = 10
            elif num == "1011":
                decimal = 11
            elif num == "1100":
                decimal = 12
            elif num == "1101":
                decimal = 13
            elif num == "1110":
                decimal = 14
            elif num == "1111":
                decimal = 15
            print(decimal)

    elif tipo == 4 and tipo1 == 3: #Binario para Hexadecimal # testar conversão, ta muito suspeito de fácil
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
        # Iinput é 4 digitos, 16 combinaçoes, ou seja, 16 fodendos IFs quero nem saber
        ## tenho cerebro pra conta mais não, agora é só por assosiação bb
        if num == "0000": # toma
            resultado_hex = "0"
        elif num == "0001": # o gigantesco tabloide da preguiça
            resultado_hex = "1"
        elif num == "0010": # eu me orgulho disso
            resultado_hex = "2"
        elif num == "0011":
            resultado_hex = "3"
        elif num == "0100":
            resultado_hex = "4"
        elif num == "0101":
            resultado_hex = "5"
        elif num == "0110":# cara, pra 0 e 1, é muito facil se perder na ordem
            resultado_hex = "6"
        elif num == "0111":
            resultado_hex = "7"
        elif num == "1000":
            resultado_hex = "8"
        elif num == "1001":
            resultado_hex = "9"
        elif num == "1010":
            resultado_hex = "A"
        elif num == "1011":
            resultado_hex = "B"
        elif num == "1100": # esses ultimos doeu a cabeça
            resultado_hex = "C"
        elif num == "1101":
            resultado_hex = "D"
        elif num == "1110":
            resultado_hex = "E"
        elif num == "1111":
            resultado_hex = "F"
        print(resultado_hex)
   
    elif tipo == 4 and tipo1 == 4: #Binario para Binario
        print(f"o numero é {num} pois é a mesma base ")


#--------------------------------------#
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
