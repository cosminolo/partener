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
    global cf
    cf =json.loads(anvil.server.call("get_cf", self.ups()))
    self.item = cf["premise"]    
    self.data_grid_1.role = 'wide'  
    ccf = []
    key_list=[]
    for key in cf.keys():
      ll={}
      if key!="premise":
        ll=cf[key]   
        ccf.append(ll)
        key_list.append(key)
    self.repeating_panel_1.items=ccf
    
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass 
  def button_4_click(self, **event_args):
    open_form('init')
    pass

  def button_5_click(self, **event_args):
    open_form('init.analiza')
    pass

  def button_1_click(self, **event_args):
    print(cf)
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    js1=self.repeating_panel_1.items
    js2 = self.item
    jsf=[]
    for i in range(0,len(js1)):
      js_int={}
      js_int["a"]=js1[0]
      js_int["b"]=js1[1]
    jsf.append(js_int)
    js_int["premise"]=js2
    jsf.append(js_int)
    anvil.server.call("upp_cf", self.ups(), jsf[0])  
    pass




