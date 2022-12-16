tipos = ['Comprimento','Tempo']
unidades = [['Metro','Milha','Jarda','Pé'],['Segundo','Minuto','Hora','Dia','Mês','Ano']]
razoes = [[[1,1],[1,1609],[1094,1000],[3281,1000]],[[60,1],[1,1],[1,60],[1,1440],[1,43800],[1,525600]]]

def converter(tp, unIn, unOut, valor):
    valor = float(valor.replace(',','.'))
    p,q = razoes[tp][unIn]
    constIn = p/q
    p,q = razoes[tp][unOut]
    constOut = p/q
    val = round(valor*constOut/constIn,3)
    return str(val).replace('.',',')