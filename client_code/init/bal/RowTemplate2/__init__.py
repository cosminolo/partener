from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import My_globals
import json
import string

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    global us
    us = self.ups()
    self.init_components(**properties)
    if self.label_6.text == "P":
       self.text_box_1.enabled = False
       self.text_box_1.background="#E0E0E0"
       self.text_box_3.enabled = False 
       self.text_box_3.background="#E0E0E0" 
       self.text_box_5.enabled = False 
       self.text_box_5.background="#E0E0E0" 
       self.text_box_2.enabled = True
       self.text_box_2.background="#CAECF8" 
       self.text_box_4.enabled = True
       self.text_box_4.background="#CAECF8"  
       self.text_box_6.enabled = True
       self.text_box_6.background="#CAECF8"
    else:
       self.text_box_1.enabled = True
       self.text_box_1.background="#CAECF8" 
       self.text_box_3.enabled = True
       self.text_box_3.background="#CAECF8"  
       self.text_box_5.enabled = True 
       self.text_box_5.background="#CAECF8"  
       self.text_box_2.enabled = True
       self.text_box_2.background="#CAECF8" 
       self.text_box_4.enabled = True
       self.text_box_4.background="#CAECF8"  
       self.text_box_6.enabled = True
       self.text_box_6.background="#CAECF8"
      
    if self.label_6.text == "A":
       self.text_box_1.enabled = True
       self.text_box_1.background="#CAECF8"  
       self.text_box_3.enabled = True 
       self.text_box_3.background="#CAECF8"  
       self.text_box_5.enabled = True 
       self.text_box_5.background="#CAECF8" 
       self.text_box_2.enabled = False 
       self.text_box_2.background="#E0E0E0" 
       self.text_box_4.enabled = False 
       self.text_box_4.background="#E0E0E0" 
       self.text_box_6.enabled = False 
       self.text_box_6.background="#E0E0E0" 
      
    # Any code you write here will run when the form opens.
    if str(self.label_1.text)[:1] == "T":
      self.label_2.bold = True
      cl = str(self.label_1.text)[1:]
      self.text_box_1.text = self.sum_clasa(cl, "D1")
      self.text_box_1.bold = True
      self.text_box_1.background= "#E0F8CA"
      self.text_box_2.text = self.sum_clasa(cl, "C1")
      self.text_box_2.bold = True
      self.text_box_2.background= "#E0F8CA"
      self.text_box_3.text = self.sum_clasa(cl, "D2")
      self.text_box_3.bold = True
      self.text_box_3.background= "#E0F8CA"
      self.text_box_4.text = self.sum_clasa(cl, "C2")
      self.text_box_4.bold = True
      self.text_box_4.background= "#E0F8CA"
      self.text_box_5.text = self.sum_clasa(cl, "D3")
      self.text_box_5.bold = True
      self.text_box_5.background= "#E0F8CA"
      self.text_box_6.text = self.sum_clasa(cl, "C3")
      self.text_box_6.bold = True
      self.text_box_6.background= "#E0F8CA"
    
  pass

  def text_box_1_lost_focus(self, **event_args):
   if self.text_box_1.enabled == True:
    s = self.text_box_1.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_1.text = 0     
        alert("Doar numar fara zecimale sau separatori!")   
   pass

  def text_box_2_lost_focus(self, **event_args):
   if self.text_box_2.enabled == True:
    s = self.text_box_2.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_2.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass
  
  def form_show(self, **event_args):
    """This method is called when the data row panel is shown on the screen"""
   
    pass

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    
    pass

  def text_box_3_lost_focus(self, **event_args):
   if self.text_box_3.enabled == True:
    s = self.text_box_3.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_3.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

  def text_box_4_lost_focus(self, **event_args):
   if self.text_box_4.enabled == True:
    s = self.text_box_4.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_4.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

  def text_box_5_lost_focus(self, **event_args):
   if self.text_box_5.enabled == True:
    s = self.text_box_5.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_5.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

  def text_box_6_lost_focus(self, **event_args):
   if self.text_box_6.enabled == True: 
    s = self.text_box_6.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_6.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass

  









