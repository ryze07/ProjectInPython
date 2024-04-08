voce = input('Qual o seu nome?')
primeiro_irmao = input('Qual o nome do seu irmão? ')
segundo_irmao = input('Qual o nome do seu segundo irmão? ')

idade = int(input('Qual a sua idade '))
idade_primeiro =  int(input(f'qual a idade do {primeiro_irmao}? '))
idade_segundo =  int(input(f'Qual a idade do {segundo_irmao}? '))


if idade > idade_segundo > idade_primeiro : # 1 3 2
    print(f'1 {voce} com {idade} anos o mais velhor, {segundo_irmao} tem {idade_segundo} anos do meio e {primeiro_irmao} tem {idade_primeiro} anos é o caçula')

elif idade > idade_primeiro > idade_segundo: # 1 2 3
    print(f'2 {voce} com {idade} anos o mais velhor, {primeiro_irmao} tem {idade_primeiro} anos do meio e {segundo_irmao} com {idade_segundo} anos é o caçula')

elif idade_primeiro > idade_segundo > idade : # 2 3 1
    print(f'3  o mais velhor é {primeiro_irmao} tem {idade_primeiro} anos, {segundo_irmao} com {idade_segundo} anos o caçula {voce} com {idade} anos do meio')

elif idade_primeiro > idade  > idade_segundo:# 2 1 3
    print(f'4 {primeiro_irmao} tem {idade_primeiro} anos e é mais velhor, {voce} com {idade} anos do meio {segundo_irmao} com {idade_segundo} anos é o caçula')

elif idade_segundo > idade_primeiro > idade: # 3 2 1 
    print(f'5 {segundo_irmao} com {idade_segundo} anos o mais velho, {primeiro_irmao} tem {idade_primeiro} anos o do meio e {voce} com {idade} anos é o caçula')

else: # 3 1 2
    print(f'6 {segundo_irmao} com {idade_segundo} anos o mais velho, {voce} com {idade} anos o do meio e {primeiro_irmao} tem {idade_primeiro} idade é o caçula')