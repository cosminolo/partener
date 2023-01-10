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
    #ccf = []
    cf = {int("0"):{"den":"Nr luni in perioada", "an_ant":"`12", "an_c":"", "an_2":""},
         int("1"):{"den":"Cifra de afaceri", "an_ant":"`0", "an_c":"0", "an_2":"0"}}
    #ccf.append(cf)    
    self.repeating_panel_1.items=cf
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    js=self.repeating_panel_1.items[0]
    print(js)
    pass




