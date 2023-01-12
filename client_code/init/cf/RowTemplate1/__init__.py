from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import stripe.checkout
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import My_globals
class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   try:
    lit1=["a", "b", "c", "d", "f", "g", "h", "m", "n", "o", "p", "r", "s", "t"]
    lit2=["e", "i", "j", "k", "l", "x", "y"]
    if self.label_1.text[0] in lit1:
      self.label_1.background="#F8F7CA"
      self.text_box_1.background="#CAECF8"
      self.text_box_2.background="#CAECF8"
      self.text_box_3.background="#CAECF8"
      self.text_box_4.background="#CAECF8"
      self.text_box_5.background="#CAECF8"
      self.text_box_6.background="#CAECF8"
      self.text_box_7.background="#CAECF8"
      self.text_box_8.background="#CAECF8"
      self.text_box_9.background="#CAECF8"
      self.text_box_10.background="#CAECF8"
      self.text_box_11.background="#CAECF8"
      self.text_box_12.background="#CAECF8"
      self.text_box_13.background="#CAECF8"
      self.text_box_14.background="#CAECF8"
      self.text_box_15.background="#CAECF8"
      self.text_box_16.background="#CAECF8"
      self.text_box_17.background="#CAECF8"
      self.text_box_18.background="#CAECF8"
      self.text_box_19.background="#CAECF8"
    if self.label_1.text[0] in lit2:
      self.label_1.background="#E3F9A9"
      self.text_box_1.background="#E3F9A9"
      self.text_box_1.enabled = False
      self.text_box_2.background="#E3F9A9"
      self.text_box_2.enabled = False
      self.text_box_3.background="#E3F9A9"
      self.text_box_3.enabled = False
      self.text_box_4.background="#E3F9A9"
      self.text_box_4.enabled = False
      self.text_box_5.background="#E3F9A9"
      self.text_box_5.enabled = False
      self.text_box_6.background="#E3F9A9"
      self.text_box_6.enabled = False
      self.text_box_7.background="#E3F9A9"
      self.text_box_7.enabled = False
      self.text_box_8.background="#E3F9A9"
      self.text_box_8.enabled = False
      self.text_box_9.background="#E3F9A9"
      self.text_box_9.enabled = False
      self.text_box_10.background="#E3F9A9"
      self.text_box_10.enabled = False
      self.text_box_11.background="#E3F9A9"
      self.text_box_12.enabled = False
      self.text_box_12.background="#E3F9A9"
      self.text_box_12.enabled = False
      self.text_box_13.background="#E3F9A9"
      self.text_box_13.enabled = False
      self.text_box_14.background="#E3F9A9"
      self.text_box_14.enabled = False
      self.text_box_15.background="#E3F9A9"
      self.text_box_15.enabled = False
      self.text_box_16.background="#E3F9A9"
      self.text_box_16.enabled = False
      self.text_box_17.background="#E3F9A9"
      self.text_box_17.enabled = False
      self.text_box_18.background="#E3F9A9"
      self.text_box_18.enabled = False
      self.text_box_19.background="#E3F9A9"
      self.text_box_19.enabled = False
   except:
      pass
      

  def text_box_1_lost_focus(self, **event_args):   
   if self.text_box_1.enabled == True:
    s = self.text_box_1.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):        
        My_globals.ccf= self.calcul(My_globals.ccf)
        get_open_form('cf').refr()
        self.u_cf(My_globals.ccf, My_globals.premis)
        get_open_form('cf').refr()
        pass
    else:         
        self.text_box_1.text = 0     
        alert("Doar numar fara zecimale sau separatori!")   
   pass
  def calcul(self, js):
    js[4]["an_ant"]= 23650
    return js
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
    pass  
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass 
