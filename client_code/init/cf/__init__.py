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
    self.charge()
  def charge(self):      
      cf={}
      ccf =anvil.server.call("get_cf", self.ups())
      cf=json.loads(ccf)
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
      pass   
     
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
      js_int["c"]=js1[2]
      js_int["d"]=js1[3]
      js_int["e"]=js1[4]
      js_int["f"]=js1[5]
      js_int["g"]=js1[6]
      js_int["h"]=js1[7]
      js_int["i"]=js1[8]
      js_int["j"]=js1[9]
      js_int["k"]=js1[10]
      js_int["l"]=js1[11]
      js_int["m"]=js1[12]
      js_int["n"]=js1[13]
      js_int["o"]=js1[14]
      js_int["p"]=js1[15]
      js_int["r"]=js1[16]
      js_int["s"]=js1[17]
      js_int["t"]=js1[18]
      js_int["x"]=js1[19]
      js_int["y"]=js1[20]
    jsf.append(js_int)
    js_int["premise"]=js2
    jsf.append(js_int)
    anvil.server.call("upp_cf", self.ups(), jsf[0])  
    pass




