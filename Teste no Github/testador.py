import pandas as pd

def nameFile(name, ext):
    return "./Teste no Github/"+name+ext

def comparar(esse:(pd.DataFrame), aquele:(pd.DataFrame)):
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

fileExtension = ".data"

fileName = nameFile("test", fileExtension)
inputFile = pd.DataFrame([linhas.strip().split() for linhas in open(fileName).readlines()])
testFile = pd.DataFrame(inputFile[1:].values,columns=inputFile.iloc[0].values)

file2Name =  nameFile("test2", fileExtension)   #Arquivo a ser testado.
input2File = pd.DataFrame([linhas.strip().split() for linhas in open(file2Name).readlines()])
test2File = pd.DataFrame(input2File[1:].values,columns=input2File.iloc[0].values)

linhas_erradas = comparar(testFile,test2File) #funçao definida no começo do programa.

if linhas_erradas==[]:print("Programa sem erros")
else:print("Os valores foram errados encontrados nas linhas onde n = {",", ".join(linhas_erradas),"}")