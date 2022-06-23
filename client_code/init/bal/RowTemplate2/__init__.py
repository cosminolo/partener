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

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
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

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.label_6.text == "P":
      self.text_box_1.text =""
    
    
  pass

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    if self.text_box_1.text.isdigit() or (self.text_box_1.text.startswith("-") and S[1:].isdigit()):
        pass
    else:         
        text_box_1.text = 0     
        alert("Just numbers without decimal")    
    pass


