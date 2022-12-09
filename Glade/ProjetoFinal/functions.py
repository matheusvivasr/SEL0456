from pandas import DataFrame as pDF
def lerMedidas(medida:str):
    tabela = pDF([linhas.strip().split(',') for linhas in open('constants/'+medida+'.txt').readlines()])
    medidas = pDF(tabela[1].values,index=tabela[0].values,columns=['simbolo'])
    medidas.insert(1,'constante', [int(tabela[2][i])/int(tabela[3][i]) for i in range(len(tabela[1]))])
    return medidas

def lerPotencias():
    tabela = pDF([linhas.strip().split(',') for linhas in open('constants/potencias.txt').readlines()])
    medidas = pDF([[tabela[1][i],tabela[2][i]] for i in range(len(tabela[1]))],index=tabela[0].values,columns=['simbolo','exp10'])
    return medidas 