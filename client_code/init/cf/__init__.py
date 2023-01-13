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
    self.data_grid_1.role = 'wide'                                   
  def charge(self):     
      ccf = anvil.server.call("get_cf", self.ups())      
      cf={}
      cf=json.loads(ccf)
      premis = cf["premise"]  
      self.item = premis
      #My_globals.premis=self.item      
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
    
  def refr(self):    
    js=self.repeating_panel_1.items 
    list_key = ["an_ant", "an_c", "an_2", "an_3", "an_4", "an_5", "an_6", "an_7", "an_8", "an_9", "an_10", "an_11", "an_12", "an_13", "an_14", "an_15", "an_16", "an_17", "an_18"]
    try:
      for i in list_key:      
        js[4][i]=int(js[1][i])+int(js[2][i])-int(js[3][i])
        js[8][i]=round(-1*(int(js[5][i])+int(js[6][i])-int(js[7][i]))*int(js[1][i])/(int(js[0][i])*30))
        js[9][i]=round(int(js[4][i])+int(js[8][i]))
        js[11][i]=round(int(js[9][i])+int(js[10][i]))
        js[19][i]=int(js[12][i])+int(js[13][i])+int(js[14][i])-int(js[15][i])+int(js[16][i])+int(js[17][i])-int(js[18][i])
        if int(js[19][i])>0:
          js[20][i]=round(int(js[11][i]) / int(js[19][i]),1)
        else:
          js[20][i]=1.2
      self.repeating_panel_1.items=js
      self.u_cf(js, self.item)
    except:      
      js[4][i]=0
      js[8][i]=0
      js[9][i]=0
      js[11][i]=0
      js[19][i]=0
      js[20][i]=0
      self.repeating_panel_1.items[4][i]=0
      self.repeating_panel_1.items[8][i]=0
      self.repeating_panel_1.items[9][i]=0
      self.repeating_panel_1.items[11][i]=0
      self.repeating_panel_1.items[19][i]=0
      self.repeating_panel_1.items[20][i]=0
      self.repeating_panel_1.items=self.repeating_panel_1.items
      self.u_cf(js, self.item)      
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
    
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  def u_cf(self, js1, js2):
    #js1=self.item
    #js2 = My_globals.premis
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
    #print(jsf[0])
    pass  

  def button_3_click(self, **event_args):
    
    pass

  def text_area_1_lost_focus(self, **event_args):
    self.u_cf(self.repeating_panel_1.items, self.item)
    pass
  
  

  def text_area_2_lost_focus(self, **event_args):
    self.u_cf(self.repeating_panel_1.items, self.item)
    pass

  def text_area_3_lost_focus(self, **event_args):
    self.u_cf(self.repeating_panel_1.items, self.item)
    pass







