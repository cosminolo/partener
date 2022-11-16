import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
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
    file = anvil.server.call("down_declaratii")
    id_row.update(darh=file)
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








