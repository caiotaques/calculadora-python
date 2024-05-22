'''

Desafio: 

Crie um pacote em Python que implemente uma calculadora com as operações básicas (soma, subtração, multiplicação e divisão) e funções adicionais 
(potenciação, raiz quadrada e logaritmo) e que possa ser facilmente utilizado em outros projetos.

Lembre-se de que você já conhece o nível avançado da linguagem de programação Python e com este desafio, você irá praticar a criação de pacotes em Python, 
a organização de módulos e scripts em diretórios, além de aprender a tornar o seu código reutilizável e facilmente instalável em outros projetos.

'''
import math


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def potencia(a,b):
    return math.pow(a, b)

def raiz(a):
    return math.sqrt(a)

def log(a):
    return math.log10(a)