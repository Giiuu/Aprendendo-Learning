nome = str(input('Qual seu nome?'))
salario = float(input('Nos diga qual o seu salário mensal atual e aumentaremos em 15%!'))
salarionovo = salario * 1.15
print('{}, seu salário era de R${} e agora é de R${}'.format(nome, salario, salarionovo))