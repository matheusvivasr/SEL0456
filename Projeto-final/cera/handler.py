
from gi import require_version as Gtk_version
Gtk_version("Gtk", "3.0")

from gi.repository import Gtk
import funcoes as f

def ligar(nome):
    ligar = Handler(nome)
    Gtk.main()



class Handler:
    def __init__(self,name:str):
    #   Gtk iniciadores
        self.builder = Gtk.Builder()
        fileName = name+'.glade'
        self.builder.add_from_file(fileName)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('window')  
        self.window.show()

        self.boxEscolha = self.builder.get_object('grandeza')
        self.boxTipo1 = self.builder.get_object('unidade1') 
        self.boxTipo2 = self.builder.get_object('unidade2') 
        self.input = self.builder.get_object('entrada') 
        self.output = self.builder.get_object('saida')

    def destroy(self, *args):Gtk.main_quit()

    def tipoEscolhido(self,box):
        self.input.set_text('')
        self.output.set_text('')
        self.boxTipo2.set_active(-1)

        renderer_text = Gtk.CellRendererText()
        listener = Gtk.ListStore(str)

        tipo = f.tipos.index(box.get_active_text())
        for unidade in f.unidades[tipo]: listener.append([unidade])

        boxs = [self.boxTipo1,self.boxTipo2]

        for xbox in boxs:
            xbox.set_model(listener)
            xbox.pack_start(renderer_text, True)
            xbox.add_attribute(renderer_text, "text", 1)
            xbox.set_active(-1)

    def converter(self,botao):
        t = f.tipos.index(self.boxEscolha.get_active_text())
        uIn = f.unidades[t].index(self.boxTipo1.get_active_text())
        uOut = f.unidades[t].index(self.boxTipo2.get_active_text())
        num = self.input.get_text()
        self.output.set_text(f.converter(t, uIn, uOut, num))


    def pressed(self,botao):
    #   converter as unidades
        pass