#Crie um programa que tenha a funcao leiaInt(),
#que vai funcionar de forma semelhante a função
#input() do python. So que fazendo a validação para aceitar apenas um valor númerico.
#Ex: inteiro, real. Obs: Se o usuario não digitar o valor, 
#quero que ele atribua o valor 0 a aquela variável.
def leiaInt():
    a=(input("Insira um número:"))
    stringS(a)
    if (a == ""):
        a=0
        print("Campo em branco, valor",a,"atribuído.")
    else:
        print("Valor digitado igual a:",a)

def stringS(valor):
    try:
        float(valor)
    except (ValueError):
        print("Valor não pôde ser aceito.")
        SystemExit
leiaInt()
