from ._anvil_designer import finTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class fin(finTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def text_box_108_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
  
  def v(self, tt):
   if self.text_box_4.enabled == True:
    s = self.text_box_4.text
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        anvil.server.call('upp_bal', us, My_globals.bal)
        pass
    else:         
        self.text_box_4.text = 0     
        alert("Doar numar fara zecimale sau separatori!") 
   pass

