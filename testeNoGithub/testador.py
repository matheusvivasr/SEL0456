from pandas import DataFrame as pDF
from fiboFact import fiboFactFile, nameFile as fff, nf

def readFile(name:str):
    fileName = nf(name)
    inputFile = pDF([linhas.strip().split() for linhas in open(fileName).readlines()])
    return pDF(inputFile[1:].values,columns=inputFile.iloc[0].values)

def compareFrame(esse:pDF, aquele:pDF):
# Compara os dados e devolve uma lista com os números para os quais os valores divergiram.
    wLines = []     
    if not esse.equals(aquele):
        bino = esse.eq(aquele)  
        # Retorna uma matriz binária em que True são valores de mesmo indice idênticos.
        for i in range(bino.shape[0]):
            if not (bino.iloc[i].iat[1] and bino.iloc[i].iat[2]): 
            # NAND para conferir se nem o fatorial nem o fibonacci estão errados.
                wLines.append(esse["#"].iat[i]) 
                # escreve para quais valores a resposta esta errada.
    return wLines


print("- Teste com o arquivo dado:")
try:
    arquivo1 = readFile("arquivo-1")
    arquivo2 = readFile("arquivo-2")
    linhas_erradas = compareFrame(arquivo1, arquivo2)
    if linhas_erradas==[]:print("   Arquivo sem erros.")
    else:print("   Os valores foram errados encontrados nas linhas onde n = {",", ".join(linhas_erradas),"}.")
except IOError:
    print("   ERRO: Arquivos inexistentes! Verifique se os arquivos estão na pasta certa e o nome correto.")

print("- Teste com o 'arquivo-test.data' gerado pelo 'fiboFact.py':")
try:
    arquivoT=readFile("arquivo-teste")
except IOError:
    fff("arquivo-teste",arquivo1["#"].values)
arquivoT=readFile("arquivo-teste")

linhas_erradasT = compareFrame(arquivo1, arquivoT)
if linhas_erradasT==[]:print("   Programa sem erros.")
else:print("   Os valores foram errados encontrados nas linhas onde n = {",", ".join(linhas_erradasT),"}")