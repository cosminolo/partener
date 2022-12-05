import anvil.email
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
def sentem(us, soc,facilit, dat):  
   sb = soc + " - " + facilit
   tx = "Trimis de: " + us
   #la = "cosmin.ologeanu2017@gmail.com"
   la = "cosmin.ologeanu@cec.ro" 
   arh = app_tables.arh.get(user=us, soc=soc,facilit=facilit, dat=dat)
   media1 = arh['darh']
   media2 = arh['farh']
   anvil.email.send(from_name="Partener", 
    to= la, 
    subject= sb,
    text= tx,                
    attachments=[media1, media2]) 
   return la
pass
#@anvil.server.callable
#def clr_ar(id):
  #c1=app_tables.lucru.get(user=id)["ar"]
  #cc = {"ar":{"tip":"", "sum_lei":0, "per":0, "perf":"", "l1":0, "l2":0, "l3":0, "l4":0, "l5":0, "l6":0, "l7":0, "l8":0, "l9den":" nealocat", "l9val":0, "l10den":"nealocat", "l10val":0, "l11den":"nealocat", "l11val":0, "comb_den":"", "comb_val":"",
  #  "p1":"", "p2":"", "p3":"", "p4":"", "p5":"", "p6":"", "p1r":"", "p2r":"", "p3r":"", "p4r":"", "p5r":"", "p6r":""}} 
  #c1["ar"] = cc["ar"]
  #us_row = app_tables.lucru.get(user=id)
  #us_row.update(ar=c1)
#pass




