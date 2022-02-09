 # LISTA III

# 1) Faça um programa que receba, via teclado, um número inteiro n e dois números inteiros i e f, que definem o início e o fim de um intervalo [i, f].
# O programa deve imprimir a tabuada de multiplicação de n entre os valores i e f. Utilize o laço for.
'''
n = int(input('Digite um número inteiro (passo): '))            
i = int(input('Digite um segundo número inteiro (inicio): '))   # 1
j = int(input('Digite um terceiro número inteiro (fim): '))     # 5
for x in range(i, j+1,n):
    for y in range(i, j+1, n):
        print(f'Tabuada da multiplicação: {x} X {y} = {x*y}')
    print()
'''

# 2) Faça um programa que receba, via teclado, dois números inteiros positivos m e n (m < n) e exiba todos os números múltiplos de 3 no intervalo [m, n].
'''
m = int(input('Digite um número inteiro de inicio da sequência: ')) # 3
n = int(input('Digite um número inteiro de fim da sequência: '))    #12
for x in range(m, n+1, 3):
    print(x)
'''

# 3) Faça um programa que receba, via teclado, dois números inteiros positivos m e n (m < n) calcule e exiba a soma de todos os números múltiplos de 3
# ou múltiplos de 4 no intervalo [m, n].
'''
m = int(input('Digite um número inteiro (inicio): '))  # 0
n = int(input('Digite um número inteiro (fim): ')) # 12
s = 0
for x in range(m, n+1, 1):
    if m %x == 3 or n %x == 4:
        s += x
        print(f'Os múltiplos são: {s}')
        break
'''

# 4) Faça um programa que receba, via teclado, um número inteiro positivo n e imprima os n primeiros números naturais ímpares.
'''
n = int(input('Digite um número inteiro: '))
for x in range(1,n+1,2):
    print(x)
'''
# 5) Faça um programa que receba, via teclado, um número inteiro positivo n e, posteriormente, receba n números reais,
# determine e exiba o menor valor digitado pelo usuário.
'''
n = int(input('Digite um número inteiro: '))
menor = float(input('Digite o primeiro valor: '))
for x in range(n-1):
    r = float(input('Digite valores reais: '))
    if r < menor:
        menor = float(input('Digite o primeiro valor: '))
print(f'O menor valor digitado é: {menor} ')
'''    


# 6) Faça um programa que receba, via teclado, um número inteiro positivo n e, posteriormente, receba n números reais,
# calcule e exiba a diferença entre a soma dos números pares e a soma dos números ímpares digitados pelo usuário.
'''
n = int(input('Digite um número inteiro: '))
m = 0
g = 0
for x in range(n):
    p = float(input('Digite um valor real: '))
    if p%2 == 0 and p > 0:
        m += p
    elif p%2 !=0 and p > 0:
        g+=p
    else:
        break
    
print(f'A soma ds números pares: {m}, A soma dos números ímpares:{g}; A subtração é: {m-g}')
'''

# 7) Faça um programa que receba, via teclado, um número inteiro positivo n e, posteriormente, receba a idade de n pessoas e imprima:
# quantas pessoas tem menos de 18 anos, quantas tem entre 18 e 30 anos, quantas tem entre 31 e 55 anos e quantas tem mais de 55 anos.
'''
n = int(input('Digite um número inteiro: '))
m = 0
g = 0
l = 0
k = 0
for x in range(1, n):
    r = int(input('Digite sua idade'))
    if r < 18:
       m += 1
       
    elif r >= 18 and r<= 30:
        g += 1

    elif r >= 31 and r <= 55:
        l += 1

    elif r > 55:
        k += 1
    
print(f'{m} pessoas possuem idade menor que 18 anos! {g} pessoas estão com idade entre 18 e 30 anos! {l} pessoas estão com idade entre 31 e 55 anos {k} pessoas possuem idade maior que 55 anos ')
'''

# 8) Faça um programa que receba, via teclado, o primeiro termo a1, a razão, q e o número de termos n
# de uma Progressão Geométrica (PG). Imprima os n
# primeiros números da PG.
'''
a1 = 4
q = 2
n = int(input('Digite um número de termos daa P.G: '))
for x in range(a1,n+1):
    print(f'{x*q}')

'''
# 9) Faça programas que recebam, via teclado, um número inteiro positivo n e calculem os seguintes somatórios:
#a) H(n) = Xn
#b) G(n) = Xn
#c) F(n) = Xn
'''
n = int(input('Digite um número inteiro: '))
H = 0
g = 0
f = 0
for x in range(1,n+1):
    if True:
        H = 1/(x)
    print(f'H(n)={H}')
## Solução imcompleta!!
'''
# 11) Faça um programa que receba, via teclado, um número inteiro positivo n e, posteriormente, receba o
#peso (Kg), altura (m) e o nome de n pessoas. A partir dos dados digitados, o programa deve calcular e
#mostrar o menor e o maior IMC (índice de massa
#corporal) e os respectivos nomes das pessoas.
'''

n     = int(input('Digite o número de pessoas : ')) # n = 4
menor = 10**10
maior = 0
for x in range(1,n+1): # 1, 2, 3, 4
    peso   = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    nome   = input('Digite o nome: ')
    imc    = (peso/(altura**2))
    print(imc)
    if imc > maior:
        maior = imc
        name = nome
    if imc < menor:
        menor = imc
        nime = nome
print(f'Maior IMC: nome = {name}, valor = {maior:.1f}')
print (f'Menor IMC: nome = {nime}, valor = {menor:.1f}')
 
'''
# 12) Faça um programa que calcule e imprima o número
# médio de alunos por turma na UFOB. O programa
# deve receber, via teclado, a quantidade t de turmas e, para cada turma, a quantidade n de alunos.
# Suponha que as turmas não podem ter mais de 45
# alunos (verifique se o número de alunos é válido para
# cada turma e, caso contrário, continue solicitando
# que o usuário digite um novo valor até que seja digitado um valor válido).
'''
t = int(input('Digite a quantidade de turmas: '))
m = 0
for x in range(1,t+1):
    a = int(input('Digite a quantidade de alunos por turma: '))
    if a <= 45:
        a*= t
        m +=a
        print(f'{m}')
    else:
        print('Digite um número q seja menor ou igual a 45!')
print(f'{m/2}')

'''
# 13) Faça um programa que receba, via teclado, um número inteiro positivo n e, posteriormente, receba n
# valores reais positivos (o programa deve aceitar somente valores positivos!), calcule e exiba a média
# geométrica dos valores digitados pelo usuário.
'''
n = int(input('Digite um inteiro positivo: '))
m = 0
t = 1
while n>0:
    for x in range (1,n+1):
        d = float(input('Digite os valores reais: '))
        if d > 0:
            m += d
            t *= d
        else:
            break
    break
#print(f'{d}')
print(f'A média geométrica é: {(t**1/n)/n}')
#print(f'{m}')
            
'''


#14) Faça um programa que receba, via teclado, um número não determinado de valores reais, até que seja
# digitado um valor não numérico, calcule e mostre a
# média aritmética dos números digitados.
'''
j = 0
h = 0
while True:
    p = input('Digite algo: ')
    if p.isnumeric():
        j += float(p)
        h += 1
    else:
        break
print(f'{j/h:.1f}')
'''


# 15) Faça um programa que receba, via teclado, um número não determinado de valores positivos, até que
# seja digitado um número negativo ou zero, calcule e
# mostre a média harmônica dos números digitados.
'''
j= 0
g = 0
while True:
    p = int(input('Digite um número: '))
    if p > 0:
        j += 1
        g += 1/p
    else:
        break
mH = j/g
print(f'{mH:.2f}')

'''

# 16) Faça um programa que receba, via teclado, um número inteiro positivo n e imprima todas as potências
# de dois menores que n.
# (Ex: n = 70 ⇒ 1, 2, 4, 8, 16, 32, 64.)



r = 0
n = int(input('Digite os números positivos: '))
for x in range(n+1):
    if x < n:
        r += 1
        if r%2 == 0:
            
            print(f'{r}')
    else:
        break


# 17) Faça um programa que receba, via teclado, um número inteiro positivo n, calcule e imprima o primeiro múltiplo de 11, 13 ou 17 maior ou igual a n.
# (Ex: n = 40 ⇒ 44.)
'''
n = int(input('Digite um número: '))
while n%11 != 0 and n%13 != 0 and n%17 !=  0:
    n += 1
print(f'O primeiro múltiplo de 11, 13 ou 17 é: {n}')

'''
# 18) Faça um programa que receba, via teclado, um número não determinado de valores inteiros positivos
# (o programa deve aceitar somente valores positivos!) até que seja digitado um número quadrado
# perfeito. Exiba na tela a mensagem: Quadrado Perfeito! (um número é quadrado perfeito quando tem
# um número inteiro com raíz quadrada).
'''
q = 1
g = 1
h = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n > 0:
        h +=1
        q *=n
        g *= q * q
        print(f'{h *g}')    # meio caminho andado
    else:
        break
'''
'''
n = int(input('Digite um valor inteiro positivo: ')) # a = 11
i = 1
while i**2 <= n: # 16 <= 11
    if i**2 == n:
        print(i)
    else:
        i += 1  # i = 4
print(f'Qual o quadrado perfeito mais próximo?  {i}')
'''

# 19) Faça um programa que implemente uma caixa registradora rudimentar. O programa deve receber,
# via teclado, um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero
# deve ser informado pelo operador para indicar o final da compra. Uma vez encerrada a compra, o
# programa deve exibir na tela o valor total da compra e receber, via teclado, o valor em dinheiro que
# o cliente forneceu e, finalmente, calcular e exibir o valor do troco.
'''
a = 0
d = 0
v = 0
while True:
    n = float(input('Digite o valor do produto: '))
    p = float(input('Digite o valor de pagamento: '))
    if n > 0:
        a +=1
        a +=n
        if p > n:
            n -=p
            d +=n
            print(f'Seu troco é de {n}')
            print(d)
        if p < n:
            n -=p
            v +=n
            print(f'Você está devendo um valor de {n}')
            print(v)
            
    else:
        break
print(f'Sua compra foi de {a}, sendo o seu troco de {d}, e você está devendo um valor de {v}! Volte sempre e obrigada pela preferência! ')

'''
# 21) É possível alcançar uma aproximação inteira para
# a raiz quadrada de um número inteiro positivo subtraindo consecutivamente dos resultados a sequência dos números ímpares (1, 3, 5, · · ·) até que o valor
# a ser subtraído seja maior ou igual ao resultado.
# Exemplo: 27
# 27 − 1 = 26
# 26 − 3 = 23
# 23 − 5 = 18
# 18 − 7 = 11
# 11 − 9 = 2
'''
n = int(input('Digite um valor inteiro positivo:')) # n = 27
x = n # x = 27
i  = 1 # Sequencia dos ímpares
c = 0 # Contador
while x >= i:
    x  -= i  # x = 2
    i  += 2 # i = 11
    c += 1 # c = 5
print(f'Aproximação para raiz quadrada de {n} = {c}.')

'''


