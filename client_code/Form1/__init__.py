
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
    
    self.column_panel_1.clear()
   
    global txb
    txb = self.txb = {}
    global i
    global j
    global fin
    i = 1
    j = 0   
    fin = {"cont": 231, "suma": 300}
    self.item = fin
    for i in range(1, 9): # col 
      k=10+i  
      if i == 1:
       self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff",placeholder=f"place{k}")
       self.txb[k].role = "input" #"form-control"
       self.txb[k].tag.name = k
       self.txb[k].text = self.item["cont"]  
       #self.item = fin["cont"] 
       self.column_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=1)
       self.txb[k].set_event_handler('lost_focus', self.l_focus) 
       k = k+1
       self.txb[k] = TextBox(type="text", font="Arial", font_size="10",
                              spacing_above = "small",
                              spacing_below = "none",
                              width=80,
                              foreground="#000",background="#fff",placeholder=f"place{k}")
       self.txb[k].role = "input" #"form-control"
       self.txb[k].tag.name = k
       self.txb[k].text = self.item["suma"]  
       #self.item = fin["suma"] 
       self.column_panel_1.add_component(self.txb[k], row=1, col_xs=0, width_xs=1)
       self.txb[k].set_event_handler('lost_focus', self.l_focus)  
        
        
        
        
        
    
  def l_focus (self, sender,**event_args):
    #print(self.item)
    #print(sender.tag.name)   
    
    if not sender.text:
      pass
    else:
      S = sender.text
      if S.isdigit() or (S.startswith("-") and S[1:].isdigit()):
               
        
        pass
      else:         
        sender.text = 0     
        alert("Just numbers without decimal")        
    pass

