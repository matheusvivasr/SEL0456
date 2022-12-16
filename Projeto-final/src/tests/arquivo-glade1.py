import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()

class Handler:
    def destruiu(self, *args):
        Gtk.main_quit()

    def aperto(self, botao):
        print("apertou aqui em!")

builder.add_from_file("arquivo-glade1.glade")
builder.connect_signals(Handler())

janelinha = builder.get_object("janela")
janelinha.show_all()

Gtk.main()