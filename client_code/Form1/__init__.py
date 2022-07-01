from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    lit = anvil.server.call("litigii", "sonimpex")
    self.repeating_panel_1.items = json.loads(lit)
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    pass

