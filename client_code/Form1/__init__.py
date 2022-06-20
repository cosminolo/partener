
from ._anvil_designer import Form1Template
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..init.start import start
import json
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.xy_panel_1.clear()
   
    global txb
    txb = self.txb = {}
    global i
    global j
    global fin
    global d
    i = 1
    j = 0   
    fin = {1: 231, 2: 300}
    d={}
    for i in range(1, 9): # col 
      #k=10+i  
      if i >0:
       k=1
       self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              border="solid black 2px",
                              foreground="#000",background="#fff",placeholder=f"place{k}")
       self.txb[k].role = "input" #"form-control"
       self.txb[k].tag.name =  k
       self.txb[k].text = fin[k]  
       #self.txb[k] = self.item["cont"]   
       
       self.xy_panel_1.add_component(self.txb[k], x=1, y=1)
       self.txb[k].set_event_handler('lost_focus', self.l_focus) 
       k = k+1
       self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff",placeholder=f"place{k}")
       self.txb[k].role = "input" #"form-control"
       self.txb[k].tag.name = k
       self.txb[k].text = fin[k]  
       #self.item = fin["suma"] 
       self.xy_panel_1.add_component(self.txb[k], x=10, y=10)
       #self.txb[k].set_event_handler('lost_focus', self.l_focus)  
        
    
     
  def l_focus (self, sender,**event_args):
    
    #print(sender.tag.name)   
    
    if not sender.text:
      pass
    else:
      S = sender.text
      if S.isdigit() or (S.startswith("-") and S[1:].isdigit()):
        x = sender.tag.name
        fin[x] = sender.text
        print(fin)
      else:         
        sender.text = 0     
        alert("Just numbers without decimal")        
    pass

