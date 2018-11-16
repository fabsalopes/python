# Programa para calcular a média ponderada de um aluno

try:
    #variáveis
    media = float(input('Digite a MÉDIA escolar: '))
    peso1 = float(input('Digite o PESO da primeira prova: '))
    peso2 = float(input('Digite o PESO da segunda prova: '))
    nota1 = float(input('Digite a NOTA da primeira prova: '))
    nota2 = float(input('Digite a NOTA da segunda prova: '))

    #resolução
    media = ((peso1*nota1) + (peso2*nota2)) / (peso1+peso2)

    #impressão
    print('A MÉDIA do aluno é:',media)

    #resultado_final
    if media >= 7:
       print('APROVADO')
    else:
       print('REPROVADO')

except ValueError:
    print("Somente valores númericos")

#sair do programa
input ('Aperte enter para sair')
