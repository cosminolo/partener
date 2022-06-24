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
    self.text_box_7.text = self.sum_clasa("2", "D1")
    self.text_box_8.text = self.sum_clasa("2", "D2")
    self.text_box_9.text = self.sum_clasa("2", "D3")
    self.text_box_10.text = self.sum_clasa("2", "C1")
    self.text_box_11.text = self.sum_clasa("2", "C2")
    self.text_box_12.text = self.sum_clasa("2", "C3")
    self.text_box_13.text = self.sum_clasa("3", "D1")
    self.text_box_14.text = self.sum_clasa("3", "D2")
    self.text_box_15.text = self.sum_clasa("3", "D3")
    self.text_box_16.text = self.sum_clasa("3", "C1")
    self.text_box_17.text = self.sum_clasa("3", "C2")
    self.text_box_18.text = self.sum_clasa("3", "C3")
    self.text_box_19.text = self.sum_clasa("4", "D1")
    self.text_box_20.text = self.sum_clasa("4", "D2")
    self.text_box_21.text = self.sum_clasa("4", "D3")
    self.text_box_22.text = self.sum_clasa("4", "C1")
    self.text_box_23.text = self.sum_clasa("4", "C2")
    self.text_box_24.text = self.sum_clasa("4", "C3")
    self.text_box_25.text = self.sum_clasa("5", "D1")
    self.text_box_26.text = self.sum_clasa("5", "D2")
    self.text_box_27.text = self.sum_clasa("5", "D3")
    self.text_box_28.text = self.sum_clasa("5", "C1")
    self.text_box_29.text = self.sum_clasa("5", "C2")
    self.text_box_30.text = self.sum_clasa("5", "C3")
    self.text_box_31.text = self.sum_clasa("6", "D1")
    self.text_box_32.text = self.sum_clasa("6", "D2")
    self.text_box_33.text = self.sum_clasa("6", "D3")
    self.text_box_34.text = self.sum_clasa("6", "C1")
    self.text_box_35.text = self.sum_clasa("6", "C2")
    self.text_box_36.text = self.sum_clasa("6", "C3")
    self.text_box_37.text = self.sum_clasa("7", "D1")
    self.text_box_38.text = self.sum_clasa("7", "D2")
    self.text_box_39.text = self.sum_clasa("7", "D3")
    self.text_box_40.text = self.sum_clasa("7", "C1")
    self.text_box_41.text = self.sum_clasa("7", "C2")
    self.text_box_42.text = self.sum_clasa("7", "C3")
    self.text_box_43.text = "{:,}".format(int(self.text_box_1.text + self.text_box_7.text
                            + self.text_box_13.text + self.text_box_19.text
                            + self.text_box_25.text + self.text_box_31.text
                            + self.text_box_37.text))
    self.text_box_44.text = "{:,}".format(self.text_box_2.text + self.text_box_8.text
                            + self.text_box_14.text + self.text_box_20.text
                            + self.text_box_26.text + self.text_box_32.text
                            + self.text_box_38.text)
    self.text_box_45.text = "{:,}".format(self.text_box_3.text + self.text_box_9.text
                            + self.text_box_15.text + self.text_box_21.text
                            + self.text_box_27.text + self.text_box_33.text
                            + self.text_box_39.text)
    self.text_box_46.text = "{:,}".format(self.text_box_4.text + self.text_box_10.text
                            + self.text_box_16.text + self.text_box_22.text
                            + self.text_box_28.text + self.text_box_34.text
                            + self.text_box_40.text)
    self.text_box_47.text = "{:,}".format(self.text_box_5.text + self.text_box_11.text
                            + self.text_box_17.text + self.text_box_23.text
                            + self.text_box_29.text + self.text_box_35.text
                            + self.text_box_41.text)
    self.text_box_48.text = "{:,}".format(self.text_box_6.text + self.text_box_12.text
                            + self.text_box_18.text + self.text_box_24.text
                            + self.text_box_30.text + self.text_box_36.text
                            + self.text_box_42.text)
    
    
    pass
  
  def sum_clasa (self, cl, col):
    
    nr = len(My_globals.bal)
    s = int(0)
    for i in range (0,nr):
      if str(My_globals.bal[i]['Cont'])[:1] == cl:
        if My_globals.bal[i][col]:
          s = s + int(My_globals.bal[i][col])
    return s

