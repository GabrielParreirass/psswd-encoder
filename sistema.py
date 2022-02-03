from configparser import Error
import mysql.connector
import time
import random





# LIGAÇÃO COM O BANCO DE DADOS 

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastros_logins"
)

cursor = banco.cursor()

comando_sql = "INSERT INTO cadastros (usuario, senha, id) VALUES (%s, %s, %s)"

print(banco)

#-

# FUNÇÕES 

def main():
    # DIRECIONA PARA AS OUTRA FUNÇÕES.
    print('')
    print('\033[1;34mPagina principal\033[m')
    print('-'*100)
    while True:
        x = str(input('Você ja possui cadastro? (s/n):'))
        x = x.lower()
        if x == 's':
            login()
            break
        elif x == 'n':
            cadastro() 
            break
        else:
            print('\033[31mDIGITE UMA OPÇÃO VALIDA!\033[m')
            time.sleep(1)
#-

def login():
    # FAZ O LOGIN CHECANDO OS DADOS NO BANCO.
    print('\033[1;34mBem vindo a pagina de login\033[m')
    print('')


    while True:

        confirma_usuario = ''
        while confirma_usuario == '':
            confirma_usuario = str(input('\033[1;33mEscreva seu nome de usuario: \033[m'))
            if not confirma_usuario:
                print('\033[31mESTE CAMPO PRECISA SER PREENCHIDO!\033[m')
                time.sleep(1)
            else:
                pass

        confirma_senha = ''
        while confirma_senha == '':
            confirma_senha = str(input('\033[1;33mEscreva sua senha: \033[m'))
            if not confirma_senha:
                print('\033[31mESTE CAMPO PRECISA SER PREENCHIDO!\033[m')
                time.sleep(1)
            else:
                pass

        comando_sql = f"SELECT * FROM cadastros WHERE usuario = '{confirma_usuario}' AND senha = '{confirma_senha}'"

        cursor.execute(comando_sql)

        valor = cursor.fetchall()

        if valor == []:
            print('\033[31mUSUARIO OU SENHA INCORRETOS!\033[m')
            print('-'*100)
        else:
            print('\033[32mLOGIN REALIZADO COM SUCESSO!\033[m')
            print('-'*100)
            print(f'VOCÊ ESTA LOGADO COMO {confirma_usuario}!')
            programa(confirma_usuario)
            break
            

def cadastro():
    # REGISTRAR O CADASTRO NO BANCO DE DADOS.
        print('')
        print('-'*100)
        print('\033[1;36mBEM VINDO A PAGINA DE CADASTRO! PREENCHA OS CAMPOS ABAIXO PARA PODERMOS FAZER SEU REGISTRO!\033[m')
        print('')

        usuario = ''
        while usuario == '':
            usuario = str(input('Escreva seu nome de usuario: ')).lower()
            if not usuario:
                print('\033[31mESTE CAMPO PRECISA SER PREENCHIDO!\033[m')
            else:
                pass

        senha = ''   
        while senha == '':
            senha = str(input('Escreva sua senha: '))
            if not senha:
                print('\033[31mESTE CAMPO PRECISA SER PREENCHIDO!\033[m')
            else:
                pass

        id = random.randint(1, 999)

        

        verificar(usuario,senha,id)


def verificar(usuario, senha, id):
        comando = 'SELECT usuario FROM cadastros'
        cursor.execute(comando)
        x = cursor.fetchall()

        c = 0

        usuario_formatado = (f'{usuario}',)

        for i in x:

            if usuario_formatado == i:
                c = 1
                break
                
            elif usuario_formatado != i:
                c = 2
                continue

        if c == 2:
            dados = usuario, senha, id
            cursor.execute(comando_sql, dados)
            print('-'*100)
            print('\033[32mUSUARIO CADASTRADO COM SUCESSO\033[m')
            print('-'*100)
            login()
        elif c == 1:
            print('-'*100)
            print('\033[31mESSE USUARIO JA EXISTE, VOLTANDO PARA O CADASRTO!\033[m')
            cadastro()
              

def codificador(strS, plataforma, idf, usuario):
    x = (strS)
    x2 = len(x)
    c = 0
    y = 1
    x3 = list('')
    while c != x2:
        letra = (x[x2-y])
        y += 1
        c += 1
        x3.append(letra)
        
    senha = (list(reversed(x3)))
    x3 = len(senha)

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','@','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ','a']
    
    c2 = 0
    y2 = 1
    while c2 != x3:
        id = senha[0 + c2]
        index = alfabeto.index(id)
        senha[0 + c2] = alfabeto[index + 1]
        c2 += 1
    

    strS2 = "".join(senha)
    

    v1 = str(plataforma)
    v2 = str(strS2)
    v3 = str(idf)

    dados2 = (v1, v2, v3)

    veri_dados = f"SELECT plataforma FROM `senhas` WHERE id = {idf}"

    cursor.execute(veri_dados)

    lista = cursor.fetchall()

    if (f'{plataforma}',) in lista:
        print('')
        print('\033[1;33mJA EXISTE UMA SENHA CADASTRADA PARA ESSA PLATAFORMA!\033[m')
        print('\033[1;33mTENTE NOVAMENTE COM OUTRO NOME DE PLATAFORMA!\033[m')
        print('-'*100)
        programa(usuario)
    elif (f'{plataforma}',) not in lista:
        comando_sql3 = "INSERT INTO senhas (plataforma, senha, id) VALUES (%s, %s, %s)"

        cursor.execute(comando_sql3, dados2)

        print('\033[32mSENHA CADASTRADA COM SUCESSO!\033[m')

    time.sleep(1)
    print("-"*100)
    programa(usuario)


def decodificador(senha, idf, usuario):
    resp = str(input('Qual senha deseja decodificar?:'))
    comando_getplat = f'SELECT plataforma FROM `senhas` WHERE id = {idf}'
    cursor.execute(comando_getplat)
    plat1 = cursor.fetchall()

    y = list()

    c = 0

    while c != len(plat1):
        plat = ''.join(map(str, plat1[c]))
        c += 1
        y.append(plat)


    print('')


    if resp in y:
        comando_getsenhas = f"SELECT senha FROM senhas WHERE plataforma = '{resp}' AND id = {idf}"
        cursor.execute(comando_getsenhas)
        senha1 = cursor.fetchall()
    elif resp not in y:
        print('n')
        

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','@','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ',' ']


    c = 0
    while c != len(senha1):
        senha = ''.join(map(str, senha1[c]))

        lixo = '[](),'

        for i in range(len(lixo)):
            senha_formatada = senha.replace(lixo[i],"")
        c+=1
        
    y = list(senha_formatada)

    c2 = 0

    while c2 != len(senha_formatada):
        id = y[0 + c2]
        index = alfabeto.index(id)
        y[0 + c2] = alfabeto[index - 1]
        c2 += 1
    z = "".join(y)
    
    print(f'A senha decodificada é: {z}')
    
    print('-'*100)
    print('')
    time.sleep(0.5)
    programa(usuario)


def exibir_senhas(usuario):
    print('-'*100)
    print('\033[32mESSAS SÃO SUAS SENHAS CADASTRADAS:\033[m')
    print('')
    comando_getid = f"SELECT id FROM cadastros WHERE usuario = '{usuario}'"
    cursor.execute(comando_getid)
    x = cursor.fetchall()
    x2 = str(x)
    if x2[4] == ',':
        idf = x2[2:4]
    elif x2[4] != ',':
        idf = x2[2:5]

    comando_getsenhas = f'SELECT senha FROM `senhas` WHERE id = {idf}'
    cursor.execute(comando_getsenhas)
    senha1 = cursor.fetchall()
    comando_getplat = f'SELECT plataforma FROM `senhas` WHERE id = {idf}'
    cursor.execute(comando_getplat)
    plat1 = cursor.fetchall()

    c = 0

    while c != len(senha1):
        senha = ''.join(map(str, senha1[c]))
        plat = ''.join(map(str, plat1[c]))

        lixo = '[](),'

        for i in range(len(lixo)):
            senha_formatada = senha.replace(lixo[i],"")

        for i in range(len(lixo)):
            plat_formatada = plat.replace(lixo[i],"")

        print(f'{senha_formatada} plataforma é {plat_formatada}')

        c +=1
        print('')
    resp = 'a'
    while True:
        print('DESEJA DECODIFICAR SUAS SENHAS?')
        resp = str(input('S/N:'))
        if resp.lower() == 's':
            decodificador(senha_formatada, idf, usuario)
            break
        elif resp.lower() == 'n':
            time.sleep(1)
            print('-'*100)
            programa(usuario)
        else:
            print('\033[31mDIGITE UM OPÇÃO VALIDA!\033[m')


def programa(usuario):
    dados = usuario
    comando_sql2 = f"SELECT id FROM cadastros WHERE usuario = '{dados}'"
    cursor.execute(comando_sql2)
    x = cursor.fetchall()
    x2 = str(x)
    if x2[4] == ',':
        idf = x2[2:4]
    elif x2[4] != ',':
        idf = x2[2:5]

    print('')
    print('CADASTRAR SENHA [1]'
          '\nVER SUAS SENHAS [2]'
          '\nSAIR DO PROGRAMA[3]')
    print('')
    op = int(input(('Qual opção você deseja:')))
    
    if op == 1:
        plataforma = str(input('Qual a plataforma você deseja registrar a senha: '))
        strS = str(input(('Digite sua senha:')))
        codificador(strS, plataforma, idf, usuario)
    elif op == 2:
        exibir_senhas(usuario)
    elif op == 3:
        print('')
        print('Saindo do programa!')
        c = 0
        while c != 5:
            print('.')
            time.sleep(0.5)
            c += 1
        exit()

# INICIALIZADOR 
if __name__ == '__main__':
    main()

