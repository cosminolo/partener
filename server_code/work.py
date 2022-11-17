import anvil.server
import json
import requests
import xmltodict
import pandas
from requests.structures import CaseInsensitiveDict
from pandas import json_normalize
from openpyxl import load_workbook
@anvil.server.callable
def pri_ini(tip):
  if tip =="a":
    j = {}
    j = {
    "gen":{"cui": "", "name": "", "codj": "", "adress": "", "tel": "", "email": "", "caen": "", "d_caen": "", "tip": "", 
    "ramura": " ", "cereale": "", "reprez": "", "calit":"", "rel_spec":""}, "facilitate": {"fel": "", "denumit": "", "suma": "", "valuta": "", "per": "", "md_ramb": "", "dest": "", "per_g": "", "per_t": ""}, "garantii": [], "admin":[], "asoc":[], "grp":[],
     "d_manag": [], "sintez":{"piata":" ", "concurenta":" ", "strategia":" ", "conducere":" ", "ev_manag":" ", "cal_act":" ", "con_cli":" ", "exp_imp":" ", "nr_sal": "", "altele": ""}, "exp_bc":[], "exp_l": [],
    "decl": {"a":"", "b":"", "c":"", "d":"", "e":"", "f":"", "g":"", "h":"", "i":"", "j":"", "k":""},
    "buget":{"nume":"", "cui":"", "bs":"", "bss":"", "bas":"", "bass":"", "total":"", "obs":"", "datav":""}, "tva":{"cui":"", "scpTVA":"", "data_inceput_ScpTVA": "",
    "statusRO_e_Factura":"", "statusInactivi":"", "statusTvaIncasare":"", "dataInceputTvaInc":"", "statusSplitTVA":"", "dataInceputSplitTVA":"", "mesaj_ScpTVA":"", "data":""},
    "litigii":{}, "bil":{}, "data_fin":{"d1":"", "d2":"", "d3":""}, "iv":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0},
     "d":{"a1":0, "a2":0, "a3":0}}, "cd":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0},
     "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}, "f":{"a1":0, "a2":0, "a3":0}, "g":{"a1":0, "a2":0, "a3":0}, "h":{"a1":0, "a2":0, "a3":0}, "i":{"a1":0, "a2":0, "a3":0}},
     "sf":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0}, "c":{"a1":0, "a2":0, "a3":0}, "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}}, "dt":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"a1":0, "a2":0, "a3":0},
     "c":{"a1":0, "a2":0, "a3":0}, "d":{"a1":0, "a2":0, "a3":0}, "e":{"a1":0, "a2":0, "a3":0}, "f":{"a1":0, "a2":0, "a3":0}, "g":{"a1":0, "a2":0, "a3":0}, "h":{"a1":0, "a2":0, "a3":0}, "i":{"a1":0, "a2":0, "a3":0},
     "j":{"a1":0, "a2":0, "a3":0}, "k":{"a1":0, "a2":0, "a3":0}, "l":{"a1":0, "a2":0, "a3":0}, "m":{"a1":0, "a2":0, "a3":0}, "n":{"a1":0, "a2":0, "a3":0}, "o":{"a1":0, "a2":0, "a3":0}, "p":{"a1":0, "a2":0, "a3":0},
     "r":{"a1":0, "a2":0, "a3":0}, "s":{"a1":0, "a2":0, "a3":0}, "t":{"a1":0, "a2":0, "a3":0}, "u":{"a1":0, "a2":0, "a3":0}, "v":{"a1":0, "a2":0, "a3":0}}}
    return j
  if tip =="b":
    k={}
    k = {"crit":{"a":False, "b":False, "c":False, "d":False, "e":False, "f":False, "g":False, "h":False, "i":False, "j":False, "k":False, "l":False, "m":False, "n":False}} 
    return k
@anvil.server.callable  
def conv(file):
    with anvil.media.TempFile(file) as filename:
      wb = load_workbook(filename, read_only=False, keep_vba=True)

    #print('Excel Sheet to JSON:\n', json_str)