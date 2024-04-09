login = input('Digite um Login: ') 
print(30*'-')
senha = input('digite uma senha: ')

print('Loguin Criado com sucesso!!!')
print(30*'-')
print('Agora digite o seu login')

logar = input('login: ')
print(30*'-')
print('Digite a sua senha')
senha_entrar = input('Senha: ')

print(30*'-')

if logar == login and senha_entrar == senha:
    print('Você entrou!!!!!')
    print(30*'-')   

elif logar != login or senha_entrar != senha:
    print('Senha ou login foram digitado Incorretamente')
    print(30*'-')

    redefinir = input('Deseja redefinir senha? [s] ou [n]')

    if redefinir == "s" or redefinir == 'S':
        print(30*'-')   
        loguin2 = input('digite o seu login: ')

        if loguin2 == login:
            
            print(30*'-')   
            redefinir_senha = input('Digite a sua nova senha ')
            senha = redefinir_senha 
            print(30*'-')

            print("Sua senha foi redefinida com SUCESSO !!!")
            
            print(30*'-')
            if logar == login and senha_entrar == senha:
                print(30*'-')
                print('Você entrou!!!!!')
                print(30*'-')

        else:
            print('Você digitou o seu login errado')
            print(30*'-')
            print('Verifique os deus dados e tente novamente!!')
    else:
        print('Voce não conseguiu logar, Verifique seu login e a sua senha e tente novamente')
