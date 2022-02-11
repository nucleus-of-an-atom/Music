# imports
import sys,os
sys.path.append("../")
from conf.conf import *
from tk import intp as intp
from tk.intp import *
sys.path.remove("../")
# func
def list_song():
    conf_thing=find(read("config.conf"),"files","type")
    songs2=os.popen(f"ls ~/Music | grep {conf_thing}").read().split("\n")
    songs2.remove(songs2[-1])
    return songs2
def search_song(name):
    songs2=os.popen(f"ls ~/Music | grep '{name}'").read().split("\n")
    songs2.remove(songs2[-1])
    for wid in g["list"].get_children():
        g["list"].remove(wid)
    g["root"].resize(1,1)
    add_btns=[]
    for song in songs2:
        add_btn=TBtn("",["label='Add'"])
        add_btns.append(add_btn)
        g["list"].pack_start(
            Box(f"{song}_box",["pack_start",True,True,0],['orientation=Vars.hori','spacing=10'],
                Label(song,[f'label="{song}"']),
                add_btn
            ),
        True,True,0)
        if os.popen("mpc playlist").read().split("\n").count(song)>0:
            add_btn.set_active(True)
            add_btn.set_label("Rmv")
        add_btn.connect("toggled",add_song)
    g["root"].show_all()
    return songs2
def add_song(w):
    btn_x=w.get_parent().get_children()[0]
    btn_y=w.get_parent().get_children()[1]
    btn_t=btn_x.get_label()
    if w.get_active():
        btn_y.set_label("Rmv")
        os.system(f"mpc add {btn_t}")
    else:
        btn_y.set_label("Add")
        songs=os.popen("mpc playlist").read().split("\n")
        songs=list(filter((btn_t).__ne__, songs))
        songs.remove(songs[-1])
        os.system("mpc clear")
        for song in songs:
            os.system(f"mpc add {song}")
        if g["home"].get_active():
            home_songs(g["home"])
#misc
pkg=["pack_start",True,False,0]
g=vars(intp)

#gui
Gui.__style__("style.css")
HeaderBar("hb",[])
Box("hbhbox",pkg,["orientation=Vars.hori","spacing=10"],
    TBtn("home",["label='Home'"]),
    TBtn("all",["label='All Songs'"])
)
Win("root",[],
    Box("vbox",pkg,["orientation=Vars.vert"],
        Box("tools",["pack_start",True,True,0],["orientation=Vars.hori","spacing=10"],
            Btn("prev",["label='⏮'"]),
            TBtn("play",["label='►'"]),
            Btn("next",["label='⏭'"]),
            TBtn("repeat",["label='𝄇'"])
        ),
        Box("list",pkg,["orientation=Vars.vert","spacing=10"]),
    ),
)
SE("search",[])
Scale("seek",[])
g["vbox"].pack_end(g["search"],True,False,0)
g["vbox"].pack_end(g["seek"],True,False,0)
# func 2.0
def search_actv(*args):
    w = args[0]
    x=search_song(w.get_text())
def all_songs(w):
    if w.get_active()==True:
        for wid in g["list"].get_children():
            g["list"].remove(wid)
        g["root"].resize(1,1)
        g["home"].set_active(False)
        songs=list_song()
        add_btns=[]
        for song in songs:
            add_btn=TBtn("",["label='Add'"])
            add_btns.append(add_btn)
            g["list"].pack_start(
                Box(f"{song}_box",["pack_start",True,True,0],['orientation=Vars.hori','spacing=10'],
                    Label(song,[f'label="{song}"']),
                    add_btn
                ),
            True,True,0)
            if os.popen("mpc playlist").read().split("\n").count(song)>0:
                add_btn.set_active(True)
                add_btn.set_label("Rmv")
            add_btn.connect("toggled",add_song)
        g["root"].show_all()
    else:
        for wid in g["list"].get_children():
            g["list"].remove(wid)
        g["root"].resize(1,1)
def home_songs(w):
    if w.get_active()==True:
        for wid in g["list"].get_children():
            g["list"].remove(wid)
        g["root"].resize(1,1)
        g["all"].set_active(False)
        songs=os.popen("mpc playlist").read().split("\n")
        songs.remove(songs[-1])
        add_btns=[]
        for song in songs:
            add_btn=TBtn("",["label='Rmv'"])
            add_btns.append(add_btn)
            g["list"].pack_start(
                Box(f"{song}_box",["pack_start",True,True,0],['orientation=Vars.hori','spacing=10'],
                    Label(song,[f'label="{song}"']),
                    add_btn
                ),
            True,True,0)
            add_btn.set_active(True)
            add_btn.connect("toggled",add_song)
        g["root"].show_all()
    else:
        for wid in g["list"].get_children():
            g["list"].remove(wid)
        g["root"].resize(1,1)
def prev(w):
    os.system("mpc prev")
def play_pause(w):
    if w.get_active():
        os.system("mpc play")
        w.set_label("⏸")
    else:
        os.system("mpc pause")
        w.set_label("►")
def next(w):
    os.system("mpc next")
isToUpd=True
def upd_pos():
    global isToUpd
    isToUpd=False
    val=float(os.popen("mpc").read().split("\n")[1].split("(")[1].split(")")[0].replace("%",""))
    g["seek"].set_value(val)
    return True
def upd_seek(w):
    global isToUpd
    if isToUpd:
        seek(w)
    else:
        isToUpd=True
def seek(w):
    time_val=float(w.get_value()).__round__(4)
    os.system(f"mpc seek {time_val}%")
def loop_de_loop(w):
    if w.get_active:
        os.system("mpc repeat on")
    else:
        os.system("mpc repeat off")
def init_f():
    if os.popen("mpc").read().split("\n")[1].split("[")[1].split("]")[0].replace("%","")=='playing':
        g["play"].set_active(True)
        g["play"].set_label("⏸")
    else:
        g["play"].set_active(False)
GLib.timeout_add_seconds(1,upd_pos)
init_f()
g["repeat"].connect("toggled",loop_de_loop)
g["seek"].set_draw_value(False)
g["seek"].set_adjustment(Vars.perCent)
g["seek"].connect("value-changed", upd_seek)
g["prev"].connect("clicked",prev)
g["next"].connect("clicked",next)
g["play"].connect("toggled",play_pause)
g["all"].connect("toggled",all_songs)
g["all"].set_active(True)
g["home"].connect("toggled",home_songs)
g["hb"].set_custom_title(g["hbhbox"])
g["root"].set_titlebar(g["hb"])
g["root"].set_size_request(200,1)
g["search"].set_placeholder_text("Search")
g["search"].connect("activate",search_actv)
Gui.__run__(g["root"])
