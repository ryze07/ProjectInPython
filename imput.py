nome = input("qual é o seu nome? ")

print (f"olá {nome}")

dtnascimento = int(input("digite seu ano de nascimento "))
anos =  2024 - dtnascimento 
meses = anos * 12
semana = anos * 52
dia = semana * 7
hora = dia * 24

print(f'Olá {nome} você tem {anos} anos, {meses} meses, {semana} semanas, {dia} de dias e {hora} horas de vida')


