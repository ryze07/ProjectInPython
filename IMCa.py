nome =  input ("Qual o seu nome? ")
altura = float(input( "Qual a sua altura? "))
peso = int(input("Qual o seu peso? "))

imc =  peso / (altura * altura) 

print(f'Nome: {nome} e tem a altura de {altura}')
print(f'Pesa: {peso} Quilos')
print(f"E seu IMC é: {imc:.2f}")