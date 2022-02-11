import os, re

def read(file:str):
    with open(file,"r") as ctn:
        return ctn.read().replace("\n","").replace("    ","")
def find(ctn:str,obj:str,prop:str) -> str:
    obj_ctn=re.findall(f"{obj}\[.*\]",ctn)[0]
    for line in obj_ctn.split(";"):
        obj_ctn2=re.findall(f"{prop}:.*",line)
        if len(obj_ctn2)>0:
            obj_ctn3=obj_ctn2[0].replace(f"{prop}:","")
            return obj_ctn3
if __name__=="__main__":
    os.system("python3 test.py")