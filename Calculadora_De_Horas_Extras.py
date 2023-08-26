# Nome de entrada
print('Bem vindo')

nome = str(input('Digite o seu nome? ')).title()

# Multiplicador 1.5 por hora.
m = 1.5
m2 = 2

while True:
    escolha = str(input("Gostaria de calcular as horas extras da 'semana',ou do 'domingo',\nas horas extras da semana inclui de segunda a sabado, de domingo referece a domingo e feriados, faça sua escolha \npara sair digite 'sair'? "))

    if escolha == 'semana':

        # Pagamento regular por hora
        salario = float(input('Qual é o seu salário? '))
        cargahoraria = float(input('Qual a sua carga horária mensal na empresa? Por gentileza use . e não : '))
        horasextras = float(input('Quantas horas extras você trabalhou nesta semana? Por gentileza use . e não : '))

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
            print(f'Até logo. {nome}')
            break
        else:
            print(f'Vamos lá. {nome}')
    elif escolha == 'sair':
        break
    elif escolha == 'domingo':
        # Pagamento regular por hora
        salario = float(input('Qual é o seu salário? '))
        cargahoraria = float(input('Qual a sua carga horária mensal na empresa? Por gentileza use . e não : '))
        horasextras = float(input('Quantas horas extras você trabalhou neste domingo ou feriado? Por gentileza use . e não : '))

        # Encontrando o valor da sua hora na empresa
        valordahoranormal = salario / cargahoraria
        # Multiplicando o valor da sua hora por 1.5
        valordahoraextra = valordahoranormal * m2
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
            print(f'Até logo. {nome}')
            break
        else:
            print(f'Vamos lá. {nome}')
        