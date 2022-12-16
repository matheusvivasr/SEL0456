press = ['Pascal','Atmosfera','Bar','Torr']
pressConst = [[1,1],[1,101325],[1,100000],[133322,1000]]

def tratarNum(num:str):
    num.replace(',','.')
    return float(num)

def numOut(num:float):
    num = round(num,3)
    num = str(num)
    return num.replace('.',',')

def celciusFar(n):
    n = tratarNum(n)
    return (n*9/5)+32

def farCelcius(n):
    n = tratarNum(n)
    return (n-32)*5/9

def celciusK(n):
    n = tratarNum(n)
    return n+273.15

def kelCelcius(n):
    n = tratarNum(n)
    return n-273.15

def pressoes(num,entrada:str, saida:str):
    num = tratarNum(num)
    unidadeIn = press.index(entrada)
    unidadeOut = press.index(saida)

    num = num*pressConst[unidadeIn][1]/pressConst[unidadeIn][0]
    num = num*pressConst[unidadeOut][0]/pressConst[unidadeOut][1]

    return num