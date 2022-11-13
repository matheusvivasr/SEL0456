def substituir(texto):
    modificado = ","

    dentro = False
    frase = list(texto)

    #https://regex101.com/
    # ^ da pra fazer pelo regex ^

    for indice in range(len(frase)):        
        if frase[indice] == '"' and not dentro:
            dentro = True
        elif indice == '"' and dentro:
            dentro = False
        
        if frase[indice] == modificado and not dentro:
            frase[indice] = ';'

    out = ''.join(frase)

    return out


with open("in.txt", "r") as entrada:
    caracteres = entrada.read()
        
texto_modificado = substituir(caracteres)

with open("out.txt", "w") as saida:
    saida.write(texto_modificado)
