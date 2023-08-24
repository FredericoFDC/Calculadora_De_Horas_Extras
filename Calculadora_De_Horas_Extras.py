# Nome de entrada
print('Bem vindo')

nome = str(input('Digite o seu nome? ')).title()

# Multiplicador 1.5 por hora.
m = 1.5

while True:
    # Pagamento regular por hora
    salario = float(input('Qual é o seu salário? '))
    cargahoraria = float(input('Qual a sua carga horária mensal na empresa? '))
    horasextras = float(input('Quantas horas extras você trabalhou? '))

    # Encontrando o valor da sua hora na empresa
    valordahoranormal = salario / cargahoraria
    # Multiplicando o valor da sua hora por 1.5
    valordahoraextra = valordahoranormal * m
    # Calculando o valor total das horas extras
    extra = valordahoraextra * horasextras
    # Somando quanto você deverar receber no valor bruto do mês sem descontos
    valor = salario + extra

    print("="*125)
    print(nome)
    print('O valor da sua hora na empresa e de R${:,.2f}.\nO valor da sua hora durante o período de hora extra ficou em R$ {:,.2f}.\nVocê teve um valor bruto de R$ {:,.2f} de horas extras no mês.\nNo final do mês o seu salário bruto será de R$ {:,.2f}.'.format(valordahoranormal,valordahoraextra,extra,valor))
    print("="*125)

    calcular = str(input('Deseja calcular novamente (S/N)? ')).title()
    if calcular == 'N':
        print('Até logo.')
        break
    else:
        print('Vamos lá.')
        