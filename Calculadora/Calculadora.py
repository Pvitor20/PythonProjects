produto = 0
atuante = 0
acao = " "

def somar(produto, atuante):
    return produto + atuante

def subtrair(produto, atuante):
    return produto - atuante

def mult(produto, atuante):
    return produto * atuante

def dividir(produto, atuante):
    return produto / atuante if atuante != 0 else "Erro: Divisão por zero"

produto = float(input("Passe o valor inicial: "))

while acao != '=':
    acao = input("Digite '+' para somar, '-' para subtrair, 'x' para multiplicar, '/' para dividir e '=' para finalizar a operação").lower()
    if acao == '+':
        atuante = float(input('Qual valor deseja acrecentar:'))
        produto = somar(produto, atuante)

    elif acao == '-':
        atuante = float(input('Qual valor deseja subtrair:'))
        produto = subtrair(produto, atuante)

    elif acao == '*':
        atuante = float(input('Qual valor deseja multiplicar:'))
        produto = mult(produto, atuante)

    elif acao == '/':
        atuante = float(input('Qual valor deseja dividir:'))
        produto = dividir(produto, atuante)

print(f"Resultado final: {produto}")