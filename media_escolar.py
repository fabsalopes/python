# Programa para calcular a média escolar de um aluno

try:
   #variáveis
   media = float(input('Qual sua média escolar ?: '))
   nota1 = float(input('Digite a nota da primeira prova: '))
   nota2 = float(input('Digite a nota da segunda prova: '))

   #resolução
   media = ((nota1) + (nota2)) / 2

   #impressão
   print('Sua média é:',media)

   #resultado_final
   if media >= 7:
      print('APROVADO')
   else:
      print('REPROVADO')

except ValueError:
    print('Somente valores numéricos')

#sair do programa
input ("Aperte enter para sair")
