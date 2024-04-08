loguin = input('Digite um Login: ') 
senha = int(input('digite uma senha: ')) 

print('Loguin Criado com susseso!!!')
print(30*'-')
print('Agora digite o seu loguin')

logar = input('login: ')
print(30*'-')
print('Digite a sua senha')
senha_entrar = int(input('Senha: '))

print(30*'-')

if logar == loguin and senha_entrar == senha:
    print('Você entrou!!!!!')
    print(30*'-')   

elif logar != loguin or senha_entrar != senha:
    print('Senha ou loguin foram digitado Incorretamente')
    print(30*'-')

    redefinir = input('Deseja redefinir senha? [s] ou [n]')

    if redefinir == "s" or redefinir == 'S':
        print(30*'-')   
        loguin2 = input('digite o seu login: ')

        if loguin2 == loguin:
            
            print(30*'-')   
            redefinir_senha = int(input('Digite a sua nova senha '))
            senha = redefinir_senha 
            print(30*'-')

            print("Sua senha foi redefinida com SUSSECO!!!")
            
            print(30*'-')
            if logar == loguin and senha_entrar == senha:
                print(30*'-')
                print('Você entrou!!!!!')
                print(30*'-')

        else:
            print('Você digitou o seu login errado')
            print('Verifique os deus dados e tente novamente!!')
    else:
        print('Voce não conseguiu logar, Verifique seu login e a sua senha e tente novamente')
