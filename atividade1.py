#Crie um programa que tenha a funcao leiaInt(),
#que vai funcionar de forma semelhante a função
#input() do python. So que fazendo a validação para aceitar apenas um valor númerico.
#Ex: inteiro, real. Obs: Se o usuario não digitar o valor, 
#quero que ele atribua o valor 0 a aquela variável.
import re
def leiaInt():
    a=(input("Insira um número:"))
    if re.match('^\d+$', a) or re.match('^\d+\.\d+$', a):
        print("Valor digitado:",a)
    elif (a == ""):
        a=0
        print("Campo em branco, valor",a,"atribuído.")
    else:
        print("O valor inserido é uma string, inválido!")
leiaInt()
