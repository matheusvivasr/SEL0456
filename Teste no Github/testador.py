import pandas as pd

def readFile(name):
    fileDirectory, fileExtension = "./Teste no Github/",".data"
    fileName = fileDirectory+name+fileExtension
    inputFile = pd.DataFrame([linhas.strip().split() for linhas in open(fileName).readlines()])
    return pd.DataFrame(inputFile[1:].values,columns=inputFile.iloc[0].values)

def compareFrame(esse:(pd.DataFrame), aquele:(pd.DataFrame)):
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


arquivo1 = readFile("arquivo-1")
arquivo2 = readFile("arquivo-2")

linhas_erradas = compareFrame(arquivo1, arquivo2) 

if linhas_erradas==[]:print("Programa sem erros")
else:print("Os valores foram errados encontrados nas linhas onde n = {",", ".join(linhas_erradas),"}")