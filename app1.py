# Entrada e saida de dados 

nome = input ('Qual o seu nome?')
dia = input('Que dia você nasceu?')
mes = input('Qual mês ?')
ano = int(input('Qual ano ?'))  # usei o int para mostrar que o input seria um numero inteiro para que eu pudesse montar a conta de subtração na linha de baixo
idade = 2024 - ano

print('sendo assim', nome , ', voce tem' , idade, 'anos,', 'pois nasceu dia', dia, 'do mês de', mes, 'do ano de', ano)

