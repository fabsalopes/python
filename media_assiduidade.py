# Programa para calcular a média, assiduidade e o resultado 'aprovado' ou 'reprovado' por média e/ou assiduidade

nome = input('Digite o nome do aluno: ').title()

try:
    nota1 = float(input('Digite a nota da prova 1: '))
    nota2 = float(input('Digite a nota da prova 2: '))
    faltas = int(input('Digite o número de faltas: '))

    media = (nota1+nota2)/2
    assid = (20-faltas)/20

    if media >= 6 and assid >= 0.7:
        resultado = 'APROVADO'

    elif media < 6 and assid < 0.7:
        resultado = 'Reprovado por média e por faltas'

    elif media < 6:
        resultado = 'Reprovado por média'

    elif assid < 0.7:
        resultado = 'Reprovado por faltas'

    else:
        print ('Erro')

    print('Nome',nome)
    print('Média',media)
    print('Assiduidade',str(assid*100)+'%')
    print('Resultado',resultado)

except ValueError:
    print("Somente valores númericos")
