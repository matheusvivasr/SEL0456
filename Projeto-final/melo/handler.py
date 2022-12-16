from gi import require_version as Gtk_version
Gtk_version("Gtk", "3.0")

from gi.repository import Gtk
import functions as f

def ligar():
    ligar = Handler()
    Gtk.main()

temp = ['Celcius','Kelvin','Fahrenheit']
press = ['Pascal','Atmosfera','Bar','Torr','Psi']


class Handler:
    def __init__(self):
    #   Gtk iniciadores
        self.builder = Gtk.Builder()
        fileName = 'conversor.glade'
        self.builder.add_from_file(fileName)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('janela')  
        self.window.show()

        self.boxTipo1 = self.builder.get_object('type1') 
        self.boxTipo2 = self.builder.get_object('type2') 
        self.input = self.builder.get_object('input') 
        self.output = self.builder.get_object('output')


        self.boxEscolha = self.builder.get_object('choice') 



    def destruir(self, *args):Gtk.main_quit()

#   quando selecionar o tipo, seta as escolhas de unidade no input
#   sinal do 'choice' para alterar o 'type1'

    def setarInput(self,box):
        self.input.set_text('')
        self.output.set_text('')
        self.boxTipo2.set_active(-1)
        listenerI = Gtk.ListStore(str)

        if box.get_active_text() == 'Temperatura': unidades = temp
        elif box.get_active_text() == 'Pressão': unidades = press

        for u in unidades: listenerI.append([u])

        self.boxTipo1.set_model(listenerI)
        renderer_text = Gtk.CellRendererText()
        self.boxTipo1.pack_start(renderer_text, True)
        self.boxTipo1.add_attribute(renderer_text, "text", 1)
        self.boxTipo1.set_active(-1)
        self.boxTipo2.set_model(listenerI)
        renderer_text = Gtk.CellRendererText()
        self.boxTipo2.pack_start(renderer_text, True)
        self.boxTipo2.add_attribute(renderer_text, "text", 1)
        self.boxTipo2.set_active(-1)

#   converter as unidades
    def apertar(self,botao):
        sett = self.boxEscolha
        
        num = self.input.get_text()
        
        inputType = self.boxTipo1.get_active_text()
        outputType = self.boxTipo2.get_active_text()

        if sett.get_active_text() =='Temperatura':
            aIn = temp.index(inputType)
            aOut = temp.index(outputType)

            if aIn == 0:
                valor = f.tratarNum(num)
            elif aIn == 1:
                valor = f.kelCelcius(num)
            elif aIn == 2:
                valor = f.farCelcius(num)

            if aOut == 1:
                valor = f.celciusK(num)
            elif aOut == 2:
                valor = f.celciusFar(num)
            else:
                valor = f.tratarNum(num)

        elif sett.get_active_text() == 'Pressão':
            valor = f.pressoes(num, inputType,outputType)
            
        valor = f.numOut(valor)
        self.output.set_text(valor)