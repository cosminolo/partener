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
    self.link_1.width= 120
    self.link_2.width= 120
    
    self.button_1.width=50
    self.button_2.width=50
    self.column_panel_1.width=100
    
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
    if self.login_status.text != "":
        
        open_form("init.start")
    else:
        anvil.users.login_with_form()
        self.ups()
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
    self.ups()
    pass






