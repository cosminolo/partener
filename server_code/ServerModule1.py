import anvil.stripe
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
import time
from io import BytesIO
@anvil.server.callable
def add_user(id):
 id_row = app_tables.lucru.get(user=id)
 if id_row:
  pass
 #for user in app_tables.lucru.search(tables.order_by("user")):
  #break
 else:
  app_tables.lucru.add_row(user=id)
  anvil.server.call("new_us", id)  
pass
@anvil.server.callable
def app_new(id):
  try:
    id_row = app_tables.lucru.get(user=id)
    jsg = anvil.server.call("pri_ini","a") 
    jar = anvil.server.call("pri_ini","b") 
    jbal = anvil.server.call("bal_gol") 
    id_row.update(p1=jsg)    
    id_row.update(bal=jbal)    
    id_row.update(ar=jar)
    file =anvil.server.call ("down_declaratii")
    id_row.update(darh=file)
    file =anvil.server.call ("down_declaratii")
    id_row.update(farh=file)
  except:
    pass
pass
@anvil.server.callable
def get_bal(id):
  try:    
    js=app_tables.lucru.get(user=id)["bal"]
    return js
  except:
    pass
pass

@anvil.server.callable
def upp_bal(id,bal):  
    id_row = app_tables.lucru.get(user=id)
    id_row.update(bal=bal)
pass
@anvil.server.callable
def arh2 (us, dat, entit, facilit):
  id_row = app_tables.lucru.get(user=us)  
  app_tables.arh.add_row(user=us,
                          soc=entit,
                          facilit=facilit,
                          dat=dat,
                          p1=id_row["p1"],                          
                          bal=id_row['bal'],     
                          darh=id_row['darh'],
                          farh=id_row['farh'],
                          ar=id_row['ar'])   
pass
@anvil.server.callable
def nr_rows(us):
  nr = len(app_tables.arh.search(user=us))
  return nr
pass
@anvil.server.callable
def sele_us(us):
  result = [
        {
            "soc": row['soc'],
            "facilit": row['facilit'],
            "dat":row['dat'],
        }
        for row in app_tables.arh.search(user=us)
    ]
  return result
pass
@anvil.server.callable
def preia_inlucru(us, soc, facilit, dat):
  arh = app_tables.arh.get(user=us, soc=soc,facilit=facilit, dat=dat)
  id_row = app_tables.lucru.get(user=us)
  id_row.update(p1=arh['p1'], bal=arh['bal'], ar=arh['ar'])
  media = arh['darh']
  media = anvil.BlobMedia('arhiva.zip', media.get_bytes())
  id_row.update(darh=media)
  media = arh['farh']
  media = anvil.BlobMedia('arhiva_fin.zip', media.get_bytes())
  id_row.update(farh=media)
  
  #media = report['media']
  #media = anvil.BlobMedia('text/html', media.get_bytes() )
  
pass
@anvil.server.callable
def sterge_arh(us, soc, facilit, dat):
 id_row = app_tables.arh.get(user=us, soc=soc,facilit=facilit, dat=dat)
 if id_row is not None:
  id_row.delete()
pass
@anvil.server.callable
def apl(id):
  fl = anvil.server.call("apl_gol")  
  us_row = app_tables.lucru.get(user=id)
  us_row.update(apl_x=fl) 
  return fl 
pass
@anvil.server.callable
def sp1(id,p1):
  try:
    us_row = app_tables.lucru.get(user=id)
    us_row.update(p1=p1)
  except:
    pass
pass
@anvil.server.callable
def get_p1(id):
  try:    
    p1=app_tables.lucru.get(user=id)["p1"]
    return p1
  except:
    pass
pass
@anvil.server.callable
def upld(id, file):
    us_row = app_tables.lucru.get(user=id)
    us_row.update(darh=file)
pass
@anvil.server.callable
def uplf(id, file):
    us_row = app_tables.lucru.get(user=id)
    us_row.update(farh=file)
pass
@anvil.server.callable
def get_crit(id):
  try:    
    c1=app_tables.lucru.get(user=id)["ar"]
    return c1
  except:
    pass
pass
@anvil.server.callable
def upc(id,c1):
  try:
    us_row = app_tables.lucru.get(user=id)
    us_row.update(ar=c1)
  except:
    pass
pass

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
  pass







