import gi, os
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GLib, GObject

#variables
class Vars():
    vert = Gtk.Orientation.VERTICAL
    hori = Gtk.Orientation.HORIZONTAL
    pks = ["pack_start",True,True,0]
    pke = ["pack_end",True,True,0]
    scrW = Gdk.Screen().get_default().get_width()
    scrH = Gdk.Screen().get_default().get_height()
    perCent = Gtk.Adjustment(0, 0, 100, 1, 10, 0)


# widgets
class Win():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.Window({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class Btn():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.Button({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class TBtn():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.ToggleButton({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class HeaderBar():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.HeaderBar({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class SE():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.SearchEntry({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class Label():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.Label({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class VolBtn():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.VolumeButton({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]
class Scale():
    def __new__(self,id:str,param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.Scale({params})')
        for i in args:
            globals()[id].add(i)
        return globals()[id]

# layouts
class Box():
    def __new__(self,id:str,pkg:list=[],param:list=[],*args):
        params=""
        for i in param:
            params+=i+","
        exec(f'globals()["{id}"] = Gtk.Box({params})')

        for i in args:
            exec(f'globals()["{id}"].{pkg[0]}(i,pkg[1],pkg[2],pkg[3])')
        return globals()[id]

# misc
class Gui():
    def __run__(obj):
        obj.show_all()
        obj.connect("destroy",exit)
        Gtk.main()
    def __style__(file:str):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        provider.load_from_path(file)

if __name__ == "__index__":
    os.system("test.py")