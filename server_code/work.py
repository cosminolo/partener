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
    "litigii":{}, "bil":{}, "iv":{"a":{"a1":0, "a2":0, "a3":0}, "b":{"b1":0, "b2":0, "b3":0}, "c":{"c1":0, "c2":0, "c3":0},
     "d":{"d1":0, "d2":0, "d3":0}}, "cd":{"a":{"a1":0, "a2":0, "a3":0}}}
 return j

