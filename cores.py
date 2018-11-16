# progrma apara listar as cores existentes

cores = {"verde": "green", "vermelho": "red", "preto": "black", "branco": "white"}
cor = input('Escolha a cor para traduzir: ')
traducao = cores.get(cor, 'Esta cor não consta na lista')
print(traducao)
