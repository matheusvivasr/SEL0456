import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Pagina:
    '''The Application Class.'''

    def __init__(self,fileName):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(fileName)

        self.window = self.builder.get_object('window')

        self.liststore = Gtk.ListStore(str, str)