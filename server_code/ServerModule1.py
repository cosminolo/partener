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
 
 for user in app_tables.lucru.search(tables.order_by("user")):
  break
 else:
  app_tables.lucru.add_row(user=id)
  js = anvil.server.call("j_g_gol")
  us_row = app_tables.lucru.get(user=id)
  us_row.update(js_gen_gol=js, js_gen=js ) 
pass

@anvil.server.callable
def app_new(id):
  try:
    js=app_tables.lucru.get(user=id)["js_gen_gol"]
    id_row = app_tables.lucru.get(user=id)
    id_row.update(js_gen=js)
    id_row.update(js_bil="")
    id_row.update(j_bil="")
    id_row.update(js_tva="")
  except:
    app_tables.lucru.add_row(user=id)
    js = anvil.server.call("j_g_gol")
    us_row = app_tables.lucru.get(user=id)
    us_row.update(js_gen_gol=js, js_gen=js ) 
    us_row.update(js_bil="")
    us_row.update(j_bil="")
    us_row.update(js_tva="")
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
  #try:
    if a == 1:
      us_row = app_tables.lucru.get(user=id)
      us_row.update(js_bil=js)
    if a == 2:
      us_row = app_tables.lucru.get(user=id)
      us_row.update(j_bil=js)
      time.sleep(1)
  #except:
   # pass
pass


@anvil.server.callable
def get_bil(id,a):
  #try:
      if a == 1:
        js=json.loads(app_tables.lucru.get(user=id)["js_bil"])
        return js
      if a == 2:
        jst=json.loads(app_tables.lucru.get(user=id)["j_bil"]) 
        return jst
  #except:
   # pass
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
def arh (us, dat, entit, facilit, j):
  app_tables.arh.add_row(user=us,
                          soc=entit,
                          facilit=facilit,
                          dat=dat,
                          js_gen=j)
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
  js = app_tables.arh.get(user=us, soc=soc,facilit=facilit, dat=dat)["js_gen"]
  id_row = app_tables.lucru.get(user=us)
  id_row.update(js_gen=js)
pass
@anvil.server.callable
def sterge_arh(us, soc, facilit, dat):
 id_row = app_tables.arh.get(user=us, soc=soc,facilit=facilit, dat=dat)
 if id_row is not None:
  id_row.delete()
pass



