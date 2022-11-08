import anvil.server
import json
import requests
import xmltodict
from requests.structures import CaseInsensitiveDict
from pandas import json_normalize

@anvil.server.callable
def pri_ini():
 j = {}
 j = {
    "gen":{"cui": "", "name": "", "codj": "", "adress": "", "tel": "", "email": "", "caen": "", "d_caen": "", "tip": "", 
    "ramura": " ", "cereale": "", "reprez": ""}, "facilitate": {"fel": "", "denumit": "", "suma": "", "valuta": "", "per": "", "md_ramb": "", "dest": "", "per_g": "", "per_t": ""}, "garantii": [], "admin":[], "asoc":[], "grp":[],
     "d_manag": [], "sintez":{"piata":" ", "concurenta":" ", "strategia":" ", "conducere":" ", "ev_manag":" ", "cal_act":" ", "con_cli":" ", "exp_imp":" ", "nr_sal": "", "altele": ""}, "exp_bc":[], "exp_l": [],
    "decl": {"a":"", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":""},
    "buget":{"nume":"", "cui":"", "bs":"", "bss":"", "bas":"", "bass":"", "total":"", "obs":"", "datav":""}, "tva":{"cui":"", "scpTVA":"", "data_inceput_ScpTVA": "",
    "statusRO_e_Factura":"", "statusInactivi":"", "statusTvaIncasare":"", "dataInceputTvaInc":"", "statusSplitTVA":"", "dataInceputSplitTVA":"", "mesaj_ScpTVA":"", "data":""},
    "litigii":{}, "bil":{}, "iv":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0},
     "d":{"a1":0, "a2":0, "a3":0}}, "cd":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0},
     "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}, "f":{"a1":0, "a2":0, "a3":0}, "g":{"a1":0, "a2":0, "a3":0}, "h":{"a1":0, "a2":0, "a3":0}, "i":{"a1":0, "a2":0, "a3":0}},
     "sf":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0}, "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}}, "tg":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0},
     "c":{"a1":0, "a2":0, "a3":0}, "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}, "f":{"a1":0, "a2":0, "a3":0}, "g":{"a1":0, "a2":0, "a3":0}, "h":{"a1":0, "a2":0, "a3":0}, "i":{"a1":0, "a2":0, "a3":0},
     "j":{"a1":0, "a2":0, "a3":0}, "k":{"a1":0, "a2":0, "a3":0}, "l":{"a1":0, "a2":0, "a3":0}, "m":{"a1":0, "a2":0, "a3":0}, "n":{"a1":0, "a2":0, "a3":0}, "o":{"a1":0, "a2":0, "a3":0}, "p":{"a1":0, "a2":0, "a3":0},
     "r":{"a1":0, "a2":0, "a3":0}, "s":{"a1":0, "a2":0, "a3":0}, "t":{"a1":0, "a2":0, "a3":0}, "u":{"a1":0, "a2":0, "a3":0}, "v":{"a1":0, "a2":0, "a3":0}}}
 return j

