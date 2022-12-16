import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from pandas import DataFrame as pDF
def lerMedidas(medida:str):
    tabela = pDF([linhas.strip().split(',') for linhas in open('constants/'+medida+'.txt').readlines()])
    medidas = pDF(tabela[1].values,index=tabela[0].values,columns=['simbolo'])
    medidas.insert(1,'constante', [int(tabela[2][i])/int(tabela[3][i]) for i in range(len(tabela[1]))])
    return medidas

def lerPotencias():
    tabela = pDF([linhas.strip().split(',') for linhas in open('constants/potencias.txt').readlines()])
    medidas = pDF([[tabela[0][i],tabela[1][i]] for i in range(len(tabela[1]))],index=tabela[2].values,columns=['nome','simbolo'])
    medidas.insert(2,'exp10', [int(tabela[2][i]) for i in range(len(tabela[1]))])
    return medidas

class Unidade:
    def __init__(self, v, uc, e):
        self.valor = v
        self.const = uc
        self.exp = e

    def converter(self,u2, p2):
        prop = u2/self.const
        pot = p2-self.exp
        valor = self.valor*prop
        return Unidade(valor, u2, pot)

class BoraMofio: 
    def __init__(self):
    #   Gtk iniciadores
        self.builder = Gtk.Builder()
        self.builder.add_from_file("projeto.glade")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('janela')      
        self.window.show()

    #   unidades
        self.unitInput = self.builder.get_object('unit_in')
        self.unitOutput = self.builder.get_object('unit_out')

    #   ordem de grandeza   
        self.pows = lerPotencias()
        self.powInput = self.builder.get_object('pow_in')
        self.powOutput = self.builder.get_object('pow_out')

    #   valores
        self.numInput = self.builder.get_object('value_in')
        self.numOutput = self.builder.get_object('value_out')

    def distruiu(self, *args):Gtk.main_quit()
    
#   funcao para atualizar o setstore (usada para cada um dos 4 comboBox)
    def comboText(self,combo,store):
        combo.set_model(store)
        renderer_text = Gtk.CellRendererText()
        combo.pack_start(renderer_text, True)
        combo.add_attribute(renderer_text, "text", 1)

#   usada para setar as medidas a partir do tipo de medida selecionado em cima]
#       comprimento: metro, milha, polegada etc
    def mudou(self, box):
        unitType = box.get_active_text()
        self.liststore = Gtk.ListStore(str)
        self.units = lerMedidas(unitType.lower())
        for n in self.units.index.values:
            self.liststore.append([n.capitalize()])
        self.comboText(self.unitInput,self.liststore)
        self.comboText(self.unitOutput,self.liststore)

#   usada para setar as grandezas da entrada
#      metro: km, cm, μm etc
    def mudouUnitIn(self, box):
        unit = box.get_active_text()
        self.liststorePowI = Gtk.ListStore(str)
        for n in range(len(self.pows.index.values)):
            self.liststorePowI.append([self.pows.values[n][0]+self.units.loc[unit].iat[0]])
        self.comboText(self.powInput,self.liststorePowI)
#   usada de maneira similar para a saida
    def mudouUnitOut(self, box):
        unit = box.get_active_text()
        self.liststorePowO = Gtk.ListStore(str)
        for n in range(len(self.pows.index.values)):
            self.liststorePowO.append([self.pows.values[n][0]+self.units.loc[unit].iat[0]])
        self.comboText(self.powOutput,self.liststorePowO)
    
    #   funcao para converter os valores
    def converte(self, botao):
        valor = float(self.numInput.get_text())

        print(self.unitInput.get_active())

        unitconstIn = self.units.loc[self.unitInput.get_active_text()].iat[1]
        unitconstOut = self.units.loc[self.unitOutput.get_active_text()].iat[1]

        expoIn = int(self.pows.values[self.powInput.get_active()][1])
        expoOut = int(self.pows.values[self.powOutput.get_active()][1])

        a = Unidade(valor,unitconstIn,expoIn)
        valorOut = a.converter(unitconstOut, expoOut)

        self.numOutput.set_text(str(valorOut))

ligar = BoraMofio()
Gtk.main()