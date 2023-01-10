from ._anvil_designer import cfTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
class cf(cfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    

  def button_4_click(self, **event_args):
    open_form('init')
    pass

  def button_5_click(self, **event_args):
    open_form('init.analiza')
    pass

  def button_1_click(self, **event_args):
    ccf = []
    cf = {"a":{"den":"Nr. luni in perioada (12 luni sau cate au ramas pana la finele anului )", "an_ant":"", "an_c":"", "an_2":""},
         "b":{"den":"Cifra de afaceri", "an_ant":"0", "an_c":"0", "an_2":"0"}}
    key_list=[]
    for key in cf.keys():
      ll={}
      ll=cf[key]   
      ccf.append(ll)
      key_list.append(key)
    self.repeating_panel_1.items=ccf  
    print(key_list)
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    js=self.repeating_panel_1.items
    jsf=[]
    for i in range(0,len(js)):
      js1={}
      js1["a"]=js[0]
      js1["b"]=js[1]
      jsf.append(js1)
    print(jsf[0])  
    pass




