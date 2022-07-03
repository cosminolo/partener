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

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
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
  #js = anvil.server.call("j_g_gol")
  #jbal = anvil.server.call("bal_gol")
  #us_row = app_tables.lucru.get(user=id)
  #us_row.update(js_gen_gol=js, js_gen=js, bal=jbal ) 
  
pass

@anvil.server.callable
def app_new(id):
  try:
    id_row = app_tables.lucru.get(user=id)
    jsg = anvil.server.call("j_g_gol") 
    id_row.update(js_gen=jsg)    
    id_row.update(js_bil="")
    id_row.update(j_bil="")
    id_row.update(js_tva="")
    id_row.update(js_gen_gol=jsg) 
    jbal = anvil.server.call("bal_gol")
    id_row.update(bal=jbal)
    
  except:
    pass
pass

@anvil.server.callable
def tva_js(id,js):
  try:
    us_row = app_tables.lucru.get(user=id)
    us_row.update(js_tva=js)
  except:
    pass
pass
@anvil.server.callable
def get_tva(id):
  try:
      js=json.loads(app_tables.lucru.get(user=id)["js_tva"])
      return js
  except:
      pass
pass
@anvil.server.callable
def bil_js(id,js,a):
  try:
    if a == 1:
      us_row = app_tables.lucru.get(user=id)
      us_row.update(js_bil=js)
    if a == 2:
      us_row = app_tables.lucru.get(user=id)
      us_row.update(j_bil=js)
      time.sleep(1)
  except:
    pass
pass


@anvil.server.callable
def get_bil(id,a):
  try:
      if a == 1:
        js=json.loads(app_tables.lucru.get(user=id)["js_bil"])
        return js
      if a == 2:
        jst=json.loads(app_tables.lucru.get(user=id)["j_bil"]) 
        return jst
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
def prel_js_gol(id, tip):
  try:
      if tip == 1:
        js=app_tables.lucru.get(user=id)["js_gen_gol"]
        return js
      if tip == 2 :
        js=app_tables.lucru.get(user=id)["js_gen"]
        return js
  except:
    pass
pass
@anvil.server.callable
def upp_js(id,js):  
    id_row = app_tables.lucru.get(user=id)
    id_row.update(js_gen=js)
pass
@anvil.server.callable
def upp_bal(id,bal):  
    id_row = app_tables.lucru.get(user=id)
    id_row.update(bal=bal)
pass
@anvil.server.callable
def arh (us, dat, entit, facilit, j, bala):
  app_tables.arh.add_row(user=us,
                          soc=entit,
                          facilit=facilit,
                          dat=dat,
                          js_gen=j,
                          bal=bala)
pass
@anvil.server.callable
def arh2 (us, dat, entit, facilit):
  id_row = app_tables.lucru.get(user=us)  
  app_tables.arh.add_row(user=us,
                          soc=entit,
                          facilit=facilit,
                          dat=dat,
                          js_gen=id_row["js_gen"],
                          j_bil=id_row["j_bil"],
                          js_bil=id_row['js_bil'],
                          js_tva=id_row['js_tva'], 
                          bal=id_row['bal'],
                          rb=id_row['rb'])
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
  id_row.update(js_gen=arh["js_gen"], js_tva=arh["js_tva"], js_bil=arh['js_bil'], j_bil=arh['j_bil'], rb=arh['rb'])
  
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
def get_jsgen(id):
  try:    
    js=app_tables.lucru.get(user=id)["js_gen"]
    re = {"den": js["den"], "cui": js["cui"]}
    return re
  except:
    pass
pass
@anvil.server.callable
def s_rb(id,rb):  
    id_row = app_tables.lucru.get(user=id)
    id_row.update(rb=rb)
@anvil.server.callable
def get_rb(id):
  try:
    js=app_tables.lucru.get(user=id)["rb"]
    return js
  except:
    pass

