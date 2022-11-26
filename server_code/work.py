import anvil.server
import json
import requests
import xmltodict
import pandas as pd
from requests.structures import CaseInsensitiveDict
from pandas import json_normalize
from openpyxl import load_workbook
@anvil.server.callable
def pri_ini(tip):
  if tip =="a":
    j = {}
    j = {
    "gen":{"cui": "", "name": "", "codj": "", "adress": "", "tel": "", "email": "", "caen": "", "d_caen": "", "tip": "", 
    "ramura": "", "cereale": "NU", "reprez": "", "calit":"", "rel_spec":"NU"}, "facilitate": {"fel": "", "denumit": "", "suma": "", "valuta": "", "per": "", "md_ramb": "", "dest": "", "per_g": "", "per_t": ""}, "garantii": [], "admin":[], "asoc":[], "grp":[],
     "d_manag": [], "sintez":{"piata":"", "concurenta":"", "strategia":"", "conducere":"", "ev_manag":"", "cal_act":"", "con_cli":"", "exp_imp":"", "nr_sal": "0", "altele": ""}, "exp_bc":[], "exp_l": [],
    "decl": {"a":"", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"Da", "i":"", "j":"", "k":""},
    "buget":{"nume":"", "cui":"", "bs":"", "bss":"", "bas":"", "bass":"", "total":"", "obs":"", "datav":""}, "tva":{"cui":"", "scpTVA":"", "data_inceput_ScpTVA": "",
    "statusRO_e_Factura":"", "statusInactivi":"", "statusTvaIncasare":"", "dataInceputTvaInc":"", "statusSplitTVA":"", "dataInceputSplitTVA":"", "mesaj_ScpTVA":"", "data":""},
    "litigii":{}, "bil":{}, "data_fin":{"d1":"", "d2":"", "d3":""}, "iv":{'r':{'r1':"NU", 'r2':"NU", 'r3':"NU"}, "a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0},
     "d":{"a1":0, "a2":0, "a3":0}}, "cd":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0},
     "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}, "f":{"a1":0, "a2":0, "a3":0}, "g":{"a1":0, "a2":0, "a3":0}, "h":{"a1":0, "a2":0, "a3":0}, "i":{"a1":0, "a2":0, "a3":0}},
     "sf":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0}, "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}}, "dt":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0},
     "c":{"a1":0, "a2":0, "a3":0}, "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}, "f":{"a1":0, "a2":0, "a3":0}, "g":{"a1":0, "a2":0, "a3":0}, "h":{"a1":0, "a2":0, "a3":0}, "i":{"a1":0, "a2":0, "a3":0},
     "j":{"a1":0, "a2":0, "a3":0}, "k":{"a1":0, "a2":0, "a3":0}, "l":{"a1":0, "a2":0, "a3":0}, "m":{"a1":0, "a2":0, "a3":0}, "n":{"a1":0, "a2":0, "a3":0}, "o":{"a1":0, "a2":0, "a3":0}, "p":{"a1":0, "a2":0, "a3":0},
     "r":{"a1":0, "a2":0, "a3":0}, "s":{"a1":0, "a2":0, "a3":0}, "t":{"a1":0, "a2":0, "a3":0}, "u":{"a1":0, "a2":0, "a3":0}, "v":{"a1":0, "a2":0, "a3":0}}}
    return j
  if tip =="b":
    k={}
    k = {"crit":{"a":True, "b":True, "c":True, "d":True, "e":True, "f":True, "g":True, "h":True, "i":True, "j":True, "k":True, "l":True, "m":True, "n":True},
    "ar":{"tip":"", "sum_lei":0, "per":0, "perf":"", "l1":0, "l2":0, "l3":0, "l4":0, "l5":0, "l6":0, "l7":0, "l8":0, "l9den":" nealocat", "l9val":0, "l10den":"nealocat", "l10val":0, "l11den":"nealocat", "l11val":0, "comb_den":"", "comb_val":"",
    "p1":"", "p2":"", "p3":"", "p4":"", "p5":"", "p6":"", "p1r":"", "p2r":"", "p3r":"", "p4r":"", "p5r":"", "p6r":""}} 
    return k
@anvil.server.callable  
def conv(file):
    #with anvil.media.TempFile(file) as filename:
    df = pd.read_excel(file, sheet_name = 'BALANTA_PJ2021', skiprows = 0,  nrows= 566, usecols = 'A:L')
    print(df)

    #print('Excel Sheet to JSON:\n', json_str)