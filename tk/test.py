import tk.intp as intp
from tk.intp import *
Gui.__style__("test.css")
g = vars(intp)
pkg=["pack_start",True,True,0]
Win("root",[],
    Box("hbox",pkg,["orientation=Vars.hori"],
        Box("vbox1",pkg,["orientation=Vars.vert"],
            Btn("btn1",["label='btn1'"]),
        ),
        Box("vbox2",pkg,["orientation=Vars.vert"],
            Btn("btn2",["label='btn2'"]),
            Btn("btn3",["label='btn3'"]),
        )
    ),
)
def btn1_click(w):
    print("You clicked btn1")
g["btn1"].connect("clicked",btn1_click)
Gui.__run__(g["root"])