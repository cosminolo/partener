import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json
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
@anvil.server.callable
def bil_js(id,js):
  try:
    us_row = app_tables.lucru.get(user=id)
    us_row.update(js_bil=js)
  except:
    pass
pass
@anvil.server.callable
def get_bil(id):
  try:
      js=json.loads(app_tables.lucru.get(user=id)["js_bil"])
      return js
  except:
    pass

pass
 

