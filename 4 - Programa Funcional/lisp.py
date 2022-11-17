def fatorial(n:int):    
    if n<=1:return 1
    else:return n*fatorial(n-1)

def fibonacci(n:int):  
    if n<1:return 0
    elif n==1:return 1
    else:return fibonacci(n-1)+fibonacci(n-2)

texto = [linhas.strip().split() for linhas in open("./input.dat").readlines()]

with open("out.dat", "w") as saida:
    l = 1
    for linha in texto:
        x, y = linha
        fx = fibonacci(int(x))
        fy = fatorial(int(y))
        exp = f"Linha {l}:  Fibo: {fx};  Fact: {fy}"
        saida.write(exp)
        l+=1
        if l <= len(texto):
            saida.write("\n")

