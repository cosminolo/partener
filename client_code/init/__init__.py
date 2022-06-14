from ._anvil_designer import initTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class init(initTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
    self.ups()
    
  def ups(self):
      # Get the currently logged in user (if any)
      self.login_status.text = ""
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          self.login_status.text = us
          anvil.server.call("add_user", us)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("init.start")
    pass

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('init.fin')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    self.ups()
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    pass






