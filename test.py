""" def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
 
 
print(fact(0))
print(fact(5))

#print(fact(2000))

import sys
sys.setrecursionlimit(3000)
 
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
 
print(fact(2000))

foo = 100
 
def hello():
    print("Eu sou o test.py")
 
if __name__ == "__main__":
    print("Executando como programa principal")
    print('O valor de __name__ e:' , __name__)
    hello()

import test

print(test.foo)
test.hello()
 
print(test.__name__)


def multiplicacao(x,y):
    return x*y

print(multiplicacao(5,8))

lam = lambda x,y: x*y
print(lam(10,9))


print((lambda a,b : a+b)(30,70))"""

print('Liliane tem {} anos e Gustavo tem {} anos'.format(30,36))

print('o ponto flutuante {0:.1f}').format(9056.5784444)

import math
print('o float {0:10.3f}'.format(math.pi))
print('o ponto flutuante pi = {o:10.3f}')

print('Sam tem {1:d} bolas vermelhas e {0:d} bolas amarelas'.format(12,31))

print('o binario 4 e {0:b}'.format(4))

array = [34,66,12]
print('a = {0}, b = {1} e c = {2}'.format(*array))

