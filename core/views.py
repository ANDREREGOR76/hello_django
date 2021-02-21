from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse('<h1>hello {} de {} anos</h1>'.format(nome, idade))

def soma(requests, num1, num2):
    som = num1 + num2
    return HttpResponse('<h1>A soma de {} e {} é {}</h1>'.format(num1, num2, som))

def subtracao(requests, num1, num2):
    sub = num1 - num2
    return HttpResponse('<h1>A subtração de {} e {} é {}</h1>'.format(num1, num2, sub))

def multiplicacao(requests, num1, num2):
    multi = num1 * num2
    return HttpResponse('<h1>A multiplicação de {} e {} é {}</h1>'.format(num1, num2, multi))

def divisao(requests, num1, num2):
    div = num1 / num2
    return HttpResponse('<h1>A divisão de {} e {} é {}</h1>'.format(num1, num2, div))
