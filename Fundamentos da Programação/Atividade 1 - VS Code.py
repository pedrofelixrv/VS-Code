"Atividade - VS Code"

# Atribuindo valores à variáveis.
height = 1.79
weight = 68.7
# Mostrando o valor de uma variável utilizando o comando print.
print(weight)
# Utilizando operação de divisão e potenciação com números.
print(68.7 / 1.79 ** 2)
# Utilizando operação de divisão e potenciação com as variáveis peso e altura.
print(weight / height ** 2)
# Atribuindo o valor da operação de divisão e potenciação à uma variável.
bmi = weight / height ** 2
# Utilizando o comando "print" para mostrar o valor da variável "bmi".
print (bmi)
# Utilizando o comando "type" para revelar o tipo da variável. São os tipos: Float ou flutuante, são variáveis que apresentam números decimais.
print(type(bmi))
# Int são o tipo de variáveis que possuem numéros inteiros.
day_of_week = 5
type (day_of_week)
print(type(day_of_week))
# Str ou string, são variáveis que possuem texto.
x = 'body mass index'
y = "this works too"
type (y)
print(type(y))
# O tipo de variável bool são variaveis que possuem o dois valores, verdadeiro ou falso, nunca uma terceira situação.
z = True
type (z)
print(type(z))
# Soma de números inteiro por meio do sinal "+".
print(2 + 3)
# Contatenação se trata do ato de unir strings. A seguir, um exemplo de contatenação da string 'ab' mais a string 'cd'.
print('ab' + 'cd')
# Também é possivel contatenar variáveis do tipo strin. Nesse caso, a variável A recebe 'ab' e a variável B recebe 'cd' que são contatenadas.
A = 'ab'
B = 'cd'
print(A + B)
# exemplo
print(5/8)
# soma de 7 com 8
print(7 + 8)
# Operação de soma e subtração atribuidas a uma variável.
soma = 5 + 6
print (soma)
subtração = 5 - 6
print (subtração)
# Operação de potenciação, multiplicação e resto de divisão atribuidas a uma variável.
pontência = 5 ** 3
multiplicação = 5 * 3
resto_da_divisão = 5 % 3
print (pontência)
print (multiplicação)
print (resto_da_divisão)
# Operação sendo atribuida a uma variável.
rendimento = 100 * 1.1 ** 7
print (rendimento)

"SEGUNDA AULA - 22/03"

# Operação realizada com variáveis e contatenação de uma variável com ela mesmo.
savings = 100
growth_multiplier = 1.1
desc = 'compound interest'
year1 = savings * growth_multiplier
print (type(year1))
doubledesc = desc + desc
print (doubledesc)
# Operação de conversão de uma variável do tipo string para uma variável do tipo float.
pi_string = '3.1415926'
pi_float = float (pi_string)
print (type(pi_string))
print (type(pi_float))
# Contatenando strings e inteiros
savings = 100
result = 100 * 1.10 ** 7
# print ("I started with" + savings + "and now have" + result + ". Awesome!")
# Não é possível contatenar str com número. Para corrigir o problema, convertemos os números para texto, ou colamos virgulas entre os momentos, separando 'str' de 'int' e 'float'
print ("I started with $" + str(savings) + "and now have $" + str(result) + ". Awesome!")
# ou
print ("I started with $", savings, "and now have $", result, ". Awesome!")

"TERCEIRA AULA - 28/03"

# Atribuindo uma lista, que ficam entre colchetes, a uma variável. O que está entre [] e separados por virgula são os elementos dessa lista.
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)
# Dentro de uma lista é possível coexistir string, int, float e etc.
fam = ['Pedro', 1.70, 'Cristiane', 1.65, 'Dulce', 1.30, 'Gabriela', 1.55]
print(fam)
# Dentro de uma lista é possível que haja outras listas. Nesse exemplo, a lista "fam2" possui outras listas em seu valor, essas sub-listas são separadas por [].
fam2 = [['Pedro', 1.70],
        ['Cristiane', 1.65],
        ['Dulce', 1.30],
        ['Gabriela', 1.55]]
print(fam2)
# O tipo da varíavel "fam" é "list"
type(fam)
print(type(fam))
print(type(fam2))
# Atribuindo valores a variáveis para criar uma lista a partir delas.
# Áreas dos compartimentos
hall = 14.0
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Criando uma lista com as áreas dos compartimentos
áreas = [hall, kit, liv, bed, bath]
# "Printando" a lista das áreas
print(áreas)
# Adaptando a lista
áreas = 'hallway', hall, 'kitchen', kit, 'living room', liv, 'bedroom', bed, 'bathroom', bath
print(áreas)
A = [1, 2, 3, 4]
# "A" é uma lista qye possui quatro elementos inteiros
B =[[1, 2, 3], [4, 5, 6]]
# "B" é uma lista na qual possui outras duas lista dentro, sendo cada lista possuindo três elementos inteiros
C = [1 + 2, 'A' * 5, 3]
# "C" é uma lista na qual possui três elementos, sendo o primeiro elemento uma soma de inteiros, o segundo elemento a multiplicação de uma string, e o terceiro elemento um inteiro.
# Lista de listas das áreas dos compartimentos
house = [['hallway,', hall],
         ['kitchen', kit],
         ['living room', liv],
         ['bedroom', bed],
         ['bathroom', bath]]
#  "Printando" a lista das lista
print(house)
# "Printando" o tipo da variável "house"
print(type(house))
# Buscando o segundo elemento da lista "fam"
print(fam[2])
# Buscando o sexto elemento da lista "fam"
print(fam[6])
# Buscando o segundo elemento da lista "house"
print(house[2])
# Buscando o terceiro elemento da lista "house"
print(house[3])
# Buscando o elemento da lista "house" de trás para frente por meio dos números negativos
print(house[-2])
# Pegando a parte da lista "fam" apartir do sexto elemento até o oitavo, observando que a contagem dos elementos começa a partir do número 0. 
print(fam[6:8])
print(fam[2:4])
print(fam[4:6])
# Pegando do quarto elemento até o final da lista "fam"
print(fam[4:])
# "Printando" o segundo elemento da lista de áreas
print(áreas[2])
# "Printando" o ultimo elemento usando o index negativo
print(áreas[-1])
# "Printando" o valor de "living room"
print(áreas[4])