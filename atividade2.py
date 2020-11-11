#Depois reecreva a função leiaInt(), agora incluindo a possibilidade
#da digitação de um tipo invalido(fazendo as condições de erro).
#E depois Crie também uma função leiaFloat() com essa mesmafuncionalidade.

def leiaInt():
    a=(input("Insira um número inteiro:"))
    if (a == ""):
        a=0
        print("Campo em branco, valor",a,"atribuído.")
    else:
        print("Valor digitado igual a:",a)
    verifInt(a)

def verifInt(valor):
    try:
        int(valor)
    except (ValueError):
        print("Valor não é um número.")
        SystemExit
    leiaFloat()

def leiaFloat():
    a=(input("Insira um número com vírgula:"))
    if (a == ""):
        a=0
        print("Campo em branco, valor",a,"atribuído.")
    else:
        print("Valor digitado igual a:",a)
    verifFloat(a)

def verifFloat(valorF):
    try:
        float(valorF)
    except (ValueError):
        print("Valor não é um número.")
        SystemExit
leiaInt()