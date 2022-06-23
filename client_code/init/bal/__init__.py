from ._anvil_designer import balTemplate
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

class bal(balTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    My_globals.bal = anvil.server.call("get_bal", self.ups())
    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = My_globals.bal
    print(My_globals.bal)
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass