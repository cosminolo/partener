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
    "ramura": " ", "cereale": "", "reprez": ""}, "facilitate": {"fel": "", "denumit": "", "suma": "", "valuta": "", "per": "", "garantii": "", "dest": ""}, "admin":[], "asoc":[], "grp":[],
    "sintez":{"piata":" ", "concurenta":" ", "strategia":" ", "conducere":" ", "ev_manag":" ", "cal_act":" ", "con_cli":" ", "exp_imp":" ", "nr_sal": "", "altele": ""},
    "buget":{"nume":"", "cui":"", "bs":"", "bss":"", "bas":"", "bass":"", "total":"", "obs":"", "datav":""}, "tva":{"cui":"", "scpTVA":"", "data_inceput_ScpTVA": "",
    "statusRO_e_Factura":"", "statusInactivi":"", "statusTvaIncasare":"", "dataInceputTvaInc":"", "statusSplitTVA":"", "dataInceputSplitTVA":"", "mesaj_ScpTVA":"", "data":""},
    "litigii":{}, "bil":{}}
 return j

