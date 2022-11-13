from pandas import DataFrame as pDF

def nameFile(name:str):
    fileExtension, fileDirectory  = ".data","./Teste no Github/"
    return fileDirectory+name+fileExtension

def fatorial(n:int):    
    if n<=1:return 1
    else:return n*fatorial(n-1)

def fibonacci(n:int):  
    if n<1:return 0
    elif n==1:return 1
    else:return fibonacci(n-1)+fibonacci(n-2)

class Numero():
    def __init__(self,num:int):
        self.n=num
    def line(self):    #simplifica o cálculo de cada numero.
        return [self.n,fatorial(self.n),fibonacci(self.n)]

def fiboFactFile(fileName:str,numList:[int]):
    outName = nameFile(fileName)
    cols = ['#', 'fact', 'Fib']
    # Faz o arquivo de saída calculado com o método `.line()`.
    outText = pDF([Numero(int(n)).line() for n in numList],columns=cols)
    with open(outName,"w") as testOut:
        testOut.write(' '.join(cols))
        testOut.write('\n')
        for i in range(outText.shape[0]):   #escreve o arquivo de saída em acordo com o modelo esperado.
            for j in range(outText.shape[1]):
                testOut.write(str(outText.iloc[i].values[j]))
                if j < outText.shape[1]-1: testOut.write(' ')
            if i < outText.shape[0]-1: testOut.write('\n')