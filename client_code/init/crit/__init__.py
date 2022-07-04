from ._anvil_designer import critTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class crit(critTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    open_form('init')
    pass

  def check_box_5_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def button_2_click(self, **event_args):
    open_form('init.verific')
    pass

  def button_3_click(self, **event_args):
    open_form('init.bal')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    a = "True"
    self.check_box_1.checked = eval(a)
    pass





