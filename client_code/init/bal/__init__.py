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
from . import refre

class bal(balTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    My_globals.bal = anvil.server.call("get_bal", self.ups())
    # Any code you write here will run when the form opens.
    
    self.repeating_panel_1.items = My_globals.bal
    My_globals.cl1=0
    
    self.data_grid_1.show_page_controls = True
    self.data_grid_1.rows_per_page = 50
    self.data_grid_1.role = "wide"  
  
  def ups(self):
      user = anvil.users.get_user()
      if user is None:
        x=0
      else:
          us =  str(user['email'])
          return us
      pass

  def button_1_click(self, **event_args):
    self.text_box_1.text = self.sum_clasa("1", "D1")
    self.text_box_2.text = self.sum_clasa("1", "D2")
    self.text_box_3.text = self.sum_clasa("1", "D3")
    self.text_box_4.text = self.sum_clasa("1", "C1")
    self.text_box_5.text = self.sum_clasa("1", "C2")
    self.text_box_6.text = self.sum_clasa("1", "C3")
    pass
  
  def sum_clasa (self, cl, col):
    
    nr = len(My_globals.bal)
    s = int(0)
    for i in range (0,nr):
      if str(My_globals.bal[i]['Cont'])[:1] == cl:
        if My_globals.bal[i][col]:
          s = s + int(My_globals.bal[i][col])
    return s

