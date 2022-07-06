import anvil.server
import json
import requests
import xmltodict
from requests.structures import CaseInsensitiveDict
from pandas import json_normalize
@anvil.server.callable
def js_ini():
 j = {}
 j = {
    "tip":"SRL", "credit":" ", "facilit":" ", "suma":0, "valut":"Lei", "cui":" ", "den":" ", "sediu": "", "onrc":" ", "caen":" ",
    "ramura":" ", "cereale":"NU", "descriere":" ", "asociati":" ", "admin":" ", "nrsal":"0", "telef":" ", "soc_grup":" ",
    "piata":" ", "concurenta":" ", "strategia":" ", "conducere":" ", "ev_manag":" ", "cal_act":" ", "con_cli":" ", "exp_imp":" ",
    "buget":{"nume":"", "cui":"", "bs":"", "bss":"", "bas":"", "bass":"", "total":"", "obs":""}}
 return j
@anvil.server.callable
def pri_ini():
 j = {}
 j = {
    "gen":{"cui": "", "name": "", "codj": "", "adress": "", "tel": "", "email": "", "caen": "", "d_caen": "", "tip": "S.R.L.", 
    "ramura":" ", "cereale":"NU"}, "admin":[], "asoc_pf":[], "asoc_pj":[], "grup":[],
    "sintez":{"piata":" ", "concurenta":" ", "strategia":" ", "conducere":" ", "ev_manag":" ", "cal_act":" ", "con_cli":" ", "exp_imp":" "},
    "buget":{"nume":"", "cui":"", "bs":"", "bss":"", "bas":"", "bass":"", "total":"", "obs":""}}
 return j

