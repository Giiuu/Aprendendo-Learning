aluno = str(input('Qual seu nome?'))
nota1 = float(input('Qual sua primeira nota?'))
nota2 = float(input('Qual sua segunda nota?'))
nota3 = float(input('Qual sua terceira nota?'))
média = (nota1 + nota2 + nota3) / 3
print('Olá, {}, de acordo com os calculos do nosso sistema a sua média é: {:.1f}'.format(aluno, média))