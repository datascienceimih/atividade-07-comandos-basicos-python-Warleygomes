# -*- coding: utf-8 -*-
"""
Atividade_7
Projeto_Integrador
Ciências de Dados
autor: Warley Gomes 
"""
# 1 - Em comentários, explique o que cada comando faz:

5 + 5         # Soma 5 e 5. 
8 - 6         # Subtrai 8 por 6.
12 * 5        # Multiplica 12 por 5.
4 ** 2        # 4 elevado a 2.
27 ** (1/3)   # Raíz cúbica de 27.
27 / 3        # Divide 27 por 3. 
27 // 4       # Mostra o resultado inteiro da divisão 27 por 4.
27 % 4        # Mostra o resto da divisão 27 por 4


print('Este exercício é muito legal!') # Mostrar na tela essa frase.
x = 7 # Atribui o valor 7 em x. 
print(' O exercício_'  + str(x) + ' é muito fácil!') 
x, y = 5,6 # Atribui o valor 5 em x e o valor 6 em y.
print(x,y) # mostrar o valor de x e y.
print('Aprendi na escola que o {} vem antes do {}'. format (x,y)) # Mostra na tela 
# a frase entre aspa simples e insere os valores de x / y 
# dentro de cada chaves completando a frase.
meuNome = 'Neylson Crepalde' # Define o objeto meuNome com o que está entre aspas simples.
print(meuNome[:8]) # mostra as letras do meuNome desde o início até o elemento 7 (começando do 0)
print(meuNome[8:]) # mostra as letras do meuNome desde o elemento 8 até o último.



galera = ['Neylson', 'Edésio', 'Layla', 'Gerson', 'Iago','Ester', 'Juliany', 'Marcos', 'Patrick', 
          'Bia', 'Fabiano', 'Larissa', 'Sávio', 'Túlio', 'Vanessa', 'Numiá', 'Adelvan', 'Nelson', 
          'Warley', 'Vladimir']
          # atribui todos esses nomes (elementos) em "galera".

galera[1]   # mostra o segundo nome (elemento) da lista. [Edésio]
galera[0]   # mostra o primeiro nome (elemento) da lista. [Nelson]
# obs: [0 é o primeiro 1 é o segundo...]
galera[:5] # mostra os cincos primeiros (elemento) da lista.
galera[10:] # mostra desde o onze (elemento) até o final desta lista.
galera[6:15]  # mostra desde o sete (elemento) até o quinto elemento da lista.

# 2 - Crie três listas. A primeira deve conter o nome de 5 amigos de infância.
# A segunda deve conter o nome e 5 animais de estimação. 
# A terceira deve conter 5 pratos que você adora comer (use a criatividade).
# Exiba o conteúdo das listas.

amigosDeInfancia = ['Cesar', 'Felipe', 'Caroline', 'Ingrid', 'Lucas']
animaisDeEstimacao = ['Aladim','Bethoven', 'Catarina', 'Tute', 'Nino']
PratosPreferidos = ['Lasanha', 'Salmão', 'Strogonoff', 'Frango com quiabo', 'escondidinho']

print(amigosDeInfancia, animaisDeEstimacao, PratosPreferidos)

# 3 - Printe o nome do terceiro amigo da lista.
print(amigosDeInfancia[2])

# 4 - Bole uma frase bonitinha para chamar um bicho e insira nesse frase o nome do último 
# bicho de estimação. Printe a frase na tela.
print(f'Venha no papai, pois o papai chegou! Vem {animaisDeEstimacao[-1]} !')

# 5 - Exiba na tela uma frase perguntando o que você quer comer no jantar essa noite e dê três opções: o segundo,
# terceiro e quarto pratos. (dica, use os comandos print e .format)

print(f'Olá, Warley! O que gostaria de comer essa noite no jantar? \n \
No Menu está disponiveis três opções de pratos:\n \
1){pratos[1]} \n \
2){pratos[2]} \n \
3){pratos[3]} \n \
Qual opção você deseja ?')

# 6 - Crie um objeto chamado nomeCompleto e atribua a ele o seu nome completo como uma string.
nomeCompleto = 'Warley Gomes de Andrade'

# 7 - Usando apenas slices (subsettings de um dado de texto) exiba apenas seu primeiro nome,
# apenas seu nome do meio e apenas seu sobrenome, um por vez.
print(nomeCompleto[:6])
print(nomeCompleto[7:13])
print(nomeCompleto[16:])

# 8 - Crie um dicionário com dados sobre a sua casa. Pense em dados que seriam interessantes de serem usados 
# numa pesquisa de verdade - quantidade de moradores, bairro de localização, nomes das pessoas que moram, idade, cor, sexo,
# tipo de moradia (casa ou apartamento) e mais quatro campos. 
# Use a criatividade!!! Lembre-se de que num dicionário, os valores podem ser qualquer tipo de dado (string, int, float, listas, dicionários, etc.)
# e podem também ser de qualquer tamanho.

casa = {'quantidade de moradores': 2,
        'bairro': 'Lourdes',
        'nomes': ['Warley', 'Leandro'],
        'idades': [23, 33,],
        'cor': ['Branco(a)', 'Negro(a)'],
        'sexo': ['Masculino', 'Feminino'],
        'tipo de moradia': ['Casa', 'Apartamento'],
        'Escolaridade': ['Ensino médio completo', 'Superior completo'],
        'tem algum tipo de alergia': ['Não', 'Sim'],
        'estado civil': ['Solteiro(a)', 'Solteiro(a)'],
        'Exerce atividade remunerada': ['Não','Sim']}

# 9 - Exiba apenas as chaves do dicionário. Exiba apenas os valores do dicionário.

casa.keys()
casa.values()

# 10 - Exiba apenas o nome da segunda pessoa que mora na sua casa.

casa['nomes'][1]

# 11 - Escolha mais duas informações relevantes e exiba no console.

casa['Escolaridade'][0]
casa['tem algum tipo de alergia']



